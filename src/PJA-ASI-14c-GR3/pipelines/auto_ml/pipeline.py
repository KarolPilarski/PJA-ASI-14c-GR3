from kedro.pipeline import node, Pipeline

from .nodes import train_autogluon_model

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=train_autogluon_model,
                inputs=["encoded_data", "params:predicted_column"],
                outputs="trained_autogluon_model",
                name="train_autogluon_model_node",
            ),
        ]
    )