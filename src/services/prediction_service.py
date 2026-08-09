import joblib
import numpy as np
import pandas as pd
from pathlib import Path

from src.config.config_loader import load_config


# 🔹 Load model once (important for performance)
config = load_config()
base_path = Path(__file__).resolve().parents[2]
model_path = base_path / config["model"]["model_path"]

artifact = joblib.load(model_path)
model = artifact["model"]
preprocessor = artifact["preprocessor"]


def get_risk_level(probability: float) -> str:
    if probability > 0.7:
        return "High"
    elif probability > 0.4:
        return "Medium"
    else:
        return "Low"


def predict(input_data: dict):
    # 🔹 Convert to DataFrame
    df = pd.DataFrame([input_data])

    # 🔹 Apply preprocessing
    X_transformed = preprocessor.transform(df)

    # 🔹 Prediction
    prediction = int(model.predict(X_transformed)[0])
    probability = float(model.predict_proba(X_transformed)[0][1])

    # 🔹 Risk Level
    risk_level = get_risk_level(probability)

    return {
        "churn_prediction": prediction,
        "churn_probability": probability,
        "risk_level": risk_level
    }