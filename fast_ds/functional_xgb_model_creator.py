# Five functions:
# 1. read_data -- pandas
# 2. train_test_split -- sklearn (can hold out data for assessing model quality)
# 3. train_model
# 4. predict
# 5. assess

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, precision_score, f1_score
import xgboost as xgb


def read_data(path: str) -> pd.DataFrame:
    """
    Read in data from a CSV file.
    Data type specifc

    Args:
        path (str): the location of the file on your computer

    Returns:
        pd.DataFrame: the data, loaded in and possibly cleaned

    """
    df =  pd.read_csv(path)
    return df


def split_data(data: pd.DataFrame, features: list[str], labels: str, train_fraction: float = 0.7):
    """"
    Splits a DataFrame into training and testing sets.

    Args:
        data (pd.DataFrame): DataFrame that is to be split
        features (list[str]): List of column names of features to be used in model
        labels (str): Column name containing target variable 
        train_fraction (float, optional): The fraction of the data used to train the model. Defaults to 0.7.

    Returns:
        tuple: A tuple containing training and testing sets of features and labels:
            X_train (pd.DataFrame): Set of training features
            X_test (pd.DataFrame): Set of testing features
            y_train (pd.Series): Set of training labels
            y_test (pd.Series): Set of testing labels
   
     """
    y = data[labels]
    X = data[features]
    X_train, X_test, y_train, y_test = train_test_split(data[features], data[labels], train_size= train_fraction)
    
    # Solving the problem:
    # Wite a function that splits arbitrary data in a dataframe into
    # features and labels, and then splits those into training and
    # testing.
    # Independent of data type

    return X_train, X_test, y_train, y_test


def train_model(train_features: pd.DataFrame | np.ndarray, train_labels: pd.Series | np.ndarray, params: dict = None):
    """
    Trains a XGBoost Classifier on training features and labels with specific paramaters.

    Args:
        train_features (pd.DataFrame | np.ndarray): Set of training features
        train_labels (pd.Series | np.ndarray): Set of training labels
        params (dict, optional):A dictionary of parameters and their values to pass to the model. Defaults to None.

    Returns:
       xgboost.XGBClassifier: Trained XGBoost Classifier
    
    """
    xgb_model = xgb.XGBClassifier(params)
    xgb_model.fit(train_features, train_labels)
    return xgb_model
    # Train your model
    # XGBoost
    # in the case of xgboost, the tree depth is a hyperparameter
    # All of the supervised algorithms look the same
    
    
    pass



def predict(model: xgb.XGBClassifier, test_features: pd.DataFrame, threshold: float):
    """
    Perform predictions on an XGBClassifier given testing features and a specific threshold.

    Args:
        model (xgboost.XGBClassifier): Model to perform predictions on
        test_features (pd.DataFrame): Set of testing features
        threshold (float): Value to compare postive class to in order to perform predictions

    Returns:
        tuple: Tuple of two numpy arrays containing predict class labels and probabilities:
            y_pred (np.ndarray): Contains an array of predicted class labels
            y_pred_proba (np.ndarray) : Contains an array of predicted class probabilities for the postive class
   
     """
    y_pred = model.predict(test_features)
    y_pred_proba = model.predict_proba(test_features)[:,1] >= threshold
    return y_pred, y_pred_proba
    
    # returns true or false
    # predict_proba returns the probability of true, and a separate
    # column of the probability of false


def assess(model: xgb.XGBClassifier, test_features: pd.DataFrame, test_labels: pd.Series):
    """Asses the accuracy, f1-score, precision, recall, and roc-auc-score of an XGBClassifier

    Args:
        model (xgboost.XGBClassifier): Model to perform assesments on
        test_features (pd.DataFrame): Set of testing features
        test_labels (pd.Series): Set of testing labels

    Returns:
        dict: A dictionary containing the accuracy score, f1-score, precision score, recall score, and roc-auc score for the model
    """
    y_pred, y_pred_proba = predict(model, test_features)
    accuracy = accuracy_score(test_labels, y_pred)
    f1_score = f1_score(test_labels, y_pred)
    precision = precision_score(test_labels, y_pred)
    recall = recall_score(test_features, y_pred)
    roc_auc = roc_auc_score(test_features, y_pred_proba)
    return {
        'accuracy': accuracy,
        'f1': f1_score,
        'precision': precision,
        'recall': recall,
        'roc_auc': roc_auc
    }
    # Compare predicted_labels to test_labels
    # What do you want to return?
    # Accuracy, F1-score, precision, recall
    # I have to look up these four every single time
    
