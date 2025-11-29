"""Pipeline de aprendizaje no supervisado para el dataset de diabetes."""

from kedro.pipeline import Pipeline, node

from .nodes import (
    cluster_patients,
    detect_anomalies,
    prepare_unsupervised_data,
    run_pca,
    scale_features,
)


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=prepare_unsupervised_data,
                inputs=["diabetes_cleaned", "params:unsupervised_learning"],
                outputs="diabetes_unsupervised_features",
                name="prepare_unsupervised_data_node",
            ),
            node(
                func=scale_features,
                inputs="diabetes_unsupervised_features",
                outputs="diabetes_unsupervised_scaled",
                name="scale_unsupervised_features_node",
            ),
            node(
                func=run_pca,
                inputs=["diabetes_unsupervised_scaled", "params:unsupervised_learning"],
                outputs=["diabetes_pca_components", "diabetes_pca_variance"],
                name="run_pca_unsupervised_node",
            ),
            node(
                func=cluster_patients,
                inputs=["diabetes_pca_components", "params:unsupervised_learning"],
                outputs=["diabetes_cluster_assignments", "diabetes_cluster_centroids"],
                name="cluster_patients_node",
            ),
            node(
                func=detect_anomalies,
                inputs=["diabetes_unsupervised_scaled", "params:unsupervised_learning"],
                outputs="diabetes_anomaly_scores",
                name="detect_anomalies_node",
            ),
        ]
    )

