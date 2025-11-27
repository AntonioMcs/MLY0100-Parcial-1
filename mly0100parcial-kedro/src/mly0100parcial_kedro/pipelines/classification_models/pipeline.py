from kedro.pipeline import Pipeline, node

from .nodes import split_data, train_models, evaluate_models, select_best_model


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=split_data,
                inputs=["model_input_table", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_models,
                inputs=["X_train", "y_train"],
                outputs="trained_models",
                name="train_models_node",
            ),
            node(
                func=evaluate_models,
                inputs=["trained_models", "X_test", "y_test"],
                outputs="evaluation_results",
                name="evaluate_models_node",
            ),
            node(
                func=select_best_model,
                inputs=["evaluation_results", "trained_models"],
                outputs=["best_model", "evaluation_results_with_best"],
                name="select_best_model_node",
            ),
        ]
    )
