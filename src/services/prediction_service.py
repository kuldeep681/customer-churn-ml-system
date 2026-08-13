from src.models.predict_model import (
    predict_churn,
    explain_churn,
)


def get_risk_level(probability: float) -> str:
    """
    Convert churn probability into a human-readable risk level.
    """

    if probability > 0.7:
        return "High"
    elif probability > 0.4:
        return "Medium"
    else:
        return "Low"


def predict(input_data: dict):
    """
    Application-level prediction service.

    Delegates the actual ML prediction to predict_churn()
    and adds the business-level risk classification.
    """

    # Core ML prediction
    prediction, probability = predict_churn(input_data)

    # Business-level risk classification
    risk_level = get_risk_level(probability)

    return {
        "churn_prediction": prediction,
        "churn_probability": probability,
        "risk_level": risk_level,
    }


def explain(input_data: dict):
    """
    Application-level explanation service.

    Generates the prediction and attaches the most influential
    SHAP features to explain the model output.
    """

    # Get normal prediction
    prediction, probability = predict_churn(input_data)

    # Calculate risk level
    risk_level = get_risk_level(probability)

    # Generate SHAP explanation
    explanation = explain_churn(input_data)

    return {
        "churn_prediction": prediction,
        "churn_probability": probability,
        "risk_level": risk_level,
        "explanation": explanation,
    }