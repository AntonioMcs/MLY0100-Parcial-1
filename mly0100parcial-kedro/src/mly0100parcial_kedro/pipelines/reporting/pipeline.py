from kedro.pipeline import Pipeline, node
from .nodes import (
    load_evaluation_results,
    generate_plots,
    generate_report,
)

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=load_evaluation_results,
                inputs="diabetes_evaluation_results",
                outputs="evaluation_df",
                name="load_results"
            ),
            node(
                func=generate_plots,
                inputs=["evaluation_df"],
                outputs="diabetes_plots",
                name="generate_plots"
            ),
            node(
                func=generate_report,
                inputs=["evaluation_df", "diabetes_plots"],
                outputs=None,
                name="generate_pdf_report"
            ),
        ]
    )
