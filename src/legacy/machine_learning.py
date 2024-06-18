from sklearn.ensemble import RandomForestRegressor


def train_model(X_train, y_train):
    print("Training model...")

    model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    return model


