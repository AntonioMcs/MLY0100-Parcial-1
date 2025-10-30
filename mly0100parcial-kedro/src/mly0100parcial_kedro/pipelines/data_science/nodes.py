import logging
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, max_error
from sklearn.model_selection import train_test_split


def split_data(data: pd.DataFrame, parameters: dict):
    """Divide los datos en conjuntos de entrenamiento y prueba."""
    X = data[parameters["features"]]
    y = data["price"]  # Target continuo (requerimiento de la rúbrica)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test


def train_models(X_train: pd.DataFrame, y_train: pd.Series):
    """Entrena múltiples modelos de regresión."""
    models = {
        "LinearRegression": LinearRegression(),
        "Ridge": Ridge(alpha=1.0),
        "Lasso": Lasso(alpha=0.1),
        "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
        "GradientBoosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
    }

    for name, model in models.items():
        model.fit(X_train, y_train)

    return models


def evaluate_models(models: dict, X_test: pd.DataFrame, y_test: pd.Series):
    """Evalúa cada modelo con métricas de regresión estándar."""
    results = {}
    for name, model in models.items():
        y_pred = model.predict(X_test)
        results[name] = {
            "R2": r2_score(y_test, y_pred),
            "MAE": mean_absolute_error(y_test, y_pred),
            "MSE": mean_squared_error(y_test, y_pred),
            "MaxError": max_error(y_test, y_pred),
        }

    logger = logging.getLogger(__name__)
    logger.info("Resultados de evaluación de modelos:\n%s", results)

    return results


def select_best_model(evaluation_results: dict, models: dict):
    """Selecciona el mejor modelo basado en el R² más alto."""
    best_model_name = max(evaluation_results, key=lambda m: evaluation_results[m]["R2"])
    best_model = models[best_model_name]

    logger = logging.getLogger(__name__)
    logger.info(f"✅ Mejor modelo seleccionado: {best_model_name}")
    logger.info(f"Métricas: {evaluation_results[best_model_name]}")

    return best_model
