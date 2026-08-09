import yaml
from pathlib import Path


def load_config(config_path: str = "config.yaml"):
    """
    Load configuration file from project root
    """

    # 🔥 Get project root (2 levels up from this file)
    base_path = Path(__file__).resolve().parents[2]

    config_file = base_path / config_path

    if not config_file.exists():
        raise FileNotFoundError(f"Config file not found at {config_file}")

    with open(config_file, "r") as file:
        config = yaml.safe_load(file)

    return config


# 🔥 Singleton (load once)
CONFIG = load_config()