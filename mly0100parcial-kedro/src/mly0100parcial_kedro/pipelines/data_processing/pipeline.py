from kedro.pipeline import Pipeline, node
from .nodes import clean_diabetes_data, impute_diabetes_data


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=clean_diabetes_data,
                inputs="diabetes_raw",
                outputs="diabetes_clean",
                name="clean_diabetes_data_node",
            ),
            node(
                func=impute_diabetes_data,
                inputs="diabetes_clean",
                outputs="diabetes_imputed",
                name="impute_diabetes_data_node",
            ),
        ]
    )
