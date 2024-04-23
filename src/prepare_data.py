from sklearn.preprocessing import LabelEncoder
import pandas as pd
import string


def prepare_data(df: pd.DataFrame):
    print('Preparing data...')

    df = remove_na(df, 'Price per kilogram')
    df = remove_invalid_entries(df, 'Price per kilogram')
    df = encode(df)

    return df


def remove_na(df: pd.DataFrame, column):
    print("\nColumn \t\tnull count")
    print("--------------------------")
    print(df.isnull().sum())

    return df.dropna(subset=[column])


def remove_invalid_entries(df: pd.DataFrame, column: string):
    print(df[df[column] <= 0])

    df.drop(df.index[df[column] == 0], inplace=True)

    return df


def encode(df: pd.DataFrame):
    encoder = LabelEncoder()
    df['State'] = encoder.fit_transform(df['State'])
    df['City'] = encoder.fit_transform(df['City'])
    df['Store type'] = encoder.fit_transform(df['Store type'])

    return df
