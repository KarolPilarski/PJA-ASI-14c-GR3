import pandas as pd


def load_dataset():
    print('Loading dataset...')

    dataset = pd.read_csv('dataset/tortilla_prices_raw.csv')

    print(dataset.head())

    return dataset
