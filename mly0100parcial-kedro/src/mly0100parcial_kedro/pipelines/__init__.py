from .preprocessing.pipeline import create_pipeline

def register_pipelines():
    """Register the project's pipelines."""
    return {
        "__default__": create_pipeline()
    }
