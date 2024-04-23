from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns


def split_data(df: pd.DataFrame, test_size, random_state):
    print("Splitting data into train and test sets...")

    X_train, X_test, y_train, y_test = train_test_split(df.drop('Price per kilogram', axis=1), df['Price per kilogram'],
                                                        test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

    # dodać też splita na valid