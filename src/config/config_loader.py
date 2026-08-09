import yaml
from pathlib import Path

def load_config(config_path="config.yaml"):
    config_file = Path(config_path)
    
    if not config_file.exists():
        raise FileNotFoundError(f"Config file not found at {config_path}")
    
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    
    return config

# Singleton-like usage
CONFIG = load_config()