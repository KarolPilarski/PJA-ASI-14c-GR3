from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_model(model, X_test, y_test):
    print("Evaluating model...")

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print('Mean Absolute Error:', mae)
    print('Mean Squared Error:', mse)
    print('R2 Score:', r2)

    return mae, mse, r2