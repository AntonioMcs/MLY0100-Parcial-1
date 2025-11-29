from kedro.pipeline import Pipeline

from mly0100parcial_kedro.pipelines import (
    clustering as ds_clustering,
    data_science as ds_data_science,
    diabetes as ds_diabetes,
    reporting as ds_reporting,
    unsupervised_learning as ds_unsupervised,
)


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines."""

    data_science_pipeline = ds_data_science.create_pipeline()
    reporting_pipeline = ds_reporting.create_pipeline()
    diabetes_pipeline = ds_diabetes.create_pipeline()
    clustering_pipeline = ds_clustering.create_pipeline()
    unsupervised_pipeline = ds_unsupervised.create_pipeline()

    return {
        "data_science": data_science_pipeline,
        "reporting": reporting_pipeline,
        "diabetes": diabetes_pipeline,
        "clustering": clustering_pipeline,
        "unsupervised_learning": unsupervised_pipeline,
        "__default__": diabetes_pipeline,
    }
