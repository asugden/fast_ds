import numpy as np
import pandas as pd


def select_bins(df: pd.DataFrame, 
                col: str,
                n_samples: int, 
                bin_width: float = 0.1) -> pd.DataFrame:
    """Take a dataframe and split one column into bins
    and sample from them

    Args:
        df (pd.DataFrame): input dataframe
        col (str): the name of the dataframe column
        n_samples (int): number of samples per bin
        bin_width (float, optional): size of the bin. 
            Defaults to 0.1.

    Returns:
        pd.DataFrame: the set of samples
    """
    out = []
    bins = np.array(range(0, 1, bin_width))
    for binmin in bins:
        # Fencepost problem
        binmax = binmin + bin_width
        subdf = df.loc[df[col] >= binmin & df[col] < binmax]
        out.append(subdf.sample(n_samples, replace=False))
    return pd.concat(out)
    