import joblib
from pathlib import Path
from src.config.config_loader import load_config


def load_model():
    config = load_config()

    base_path = Path(__file__).resolve().parents[2]
    model_path = base_path / config["model"]["model_path"]

    if not model_path.exists():
        raise FileNotFoundError(f"Model not found at {model_path}")

    artifact = joblib.load(model_path)

    model = artifact["model"]
    preprocessor = artifact["preprocessor"]
    threshold = artifact.get("threshold", 0.5)

    return model, preprocessor, threshold
