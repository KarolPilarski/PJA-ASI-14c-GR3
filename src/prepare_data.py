from sklearn.preprocessing import LabelEncoder

def prepare_data(df):
    print('Preparing data...')

    df = remove_na(df, 'Price per kilogram')
    df = remove_invalid_entries(df, 'Price per kilogram')
    df = encode(df)

    return df


def remove_na(df, column):
    print("\nColumn \t\tnull count")
    print("--------------------------")
    print(df.isnull().sum())

    return df.dropna(subset=[column])


def remove_invalid_entries(df, column):
    print(df[df[column] <= 0])

    df.drop(df.index[df[column] == 0], inplace=True)

    return df


def encode(df):
    encoder = LabelEncoder()
    df['State'] = encoder.fit_transform(df['State'])
    df['City'] = encoder.fit_transform(df['City'])
    df['Store type'] = encoder.fit_transform(df['Store type'])

    return df
