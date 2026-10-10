"""
Entry point for the baseline predictive pipeline.

Run with:
    python main.py

This orchestrates the full (deliberately simple) pipeline:
    load config -> load data -> preprocess -> split -> train
    -> evaluate (train & test) -> save results
"""
"""
Entry point for the baseline predictive pipeline.

Run with:
    python main.py

    load config -> load data -> clean -> drop duplicates (training data only)
    -> features/target -> dev/test split -> Pipeline(preprocessor + model)
    -> evaluate -> save results
"""
import yaml
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import Pipeline

from src.data import load_data
from src.preprocessing import clean_dataset, drop_duplicate_rows, split_features_target, split_dev_test, build_preprocessor
from src.model import build_model
from src.evaluate import cross_validate_pipeline, cv_report, oof_classification_report, fairness_report
from src.results import save_run
from src.model import build_pipeline
from src.tuning import tune_pipeline, nested_cross_validate, tuning_report


def load_config(path: str = "config.yaml") -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


def main():
    config = load_config()

    df = load_data(config["data"]["path"])
    df_clean = clean_dataset(df, config["diagnostics"])                                  # row-preserving
    df_clean = drop_duplicate_rows(df_clean, config["diagnostics"].get("id_column"))     # training data only

    mnar_sources = config["preprocessing"].get("mnar_indicator_sources", [])
    X, y, extras = split_features_target(df_clean, config["data"], mnar_sources)

    X_dev, X_test, y_dev, y_test, extras_dev, extras_test = split_dev_test(
        X, y, extras,
        test_size=config["test_set"]["size"],
        random_state=config["test_set"]["random_state"],
    )

    cv_config = config["cv"]
    shuffle = cv_config.get("shuffle", True)
    cv = StratifiedKFold(n_splits=cv_config["n_splits"], shuffle=shuffle,
                         random_state=cv_config.get("random_state") if shuffle else None)
    scoring = cv_config.get("scoring", "accuracy")
    n_jobs = cv_config.get("n_jobs", 1)

    pipeline = build_pipeline(config["preprocessing"], config["model"])

    fold_scores, y_oof = cross_validate_pipeline(pipeline, X_dev, y_dev, cv, scoring, n_jobs=n_jobs)
    report = cv_report(fold_scores, scoring)

    # week 5: hyperparameter tuning -- on the development set only, every candidate scored by
    # CV of the whole pipeline (see src/tuning.py)
    tuning_config = config.get("tuning", {})
    if tuning_config.get("enabled", False):
        model_type = config["model"]["type"]
        search_spaces = tuning_config.get("search_spaces") or {}
        if model_type not in search_spaces:
            raise ValueError(f"No search space for model type '{model_type}' in config.yaml's "
                             f"tuning.search_spaces. Options: {list(search_spaces)}")
        search_space = search_spaces[model_type]
        n_trials = tuning_config["n_trials"]
        tuning_seed = tuning_config["random_state"]
        inner_cv = StratifiedKFold(n_splits=tuning_config["n_splits"], shuffle=True, random_state=tuning_seed)

        # 1. the honest estimate (its out-of-fold predictions replace the untuned ones)
        nested_scores, y_oof = nested_cross_validate(
            pipeline, X_dev, y_dev, cv, inner_cv, scoring, search_space, n_trials, tuning_seed, n_jobs=n_jobs
        )
        # 2. the hyperparameters we keep: the same procedure, once, on the whole development set
        pipeline, study = tune_pipeline(
            pipeline, X_dev, y_dev, inner_cv, scoring, search_space, n_trials, tuning_seed, n_jobs=n_jobs
        )

        report += "\n\nNested CV (tuned model)\n" + cv_report(nested_scores, scoring)
        report += "\n\n" + tuning_report(study, nested_scores, scoring)

    report += "\n\n" + oof_classification_report(y_dev, y_oof)
    report += "\n" + fairness_report(
        y_dev, y_oof, extras_dev, sensitive_attr=config["data"]["sensitive_attr"]
    )

    # CV estimates the recipe; the model you'd actually use is refit on all development rows
    final_model = pipeline.fit(X_dev, y_dev)
    print(f"Final model: {config['model']['type']} refit on all {len(X_dev)} development rows.")

    results_dir = config.get("output", {}).get("results_dir", "results")
    path = save_run(results_dir, config, report)
    print(f"Full results saved to {path}")


if __name__ == "__main__":
    main()    


'''
    X_train, X_test, y_train, y_test, extras_test = preprocess(
        df,
        target=config["data"]["target"],
        sensitive_attr=config["data"]["sensitive_attr"],X_dev, X_test, y_dev, y_test, extras_dev, extras_test = split_dev_test(
        X, y, extras,
        test_size=config["test_set"]["size"],
        random_state=config["test_set"]["random_state"],
        drop_columns=config["data"]["drop_columns"],
        test_size=config["split"]["test_size"],
        random_state=config["split"]["random_state"],
    )

    model = build_model(config["model"])
    model.fit(X_train, y_train)

    # predict on both splits -- train accuracy vs. test accuracy is how we'll spot overfitting, not just how "good" the model looks
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    report = evaluate(y_train, y_train_pred, y_test, y_test_pred)
    report += "\n" + fairness_report(
        y_test, y_test_pred, extras_test, sensitive_attr=config["data"]["sensitive_attr"]
    )

    results_dir = config.get("output", {}).get("results_dir", "results")
    path = save_run(results_dir, config, report)
    print(f"Full results saved to {path}")

'''

