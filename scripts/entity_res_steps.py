import pandas as pd

# We have to split into to types of data:
# List (dataframe) of names
# List (dataframe) of PAIRS of names


def rows_to_pairs(df: pd.DataFrame) -> pd.DataFrame:
    """Takes in raw data and converts it into pairs of entries
    for comparison

    Args:
        df (pd.DataFrame): raw list of rows

    Returns:
        pd.DataFrame: set of pairs

    """
    pairs = []
    for i, row1 in df.iterrows():
        # An underscore is a variable that exists
        # but will never be used again
        for _, row2 in df.iloc[i+1:].iterrows():
            pairs.append([row1['id'], row1['applicant_name'],
                         row2['id'], row2['applicant_name']])
    return pd.DataFrame(pairs, columns=['name1', 'name2'])
