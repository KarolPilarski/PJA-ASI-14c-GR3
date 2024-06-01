from kedro.pipeline import Pipeline, node, pipeline

from .nodes import remove_na, remove_invalid_entries, encode, evaluate_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=remove_na,
                inputs=["torillas", "params:predicted_column"],
                outputs="removed_na_data",
                name="remove_na_node",
            ),
            node(
                func=remove_invalid_entries,
                inputs=["removed_na_data", "params:predicted_column"],
                outputs="invalid_entries_removed_data",
                name="remove_invalid_entries_node",
            ),
            node(
                func=encode,
                inputs="invalid_entries_removed_data",
                outputs="encoded_data",
                name="encode_node",
            ),
            node(
                func=evaluate_data,
                inputs="invalid_entries_removed_data",
                outputs=None,
                name="evaluate_data_node",
            ),
        ]
    )
