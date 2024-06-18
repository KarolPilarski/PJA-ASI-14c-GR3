from kedro.pipeline import Pipeline, node, pipeline

from .nodes import split_data, train_model, evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["encoded_data", "params:split_params", "params:random_state", "params:predicted_column"],
                outputs=["X_train", "X_test", "X_val", "y_train", "y_test", "y_val"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train", "params:train_params", "params:random_state", "parameters"],
                outputs="trained_model",
                name="train_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["trained_model", "X_test", "y_test"],
                outputs=["mae", "mse", "r2"],
                name="evaluate_model_node",
            ),
        ]
    )
