# EffiSense Keyboard Productivity

## Overview

This module analyzes keyboard interaction patterns and constructs a keyboard productivity score from selected behavioral features. It evaluates classical machine-learning and sequence-based deep-learning models.

## Project Structure

* `data/raw/`: Original keyboard dataset.
* `data/processed/`: Extracted features, productivity scores, reduced datasets, model results, feature importance, and comparison graphs.
* `notebooks/`: Data understanding, preprocessing, model training, and comparison experiments.
* `src/`: Source-code modules.

## Notebooks

1. `01_data_understanding.ipynb` — Dataset inspection, cleaning, window creation, and feature extraction.
2. `02_preprocessing.ipynb` — Feature selection, normalization, and productivity-score construction.
3. `03_random_forest.ipynb` — Random Forest regression and feature importance.
4. `04_xgboost.ipynb` — XGBoost regression with five-fold GroupKFold evaluation.
5. `05_lstm_gru.ipynb` — LSTM and GRU experiments with sequence lengths of 5, 10, 20, and 30.
6. `06_model_comparison.ipynb` — Saved results, comparisons, graphs, and feature-importance analysis.

## Selected Results

| Model             |      MAE |     RMSE |       R² |
| ----------------- | -------: | -------: | -------: |
| Linear Regression | 5.082782 | 6.554952 | 0.806003 |
| Random Forest     | 1.549929 | 2.095466 | 0.980175 |
| XGBoost           | 0.508000 | 0.673500 | 0.998000 |

The XGBoost values are the recorded mean results across five folds. The other classical-model values are from the recorded held-out evaluation. Sequence-model results are reported separately by sequence length.

## Limitations

The productivity score is constructed from the same six behavioral features supplied to the models. Consequently, strong predictive metrics demonstrate reproduction of the constructed score, not independent validation of real-world employee productivity.

The target normalization uses the complete dataset, and the neural-network validation split is not group-aware. These limitations should be considered when interpreting results.

## Further Work

* Validate the score against independent productivity labels.
* Review feature-direction assumptions.
* Improve group-aware validation.
* Integrate the keyboard productivity module into the broader EffiSense application.

