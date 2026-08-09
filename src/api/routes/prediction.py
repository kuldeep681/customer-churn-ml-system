from fastapi import APIRouter
from src.api.schemas.prediction_schema import ChurnRequest
from src.services.prediction_service import predict

router = APIRouter()


@router.post("/predict")
def predict_churn(data: ChurnRequest):
    result = predict(data.dict())
    return result