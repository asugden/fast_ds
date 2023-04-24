import os

import numpy as np
import pandas as pd
import sklearn
import xgboost as xgb


class ModelTrainer:
    def __init__(self):
        # Double-underscore or "dunder" methods are defined by python
        # A method is just a function within a class
        # It's just a style that you wouldn't do naturally
        # Don't use dunder method names without knowing why
        # Init is always run first.
        self.model = None

    def train(self, features, labels, params: dict = {}, skip_frac: float = 0.2):
        # features is the same as matrix X, but already is the correct columns
        # labels is the same as y, but the correct Series/column
        X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
            features, labels, train_size=(1-skip_frac))

        self.model = xgb.XGBClassifier(params)
        self.model.fit(X_train, y_train)

        # Explicitly: it's a bit weird that we're splitting here and returning
        # test data, but this shows just one way you could choose to do it.
        return X_test, y_test

    def predict(self):
        # We can use self.model here without passing it in
        pass

    def assess(self):
        pass

    def save(self, path: str):
        # We can add in code to add the date to the filename
        path, filename = os.path.split(path)
        filename = 'date today' + filename
        self.model.save(os.path.join(path, filename))

    def load(self, path: str):
        pass

    # def __eq__(self, other):
    #     # Determine whether two ModelTrainers are equal
    #     return self.model_type == other.model_type

    # def __gt__(self, other):
