"""Project pipelines."""

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from mly0100parcial_kedro.pipelines import diabetes as ds_diabetes
from mly0100parcial_kedro.pipelines import data_science as ds_data_science
from mly0100parcial_kedro.pipelines import reporting as ds_reporting

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    return {
        "data_science": ds_data_science.create_pipeline(),
        "reporting": ds_reporting.create_pipeline(),
        "diabetes": ds_diabetes.create_pipeline(),
        "__default__": ds_diabetes.create_pipeline()
    }