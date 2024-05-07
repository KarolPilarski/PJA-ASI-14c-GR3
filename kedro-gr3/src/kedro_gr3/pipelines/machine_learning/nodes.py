from typing import Tuple
from sklearn.model_selection import train_test_split
import pandas as pd
import string
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def split_data(df: pd.DataFrame, test_size: float, val_size: float, random_state: int, column: string) -> Tuple[
    pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.Series, pd.Series, pd.Series]:
    print("Splitting data into train and test sets...")

    X_train, X_test, y_train, y_test = train_test_split(
        df.drop(column, axis=1),
        df[column],
        test_size=test_size,
        random_state=random_state
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X_train,
        y_train,
        test_size=val_size,
        random_state=random_state
    )

    return X_train, X_test, X_val, y_train, y_test, y_val


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestRegressor:
    print("Training model...")

    model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model: RandomForestRegressor, X_test: pd.DataFrame, y_test: pd.Series) -> Tuple[float, float, float]:
    print("Evaluating model...")

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print('Mean Absolute Error:', mae)
    print('Mean Squared Error:', mse)
    print('R2 Score:', r2)

    return mae, mse, r2
