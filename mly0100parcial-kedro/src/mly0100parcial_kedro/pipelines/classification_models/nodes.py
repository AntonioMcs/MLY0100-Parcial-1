import logging
from typing import Dict, Tuple

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)


logger = logging.getLogger(__name__)


def split_data(data: pd.DataFrame, parameters: dict) -> Tuple[pd.DataFrame, ...]:
    """
    Separa el dataset de diabetes en train/test.
    Usa estratificación por 'Outcome' para mantener proporción.
    """
    features = parameters["features"]
    target = parameters["target"]

    X = data[features]
    y = data[target]
    if isinstance(y, pd.DataFrame):
        y = y.values.ravel()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=parameters["test_size"],
        random_state=parameters["random_state"],
        stratify=y,
    )

    return X_train, X_test, y_train, y_test


def train_models(X_train: pd.DataFrame, y_train: pd.Series) -> Dict[str, object]:
    """
    Entrena varios modelos de clasificación binaria para diabetes.
    """
    models = {
        "LogisticRegression": LogisticRegression(max_iter=1000),
        "KNN": KNeighborsClassifier(),
        "RandomForest": RandomForestClassifier(random_state=42),
        "GradientBoosting": GradientBoostingClassifier(random_state=42),
        "SVC": SVC(probability=True, random_state=42),
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        logger.info("✅ Modelo %s entrenado", name)

    return models


def evaluate_models(
    models: Dict[str, object], X_test: pd.DataFrame, y_test: pd.Series
) -> Dict[str, dict]:
    """
    Evalúa cada modelo con métricas de clasificación:
    - accuracy, precision, recall, F1, ROC-AUC.
    """
    results: Dict[str, dict] = {}

    for name, model in models.items():
        y_pred = model.predict(X_test)

        if hasattr(model, "predict_proba"):
            y_prob = model.predict_proba(X_test)[:, 1]
            roc_auc = roc_auc_score(y_test, y_prob)
        else:
            roc_auc = None

        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred, zero_division=0),
            "recall": recall_score(y_test, y_pred, zero_division=0),
            "f1": f1_score(y_test, y_pred, zero_division=0),
            "roc_auc": roc_auc,
        }

        results[name] = metrics
        logger.info("📊 Métricas %s: %s", name, metrics)

    return results


def select_best_model(
    evaluation_results: Dict[str, dict], models: Dict[str, object]
):
    """
    Selecciona el mejor modelo usando F1 como métrica principal
    (puedes cambiar a recall si la rúbrica favorece sensibilidad).
    """
    best_name = max(evaluation_results, key=lambda m: evaluation_results[m]["f1"])
    best_model = models[best_name]

    logger.info("🏆 Mejor modelo: %s", best_name)
    logger.info("Métricas del mejor modelo: %s", evaluation_results[best_name])

    return best_model, evaluation_results
