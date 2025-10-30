from kedro.pipeline import Pipeline
from mly0100parcial_kedro.pipelines import (
    data_science as ds_data_science,
    reporting as ds_reporting,
    diabetes as ds_diabetes,
)

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines."""
    return {
        "data_science": ds_data_science.create_pipeline(),
        "reporting": ds_reporting.create_pipeline(),
        "diabetes": ds_diabetes.create_pipeline(),
        "__default__": ds_diabetes.create_pipeline(),
    }
