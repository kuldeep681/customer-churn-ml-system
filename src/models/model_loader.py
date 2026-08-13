import joblib
from functools import lru_cache
from pathlib import Path

from src.config.config_loader import load_config


@lru_cache(maxsize=1)
def load_model():
    """
    Load the trained ML pipeline and prediction threshold.

    The saved artifact contains:
        - pipeline: preprocessing + XGBoost model
        - threshold: probability threshold used for classification

    The model is cached so the artifact is loaded only once
    during the application's lifetime.
    """

    config = load_config()

    base_path = Path(__file__).resolve().parents[2]
    model_path = base_path / config["model"]["model_path"]

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model not found at {model_path}"
        )

    artifact = joblib.load(model_path)

    if "pipeline" not in artifact:
        raise KeyError(
            "Saved model artifact does not contain 'pipeline'."
        )

    pipeline = artifact["pipeline"]
    threshold = artifact.get("threshold", 0.5)

    return pipeline, threshold