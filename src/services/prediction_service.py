from sqlalchemy.orm import Session

from src.models.predict_model import (
    predict_churn,
    explain_churn,
)

from src.repositories.prediction_repository import (
    create_prediction,
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


def predict(
    input_data: dict,
    db: Session,
):
    """
    Application-level prediction service.

    Performs the ML prediction, determines the risk level,
    and persists the prediction result.
    """

    # ---------------------------------------------------------
    # Core ML prediction
    # ---------------------------------------------------------

    prediction, probability = predict_churn(input_data)

    # ---------------------------------------------------------
    # Business-level risk classification
    # ---------------------------------------------------------

    risk_level = get_risk_level(probability)

    # ---------------------------------------------------------
    # Persist prediction
    # ---------------------------------------------------------

    create_prediction(
        db=db,
        churn_prediction=prediction,
        churn_probability=probability,
        risk_level=risk_level,
    )

    # ---------------------------------------------------------
    # API response
    # ---------------------------------------------------------

    return {
        "churn_prediction": prediction,
        "churn_probability": probability,
        "risk_level": risk_level,
    }


def explain(input_data: dict):
    """
    Application-level explanation service.

    Generates the prediction and attaches the most influential
    SHAP features.

    This operation does NOT persist a database record.
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