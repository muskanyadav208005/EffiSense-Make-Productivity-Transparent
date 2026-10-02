# EffiSense — Keyboard Productivity Modeling

## 1. Overview

The keyboard productivity module analyzes keyboard interaction patterns and constructs a productivity score from selected behavioral features. The module evaluates classical machine-learning models and sequence-based deep-learning models for reproducing this score.

## 2. Dataset Understanding and Cleaning

The raw dataset, `free-text.csv`, contains keyboard-event records, participant identifiers, session identifiers, and timing-related variables.

The data-cleaning process removes rows missing required key and timing values, removes the malformed extra column, and converts the `DU.key1.key1` timing feature to a numeric format. Duplicate rows are retained because repeated observations may represent legitimate keyboard events.

## 3. Windowing and Feature Extraction

The cleaned data is grouped by participant and session. Non-overlapping windows of 50 keyboard events are created, with exactly 10,000 windows selected for feature extraction.

For each window, statistical features are calculated from five timing variables: mean, standard deviation, median, minimum, and maximum.

Additional behavioral features include:

* Unique key count
* Unique transition count
* Consecutive key repetition rate
* Backspace rate

The resulting dataset contains 10,000 windows and 30 behavioral features, together with participant, session, and window identifiers.

## 4. Productivity Score Construction

A constructed productivity score is created using six selected features:

* `DU.key1.key1_median`
* `DU.key1.key2_median`
* `unique_key1_count`
* `unique_transition_count`
* `consecutive_key1_repetition_rate`
* `backspace_rate`

The features are robustly normalized using the 5th and 95th percentiles and clipped to the interval [0, 1].

Timing features are assigned an inverse direction, while key and transition diversity are assigned a positive direction. Repetition and backspace rates are assigned an inverse direction. These directions are design assumptions rather than independently validated behavioral relationships.

The timing-efficiency, activity-diversity, and typing-behavior components are combined with equal weights to produce a score between 0 and 100.

## 5. Model Development

The following models were evaluated:

1. Linear Regression
2. Random Forest Regressor
3. XGBoost Regressor
4. Long Short-Term Memory (LSTM)
5. Gated Recurrent Unit (GRU)

Linear Regression, Random Forest, and XGBoost use the six selected behavioral features. LSTM and GRU use sequences of historical window features with sequence lengths of 5, 10, 20, and 30.

## 6. Evaluation

The classical models use participant-session group-based splitting. Random Forest uses a held-out group split, while XGBoost is evaluated with five-fold GroupKFold.

The sequence models use participant-session group-based train-test splits. Feature scaling is fitted on the training data.

Evaluation metrics include Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R².

## 7. Feature Importance

Random Forest and XGBoost feature-importance values are analyzed to understand which features the models rely on most when reproducing the constructed productivity score.

Consecutive key repetition rate has the highest importance in both models. The relative importance of backspace rate differs between the two models.

Feature importance describes model behavior; it does not establish causation.

## 8. Limitations

The target productivity score is constructed from the same six features supplied to the models. Therefore, high evaluation scores demonstrate reproduction of the constructed target rather than independent validation of real-world employee productivity.

The percentile normalization for the target was calculated using the full dataset before splitting. This is a limitation when interpreting the evaluation results.

The validation split used during neural-network training is not group-aware, even though the outer train-test split is grouped by participant-session.

The timing-feature direction assumptions require further validation before the score can be interpreted as a reliable measure of employee productivity.

## 9. Conclusion

The keyboard productivity module implements a complete pipeline from data cleaning and behavioral feature extraction to score construction, classical machine learning, sequence-based deep learning, and model comparison.

Further work should focus on independent productivity labels, validation of feature-direction assumptions, stricter group-aware validation, and integration into the broader EffiSense application.
