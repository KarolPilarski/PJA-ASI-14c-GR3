from autogluon.tabular import TabularPredictor

def train_autogluon_model(train_data, label_column):
    predictor = TabularPredictor(label=label_column).fit(train_data)
    return predictor