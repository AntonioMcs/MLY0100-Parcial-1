import logging
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


# ------------------------------------------------------------
# 🔹 División de los datos
# ------------------------------------------------------------
def split_data(data: pd.DataFrame, parameters: dict) -> tuple:
    """
    Divide los datos en conjuntos de entrenamiento y prueba.
    """
    X = data[parameters["features"]]
    y = data["price"]  # Variable objetivo (target continuo)
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=parameters["test_size"],
        random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test


# ------------------------------------------------------------
# 🔹 Entrenamiento con múltiples modelos de regresión
# ------------------------------------------------------------
def train_models(X_train: pd.DataFrame, y_train: pd.Series) -> dict:
    """
    Entrena varios modelos de regresión supervisada.
    """
    models = {
        "LinearRegression": LinearRegression(),
        "Ridge": Ridge(alpha=1.0),
        "Lasso": Lasso(alpha=0.1),
        "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
        "GradientBoosting": GradientBoostingRegressor(random_state=42)
    }

    trained_models = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        trained_models[name] = model

    return trained_models


# ------------------------------------------------------------
# 🔹 Evaluación de modelos
# ------------------------------------------------------------
def evaluate_models(trained_models: dict, X_test: pd.DataFrame, y_test: pd.Series) -> pd.DataFrame:
    """
    Evalúa todos los modelos y retorna un DataFrame con las métricas.
    """
    logger = logging.getLogger(__name__)
    results = []

    for name, model in trained_models.items():
        y_pred = model.predict(X_test)

        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        results.append({
            "Modelo": name,
            "MAE": mae,
            "RMSE": rmse,
            "R2": r2
        })

        logger.info(f"Modelo {name}: R2={r2:.3f}, MAE={mae:.3f}, RMSE={rmse:.3f}")

    results_df = pd.DataFrame(results).sort_values(by="R2", ascending=False).reset_index(drop=True)
    return results_df


# ------------------------------------------------------------
# 🔹 Selección del mejor modelo
# ------------------------------------------------------------
def select_best_model(evaluation_df: pd.DataFrame, trained_models: dict):
    """
    Selecciona el mejor modelo según el R² más alto.
    """
    best_model_name = evaluation_df.iloc[0]["Modelo"]
    best_model = trained_models[best_model_name]

    logger = logging.getLogger(__name__)
    logger.info(f"🏆 Mejor modelo seleccionado: {best_model_name} con R² = {evaluation_df.iloc[0]['R2']:.3f}")

    return best_model
