import pandas as pd


def load_csv_dataset(file):
    print('Loading dataset...')

    dataset = pd.read_csv(file)

    return dataset
