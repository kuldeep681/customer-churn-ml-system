from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.schemas.prediction_schema import (
    ChurnRequest,
    PredictionResponse,
    ExplainResponse,
)

from src.database.database import get_db

from src.services.prediction_service import (
    predict,
    explain,
)


router = APIRouter()


@router.post(
    "/predict",
    response_model=PredictionResponse,
)
def predict_churn(
    data: ChurnRequest,
    db: Session = Depends(get_db),
):
    """
    Predict customer churn and store the prediction.
    """

    result = predict(
        data.model_dump(),
        db,
    )

    return result


@router.post(
    "/explain",
    response_model=ExplainResponse,
)
def explain_churn(data: ChurnRequest):
    """
    Predict customer churn and explain the prediction using SHAP.

    Explanation requests are not persisted.
    """

    result = explain(data.model_dump())

    return result