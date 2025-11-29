"""Nodos para el pipeline de aprendizaje no supervisado enfocado en diabetes."""

from __future__ import annotations

import logging
from typing import Dict, List

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


logger = logging.getLogger(__name__)


def _get_feature_list(
    df: pd.DataFrame,
    params: Dict,
) -> List[str]:
    """Obtiene la lista de columnas a utilizar o infiere columnas numéricas."""
    configured = params.get("features")
    if configured:
        available = [col for col in configured if col in df.columns]
        missing = [col for col in configured if col not in df.columns]
        if missing:
            logger.warning(
                "Las columnas %s no existen en el dataset de diabetes. "
                "Se ignorarán para el pipeline no supervisado.",
                missing,
            )
        if available:
            return available
        logger.warning(
            "Ninguna de las columnas configuradas está en el dataset. "
            "Se inferirán columnas numéricas automáticamente.",
        )

    numeric_cols = (
        df.select_dtypes(include=["number"])
        .drop(columns=["Diabetes_binary"], errors="ignore")
        .columns.tolist()
    )
    if not numeric_cols:
        raise ValueError("No se encontraron columnas numéricas para análisis no supervisado.")
    return numeric_cols


def prepare_unsupervised_data(
    diabetes_cleaned: pd.DataFrame, params: Dict
) -> pd.DataFrame:
    """Selecciona las variables numéricas para el análisis y elimina nulos."""
    feature_cols = _get_feature_list(diabetes_cleaned, params)
    features_df = diabetes_cleaned[feature_cols].copy()
    return features_df.dropna()


def scale_features(features_df: pd.DataFrame) -> pd.DataFrame:
    """Escala las variables con StandardScaler para estabilizar PCA y clustering."""
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features_df)
    return pd.DataFrame(scaled, columns=features_df.columns, index=features_df.index)


def run_pca(
    scaled_df: pd.DataFrame,
    params: Dict,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Aplica PCA y devuelve componentes + varianza explicada."""
    pca_params = params.get("pca", {})
    desired_components = pca_params.get("n_components", 2)
    max_components = min(desired_components, scaled_df.shape[1])
    if max_components < desired_components:
        logger.warning(
            "n_components=%s excede el número de columnas (%s). "
            "Se ajustará a %s.",
            desired_components,
            scaled_df.shape[1],
            max_components,
        )
    n_components = max_components or 1

    pca = PCA(n_components=n_components)
    components = pca.fit_transform(scaled_df)
    component_cols = [f"PC{i+1}" for i in range(components.shape[1])]

    components_df = pd.DataFrame(
        components, columns=component_cols, index=scaled_df.index
    )
    variance_df = pd.DataFrame(
        {
            "component": component_cols,
            "explained_variance_ratio": pca.explained_variance_ratio_,
            "explained_variance": pca.explained_variance_,
        }
    )
    return components_df, variance_df


def cluster_patients(
    pca_df: pd.DataFrame,
    params: Dict,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Agrupa a los pacientes mediante K-Means sobre los componentes principales."""
    clustering_params = params.get("clustering", {})
    n_clusters = clustering_params.get("n_clusters", 3)
    random_state = clustering_params.get("random_state", 42)

    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=random_state,
        n_init=clustering_params.get("n_init", "auto"),
    )
    labels = kmeans.fit_predict(pca_df)

    clustered_df = pca_df.copy()
    clustered_df["cluster"] = labels

    centroids_df = pd.DataFrame(
        kmeans.cluster_centers_,
        columns=pca_df.columns,
    )
    centroids_df["cluster"] = range(n_clusters)

    return clustered_df, centroids_df


def detect_anomalies(
    scaled_df: pd.DataFrame,
    params: Dict,
) -> pd.DataFrame:
    """Detecta pacientes atípicos mediante IsolationForest."""
    anomaly_params = params.get("anomalies", {})
    contamination = anomaly_params.get("contamination", 0.05)
    random_state = anomaly_params.get("random_state", 42)

    detector = IsolationForest(
        contamination=contamination,
        random_state=random_state,
    )
    detector.fit(scaled_df)
    scores = detector.decision_function(scaled_df)
    predictions = detector.predict(scaled_df)

    result = pd.DataFrame(
        {
            "anomaly_score": scores,
            "is_anomaly": (predictions == -1).astype(int),
        },
        index=scaled_df.index,
    )
    return result

