from src.data.preprocess import clean_data, split_features_target, build_preprocessor
from src.models.train_model import train_model
import pandas as pd


def main():
    print("🚀 Training started...")

    # 🔹 Load data
    df = pd.read_csv("data/raw/churn.csv")

    # 🔹 Preprocess
    df = clean_data(df)
    X, y = split_features_target(df)

    # 🔹 Build preprocessor
    preprocessor = build_preprocessor(X)

    # 🔹 Train model
    train_model(X, y, preprocessor)

    print("✅ Training completed!")


if __name__ == "__main__":
    main()