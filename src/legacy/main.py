from load_dataset import load_csv_dataset
from prepare_data import prepare_data
from evaluate_data import evaluate_data
from split_data import split_data
from machine_learning import train_model
from evaluate_model import evaluate_model


def main():
    df = load_csv_dataset('dataset/tortilla_prices_raw.csv')

    df = prepare_data(df)

    evaluate_data(df)

    X_train, X_test, X_val, y_train, y_test, y_val = split_data(df, 0.15, 42)

    model = train_model(X_train, y_train)

    evaluate_model(model, X_test, y_test)


if __name__ == "__main__":
    main()