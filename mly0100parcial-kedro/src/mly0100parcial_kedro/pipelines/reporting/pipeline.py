from kedro.pipeline import Pipeline, node

from .nodes import (
    plot_target_distribution,
    plot_correlation_matrix,
    plot_bmi_vs_glucose,
)


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=plot_target_distribution,
                inputs="model_input_table",
                outputs="target_distribution_plot",
                name="plot_target_distribution_node",
            ),
            node(
                func=plot_correlation_matrix,
                inputs=["model_input_table", "params:model_options"],
                outputs="correlation_matrix_plot",
                name="plot_correlation_matrix_node",
            ),
            node(
                func=plot_bmi_vs_glucose,
                inputs="model_input_table",
                outputs="bmi_glucose_scatter_plot",
                name="plot_bmi_vs_glucose_node",
            ),
        ]
    )
