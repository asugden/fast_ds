import xgboost as xgb

from fast_ds import functional_xgb_model_creator as func


def train_xgb_model(path: str) -> xgb.XGBClassifier:
    """Function that calls other functions and creates a pipeline

    Args:
        path (str): location of file on disk

    Returns:
        xgb.XGBClassifier: output trained classifier
    """
    df = func.read_data(path)
    model = func.train_model(df)
    return model
