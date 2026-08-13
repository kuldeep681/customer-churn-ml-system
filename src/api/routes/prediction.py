from fastapi import APIRouter

from src.api.schemas.prediction_schema import (
    ChurnRequest,
    PredictionResponse,
    ExplainResponse,
)

from src.services.prediction_service import (
    predict,
    explain,
)


router = APIRouter()


@router.post(
    "/predict",
    response_model=PredictionResponse,
)
def predict_churn(data: ChurnRequest):
    """
    Predict customer churn.
    """

    result = predict(data.model_dump())

    return result


@router.post(
    "/explain",
    response_model=ExplainResponse,
)
def explain_churn(data: ChurnRequest):
    """
    Predict customer churn and explain the prediction using SHAP.
    """

    result = explain(data.model_dump())

    return result