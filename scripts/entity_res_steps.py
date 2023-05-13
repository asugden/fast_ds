import pandas as pd
import sqlalchemy

# We have to split into to types of data:
# List (dataframe) of names
# List (dataframe) of PAIRS of names


def get_rows_from_db(path: str) -> pd.DataFrame:
    engine = sqlalchemy.engine(path)
    df = pd.read_sql('SELECT id, applicant_name...', engine)
    return df


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
    return pd.DataFrame(pairs, columns=['id1', 'name1', 'id2', 'name2'])


def pairs_to_features(df: pd.DataFrame) -> pd.DataFrame:
    """Convert pairs of names into features representing how similar
    the names are

    Args:
        df (pd.DataFrame): pairs of names

    Returns:
        pd.DataFrame: features
    """
    # A lambda function is a temporary function
    df['set_dist'] = df.apply(
        lambda x: set_overlap(x['name1'], x['name2']), axis=1)
    # Add any other distance features you might want here
    # Could consider jarowinkler, levenshtein (which is very smiilar to jw)
    # Fasttext (in the future but not yet)
