from typing import Tuple
from sklearn.model_selection import train_test_split
import pandas as pd
import string
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import wandb
import numpy as np
import matplotlib.pyplot as plt

def split_data(df: pd.DataFrame, split_params: dict, random_state: int, predicted_column: string) -> Tuple[
    pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.Series, pd.Series, pd.Series]:
    print("Splitting data into train and test sets...")

    X_train, X_test, y_train, y_test = train_test_split(
        df.drop(predicted_column, axis=1),
        df[predicted_column],
        test_size = split_params["test_size"],
        random_state = random_state
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X_train,
        y_train,
        test_size = split_params["val_size"],
        random_state = random_state
    )

    return X_train, X_test, X_val, y_train, y_test, y_val


def train_model(X_train: pd.DataFrame, y_train: pd.Series, train_params: dict, random_state: int, config_params: dict) -> RandomForestRegressor:
    print("Training model...")

    wandb.init(
        project = "tortilla-prices",

        config={
            "random_state": config_params["random_state"],
            "test_size": config_params["split_params"]["test_size"],
            "val_size": config_params["split_params"]["val_size"],
            "n_estimators" : config_params["train_params"]["n_estimators"],
            "max_depth": config_params["train_params"]["max_depth"]
        }
    )

    model = RandomForestRegressor(n_estimators = train_params["n_estimators"], max_depth = train_params["max_depth"], random_state = random_state)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model: RandomForestRegressor, X_test: pd.DataFrame, y_test: pd.Series) -> Tuple[float, float, float]:
    print("Evaluating model...")

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    wandb.log({"mae": mae, "mse": mse, "r2": r2})

    print('Mean Absolute Error:', mae)
    print('Mean Squared Error:', mse)
    print('R2 Score:', r2)

    print('\nFeature importances', model.feature_importances_, '\n')
    for name, importance in zip(X_test.columns.values, model.feature_importances_):
        print(name, "=", importance)
    
    features = X_test.columns.values
    importances = model.feature_importances_
    indices = np.argsort(importances)

    plt.title('Feature Importances')
    plt.barh(range(len(indices)), importances[indices], color='g', align='center')
    plt.yticks(range(len(indices)), [features[i] for i in indices])
    plt.xlabel('Relative Importance')
    plt.show()

    wandb.finish()

    return mae, mse, r2