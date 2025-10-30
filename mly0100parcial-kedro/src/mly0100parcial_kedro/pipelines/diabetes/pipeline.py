from kedro.pipeline import Pipeline, node
from .nodes import (
    clean_diabetes_data,
    split_diabetes_data,
    train_diabetes_model,
    evaluate_diabetes_model
)

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=clean_diabetes_data,
            inputs="diabetes_raw",
            outputs="diabetes_cleaned",
            name="clean_diabetes_data_node"
        ),
        node(
            func=split_diabetes_data,
            inputs=["diabetes_cleaned", "params:diabetes_model_options"],
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="split_diabetes_data_node"
        ),
        node(
            func=train_diabetes_model,
            inputs=["X_train", "y_train"],
            outputs="diabetes_trained_model",
            name="train_diabetes_model_node"
        ),
        node(
            func=evaluate_diabetes_model,
            inputs=["diabetes_trained_model", "X_test", "y_test"],
            outputs="diabetes_evaluation_results",
            name="evaluate_diabetes_model_node"
        ),
    ])
