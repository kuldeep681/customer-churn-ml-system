import pandas as pd
from src.models.model_loader import load_model


def predict_churn(data: dict):
    """
    Core ML prediction logic
    """

    # 🔹 Convert input to DataFrame
    df = pd.DataFrame([data])

    # 🔹 Load model artifacts
    model, preprocessor, threshold = load_model()

    # 🔹 Transform input
    X_transformed = preprocessor.transform(df)

    # 🔹 Predict probability
    proba = model.predict_proba(X_transformed)[:, 1][0]

    # 🔹 Apply threshold
    prediction = int(proba >= threshold)

    return prediction, float(proba)