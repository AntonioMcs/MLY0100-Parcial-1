from kedro.pipeline import Pipeline

from mly0100parcial_kedro.pipelines import (
    data_science as ds_data_science,
    reporting as ds_reporting,
    diabetes as ds_diabetes,
    clustering as ds_clustering,   # 👈 IMPORTANTE: importar tu nuevo pipeline
)


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines."""

    data_science_pipeline = ds_data_science.create_pipeline()
    reporting_pipeline = ds_reporting.create_pipeline()
    diabetes_pipeline = ds_diabetes.create_pipeline()
    clustering_pipeline = ds_clustering.create_pipeline()   # 👈 tu pipeline nuevo

    return {
        "data_science": data_science_pipeline,
        "reporting": reporting_pipeline,
        "diabetes": diabetes_pipeline,
        "clustering": clustering_pipeline,     # 👈 aquí lo registramos
        "__default__": diabetes_pipeline,      # Puedes cambiarlo si quieres
    }
