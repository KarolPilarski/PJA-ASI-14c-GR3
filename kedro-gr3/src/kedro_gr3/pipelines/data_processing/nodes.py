import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import string


def remove_na(df: pd.DataFrame, column: string) -> pd.DataFrame:
    print("\nColumn \t\tnull count")
    print("--------------------------")
    print(df.isnull().sum())

    return df.dropna(subset=[column])


def remove_invalid_entries(df: pd.DataFrame, column: string) -> pd.DataFrame:
    print(df[df[column] <= 0])

    df.drop(df.index[df[column] == 0], inplace=True)

    return df


def encode(df: pd.DataFrame) -> pd.DataFrame:
    encoder = LabelEncoder()
    df['State'] = encoder.fit_transform(df['State'])
    df['City'] = encoder.fit_transform(df['City'])
    df['Store type'] = encoder.fit_transform(df['Store type'])

    return df

def evaluate_data(df: pd.DataFrame):
    print("Evaluating data...")

    display_basic_info(df)
    display_correlation_matrix(df)
    describe_grouped(df)
    price_per_kilogram_chart(df)


def display_basic_info(df: pd.DataFrame):
    print(round(df['Price per kilogram'].describe(), 2))


def display_correlation_matrix(df: pd.DataFrame):
    numeric_df = df.select_dtypes(include=[np.number])

    corr_matrix = numeric_df.corr()

    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Macierz korelacji')
    plt.show()


def describe_grouped(df: pd.DataFrame):
    print(df["Price per kilogram"].groupby([df["Year"]]).describe())
    print(df["Price per kilogram"].groupby([df["Month"]]).describe())


def price_per_kilogram_chart(df: pd.DataFrame):
    describe = df["Price per kilogram"].groupby([df["Year"]]).describe()
    plt.subplot(title='Price per kilogram', xlim=(2007, 2024), ylabel='Mexican peso ($MXN)')
    describe['mean'].plot(kind='line')
    describe['min'].plot(kind='line')
    describe['std'].plot(kind='line')
    plt.legend(['mean', 'min', 'std'])
    plt.ylabel = 'Price per kilogram'
    plt.gca().spines[['top', 'right']].set_visible(False)
    plt.show()