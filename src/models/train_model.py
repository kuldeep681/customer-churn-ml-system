import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

from xgboost import XGBClassifier

from src.config.config_loader import load_config


# =========================================================
# 🔥 MAIN TRAINING FUNCTION
# =========================================================
def train_model(X, y, preprocessor):
    config = load_config()

    # 🔹 Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=config["model"]["test_size"],
        random_state=config["model"]["random_state"],
        stratify=y
    )

    # 🔹 Apply preprocessing
    X_train_transformed = preprocessor.fit_transform(X_train)
    X_test_transformed = preprocessor.transform(X_test)

    # 🔹 Train model (IMPROVED)
    model = XGBClassifier(
        n_estimators=200,
        max_depth=5,
        learning_rate=0.1,
        scale_pos_weight=3,   # 🔥 handle imbalance
        eval_metric='logloss'
    )

    model.fit(X_train_transformed, y_train)

    # 🔹 Predictions (with threshold tuning)
    y_proba = model.predict_proba(X_test_transformed)[:, 1]

    threshold = 0.3  # 🔥 IMPORTANT for recall
    y_pred = (y_proba >= threshold).astype(int)

    # 🔹 Evaluation
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_proba),
    }

    print("\n📊 Model Performance:")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")

    # 🔹 Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    print("\n🧾 Confusion Matrix:")
    print(cm)

    # 🔹 Save model + preprocessor
    base_path = Path(__file__).resolve().parents[2]
    model_path = base_path / config["model"]["model_path"]

    model_path.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(
        {
            "model": model,
            "preprocessor": preprocessor,
            "threshold": threshold   # 🔥 save threshold also
        },
        model_path
    )

    print("\n✅ Model saved successfully!")

    return model, metrics


# =========================================================
# 🔥 CROSS VALIDATION FUNCTION
# =========================================================
def cross_validate_model(X, y, preprocessor):
    model = XGBClassifier(
        n_estimators=200,
        max_depth=5,
        learning_rate=0.1,
        scale_pos_weight=3,
        eval_metric='logloss'
    )

    # 🔹 Pipeline to avoid leakage
    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    scores = cross_val_score(
        pipeline,
        X,
        y,
        cv=skf,
        scoring="recall"   # 🔥 focus metric
    )

    print("\n📊 Cross-Validation Recall Scores:")
    print(scores)

    print(f"\n🔥 Mean Recall: {scores.mean():.4f}")
    print(f"📉 Std Dev: {scores.std():.4f}")

    return scores