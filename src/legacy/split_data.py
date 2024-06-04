from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns


def split_data(df: pd.DataFrame, test_size: float, val_size: float, random_state: int, column: string):
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