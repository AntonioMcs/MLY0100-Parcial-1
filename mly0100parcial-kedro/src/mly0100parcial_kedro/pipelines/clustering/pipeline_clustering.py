from kedro.pipeline import Pipeline, node, pipeline
from .node_clustering import preprocess_data, run_kmeans


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=preprocess_data,
            inputs="diabetes_cleaned",
            outputs="diabetes_scaled",
            name="scaling_step"
        ),
        node(
            func=run_kmeans,
            inputs=dict(
                df_scaled="diabetes_scaled",
                n_clusters="params:kmeans.n_clusters"
            ),
            outputs="diabetes_clusters",
            name="kmeans_step"
        )
    ])
