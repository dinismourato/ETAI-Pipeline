# Baseline Predictive Pipeline -- ETAI



20261121 - Dinis Pinto 


Comparing the results from week 1 and week 2: 

Week 1: 
logistic_regression
Train accuracy: 0.679
Test accuracy:  0.679
Gap (train - test): -0.000


decision_tree
Train accuracy: 0.829
Test accuracy:  0.624
Gap (train - test): +0.205


Week 2: 
logistic_regression
Train accuracy: 0.680
Test accuracy:  0.676
Gap (train - test): +0.004


decision_tree
Train accuracy: 0.829
Test accuracy:  0.625
Gap (train - test): +0.204


Conclusion of the results: Troughtout the last 2 weeks we were able to explore two different models being used: logistic regression params={'max_iter': 1000} and decision tree with params = {}. Comparing both models in week 1, its fascinating to see that logistic regression has the capability of performing better contrasted to the decision tree since for the logistic the gap between the train and test accuracy is zero and for the decision tree is 0.205. In week 2, with the introduction of the preprocessing we were able to clean parts of the data, with null values and correct values that appear with irregular spaces and gaps in some words. The good part of using this type of approach is that our data gets cleanear and better for modelling but can also contributte for our model to have less data and in consequence can weak our model being use and the performance can be altered. This behaviour being describe, is exactly what happens to Logistic regression. In week 2, this model performs a gap of 0.04, which means a growth of our error in the model and this implies our model not predicting so well (in the majority of the time it does) compared to week 1. The same trend does not happen with decision tree, but also does not improve our model in a significant way, with only a reduction of 0.01 (gap). Summarizing, the preprocessing unfortunaly didnt contribute for the better performance for both models. 


Week 4:

Model: dummy_model  params={}
Test size: 0.2  random_state: 42
============================================================

Train accuracy: 0.549
Test accuracy:  0.550
Gap (train - test): -0.000


Model: random_forest  params={'n_jobs': -1, 'max_depth': 5, 'random_state': 42}
Test size: 0.2  random_state: 42
============================================================

Train accuracy: 0.688
Test accuracy:  0.671
Gap (train - test): +0.018


Model: logistic_regression  params={'max_iter': 2000}
Test size: 0.2  random_state: 42
============================================================

Train accuracy: 0.676
Test accuracy:  0.658
Gap (train - test): +0.018


Model: decision_tree  params={}
Test size: 0.2  random_state: 42
============================================================

Train accuracy: 0.687
Test accuracy:  0.601
Gap (train - test): +0.086

´
Conclusion of the results: Throughtout this week there were main changes in the preprocessing.py, main.py, model.py, config.yaml and results.py. Going deep on each file, the preprocessing was the one that suffered internal changes in many functions used. 
The function clean_dataset(), now can keep every single row and with the introduction of new data, it will do a new prediction. The function drop_duplicate_rows() removes lines and the ones that are duplicated. The split_dev_test(), separates in a new training-test setup with a split of 80-20 and the build_preprocessor() start using the library TargetEncoder. The main.py, now has a new methology, loads and cleans with the clean_dataset and then removes the duplicates with  drop_duplicate_rows. After that, it separates the features with the target and with the function split_dev_test it puts 20% as test and 80% as train. Finally merges the preprocessing and the model in a single pipeline function. In the model.py, there was the introduction of two new models, being the random forest and dummyclassifier. Config.yaml had a new section for the split: test_set (size:0.2, random.state =42). The result.py had a line with alteration being the config(test_set) added and elimination of config(split) for match with the other files. 
Suceeding this description of the alterations in the project, I had develop 4 different outputs, that can be seen up on this readmme file. The outputs in this week concern the two methods talked in the previous classes and with dummy and randomforest. Comparing both methods introducted in this week, dummy was obviously the worst one, since its the basic model and the overall accuracy in the test and train set are both 0.55. On the other hand, random forest gives a better version of results, with Train accuracy: 0.676 and Test accuracy:  0.658. So, we can conclude the performance of the random forest was way better than the basic model used, what allerts for good signs of performance but that can go way better with better coding. Comparing, random forest with the other two methods used in the previous classes, we can say positively that random forest is still the prefered algorithm to predict since the accuracy of both sets (train and test) are better. 


Week 5: 
Run: 20261010_194834
Model: decision_tree  params={}
Test size: 0.2  random_state: 42
============================================================

Cross-validation (5 stratified folds, metric: accuracy)

 fold  train  validation   gap
    1  0.695       0.624 0.071
    2  0.714       0.585 0.129
    3  0.687       0.594 0.093
    4  0.679       0.620 0.059
    5  0.692       0.614 0.078

Train       mean = 0.693   std = 0.013
Validation  mean = 0.607   std = 0.017
Gap         mean = +0.086   std = 0.027


Run: 20261010_195317
Model: logistic_regression  params={'max_iter': 2000}
Test size: 0.2  random_state: 42
============================================================

Cross-validation (5 stratified folds, metric: accuracy)

 fold  train  validation    gap
    1  0.676       0.680 -0.004
    2  0.680       0.654  0.026
    3  0.674       0.675 -0.001
    4  0.672       0.688 -0.016
    5  0.674       0.665  0.010

Train       mean = 0.675   std = 0.003
Validation  mean = 0.672   std = 0.013
Gap         mean = +0.003   std = 0.016


Run: 20261010_195336
Model: dummy_model  params={}
Test size: 0.2  random_state: 42
============================================================

Cross-validation (5 stratified folds, metric: accuracy)

 fold  train  validation    gap
    1  0.549       0.549  0.000
    2  0.549       0.549 -0.000
    3  0.549       0.549 -0.000
    4  0.549       0.549 -0.000
    5  0.549       0.549 -0.000

Train       mean = 0.549   std = 0.000
Validation  mean = 0.549   std = 0.000
Gap         mean = -0.000   std = 0.000



Run: 20261010_195404
Model: random_forest  params={'n_jobs': -1, 'max_depth': 5, 'random_state': 42}
Test size: 0.2  random_state: 42
============================================================

Cross-validation (5 stratified folds, metric: accuracy)

 fold  train  validation    gap
    1  0.692       0.677  0.015
    2  0.698       0.656  0.042
    3  0.687       0.701 -0.014
    4  0.686       0.691 -0.004
    5  0.688       0.682  0.006

Train       mean = 0.690   std = 0.005
Validation  mean = 0.681   std = 0.017
Gap         mean = +0.009   std = 0.022



Conclusion of the results: In this sector, there was the introduction of the cross validation. The validation got rid of only one division of the data. The pipeline started to have a cross validation with 5 folds, with the new definitions also attached in the config.yaml. The preprocessing is made in every single fold and the evaluation fold never influences his own pre-processing. Fariness is also calculated throughout the 5800 prediction, instead of one split test.
With this new introduction of the cross validation our results dont depend on a simple split.
Indeed for the random forest, last week there was an accuracy of Train accuracy: 0.688 and Test accuracy:  0.671, but with this new method now we have a Validation that means the mean of each 5 validation that occured and the final result is 0.607 and std of 0.017 for the 5 folds. Instead of having just one split that could hide the information about the validation now we can see in each fold the validation and the train accuracy and so we can see better if is overfitting. 


This is the **starting point** for your semester project: a small but *complete* predictive pipeline -- every piece a real project needs (entry point, config, data loading, preprocessing, model, evaluation), just kept as simple as possible for now.

The task: predict two-year recidivism using ProPublica's COMPAS
dataset -- the data behind a real 2016 investigation into a risk-
assessment algorithm actually used by US courts to help inform bail and sentencing decisions. See `data/README.md` for the full problem description and a complete data dictionary before you start.

It has some **deliberately weak spots**. Part of your work this
semester is finding them and making them better -- see the pipeline progress table below, which tracks what changes and why as the weeks
go on.

## Project structure

```
.
├── main.py                # entry point: run the whole pipeline
├── config.yaml             # all tunable settings live here
├── requirements.txt
├── src/
│   ├── data.py             # loading
│   ├── preprocessing.py    # cleaning + train/test split
│   ├── model.py             # model construction
│   ├── evaluate.py         # accuracy metrics + fairness check
│   └── results.py          # saves each run's report to disk
├── results/                # created automatically -- one file per run (not tracked in git)
└── data/
    ├── compas_two_year_recidivism.csv
    └── README.md            # problem description + full data dictionary
```

## Pipeline progress

This table is updated after each practical class, so you can always see what changed in the pipeline and why -- it's a running log, not a fixed syllabus.

| Week | Practical class focus | Added to the pipeline |
|------|------------------------|------------------------|
| 2 | Introduction & baseline pipeline | Initial version: project structure, a single naive train/test split (no cross-validation), minimal preprocessing (drop rows with missing values, one-hot encode categoricals), logistic regression baseline, a first (deliberately simple) fairness check comparing our model's and COMPAS's own false-positive rate by race, train-vs-test accuracy reporting (to start spotting overfitting), and each run's full report saved automatically to `results/` |

## Environment setup

You only need to do this once per machine.

### macOS / Linux
```bash
python3 -m venv venv                 # creates an isolated Python environment in a folder called "venv"
source venv/bin/activate             # activates it -- packages install here, not system-wide, and stay out of your other projects
pip install -r requirements.txt      # installs the exact packages this project needs, into that environment
```

### Windows -- PowerShell
```powershell
python -m venv venv                  # creates an isolated Python environment in a folder called "venv"
venv\Scripts\activate                # activates it -- packages install here, not system-wide, and stay out of your other projects
pip install -r requirements.txt      # installs the exact packages this project needs, into that environment
```
If PowerShell blocks the activation script, run this once first:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### Windows -- cmd.exe
Same three steps as above, just with cmd's own activation command:
```cmd
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

Once the environment is active you'll see `(venv)` at the start of your prompt. To leave it later, run `deactivate` (same command on every OS).

### Every time after the first

Creating the environment and installing packages only needs to happen once, ever. Every other time you sit down to work -- a new terminal window, the next practical class, tomorrow -- you don't repeat any of the steps above. From the project's root folder, you just need to:

**macOS / Linux**
```bash
source venv/bin/activate
python main.py
```

**Windows**
```powershell
venv\Scripts\activate
python main.py
```

That's it -- activate, then run. If you don't see `(venv)` at the start of your prompt, the environment isn't active and `python main.py` may use the wrong Python (or fail to find a package) entirely.

## Running the pipeline

With the environment active (see above), from the project's root
folder, on any OS:
```bash
python main.py
```

This loads `config.yaml`, loads and preprocesses the data, trains the model, and prints:
- **train accuracy and test accuracy, side by side.** Comparing the two is how you catch overfitting: if the model looks much better on the data it was trained on than on data it's never seen, it has memorised rather than learned something that generalises. 
- a classification report on the test set
- a false-positive-rate-by-race comparison between our model and
  COMPAS's own score

All of this is also saved to a timestamped file in `results/` (e.g.`results/run_20260916_143012.txt`), so it doesn't just scroll past in your terminal -- open it later, or change something in `config.yaml` (like the model type) and compare the new file to the last one.
`results/` is created automatically the first time you run the
pipeline, and isn't tracked in git (see `.gitignore`) since it's
generated output, not source.

You're free to improve on this structure or restructure it entirely -- what matters is that your project stays runnable end-to-end with a single command, and that each piece (data, preprocessing, model, evaluation) stays easy to find and change independently.

## Dataset

See `data/README.md`.
