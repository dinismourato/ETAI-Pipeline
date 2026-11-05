import pandas as pd
from src.evaluate import corrected_paired_test

runs = pd.read_csv("results/runs.csv", dtype={"run": str})
xgb = runs[(runs["model"] == "xgboost") & (runs["tuned"] == True)]
with_sel = xgb[xgb["feature_selection"] == "on"].iloc[-1]
without = xgb[xgb["feature_selection"] == "off"].iloc[-1]
folds = [c for c in runs.columns if c.startswith("fold_")]

print(f"with selection:    {with_sel['mean']:.3f} ± {with_sel['std']:.3f}")
print(f"without selection: {without['mean']:.3f} ± {without['std']:.3f}")
print(corrected_paired_test(with_sel[folds].astype(float), without[folds].astype(float), test_train_ratio=1 / 4))