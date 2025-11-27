from kedro.pipeline import Pipeline, node

from .nodes import (
    add_bmi_category,
    add_age_group,
    add_risk_score,
    encode_categoricals,
    create_model_input_table,
)


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=add_bmi_category,
                inputs="diabetes_imputed",
                outputs="diabetes_with_bmi_cat",
                name="add_bmi_category_node",
            ),
            node(
                func=add_age_group,
                inputs="diabetes_with_bmi_cat",
                outputs="diabetes_with_age_group",
                name="add_age_group_node",
            ),
            node(
                func=add_risk_score,
                inputs="diabetes_with_age_group",
                outputs="diabetes_with_risk_score",
                name="add_risk_score_node",
            ),
            node(
                func=encode_categoricals,
                inputs="diabetes_with_risk_score",
                outputs="diabetes_encoded",
                name="encode_categoricals_node",
            ),
            node(
                func=create_model_input_table,
                inputs="diabetes_encoded",
                outputs="model_input_table",
                name="create_model_input_table_node",
            ),
        ]
    )
