
from keyboard_productivity_predictor import predict_keyboard_productivity
sample_features = {
    "DU.key1.key1_median": 0.095,
    "DU.key1.key2_median": 0.3045,
    "unique_key1_count": 20,
    "unique_transition_count": 38,
    "consecutive_key1_repetition_rate": 0.0,
    "backspace_rate": 0.0,
}

score = predict_keyboard_productivity(sample_features)

print(f"Predicted keyboard productivity score: {score:.2f}")