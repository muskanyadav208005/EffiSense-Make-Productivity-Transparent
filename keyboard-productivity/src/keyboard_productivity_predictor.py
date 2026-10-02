
from pathlib import Path
import joblib
import pandas as pd

# Locate the saved model relative to this script
PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "xgboost_keyboard_productivity.pkl"

FEATURE_COLUMNS = [
    "DU.key1.key1_median",
    "DU.key1.key2_median",
    "unique_key1_count",
    "unique_transition_count",
    "consecutive_key1_repetition_rate",
    "backspace_rate",
]


def predict_keyboard_productivity(features: dict) -> float:
    """Predict a keyboard productivity score from six extracted features."""
    missing = [column for column in FEATURE_COLUMNS if column not in features]
    if missing:
        raise ValueError(f"Missing required features: {missing}")

    input_df = pd.DataFrame(
        [[features[column] for column in FEATURE_COLUMNS]],
        columns=FEATURE_COLUMNS,
    )

    model = joblib.load(MODEL_PATH)
    score = float(model.predict(input_df)[0])

    # Keep the displayed score within the intended 0–100 range.
    return max(0.0, min(100.0, score))