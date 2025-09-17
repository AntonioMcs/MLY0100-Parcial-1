from kedro.pipeline import Pipeline, node
from .nodes import clean_data, encode_features

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=clean_data,
            inputs="raw_dataset",
            outputs="cleaned_dataset",
            name="cleaning_node"
        ),
        node(
            func=encode_features,
            inputs="cleaned_dataset",
            outputs="processed_dataset",
            name="encoding_node"
        ),
    ])
