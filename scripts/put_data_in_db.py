import pandas as pd
import sqlalchemy

# You'll have to install sqlalchemy
# conda install -c anaconda sqlalchemy


# Engine is a connection + translation to a db
# Looks just like http://
# We're specifying the "protocol" or language being spoken
# 3 slashes is relative path
# 4 slashes is absolute path (e.g. sqlite:////Users/arthur/data/whoop.db)
engine = sqlalchemy.create_engine('sqlite:///data/whoop.db')

# Load in all data
df = pd.read_csv('data/clean_whoop.csv')

df.to_sql('raw', engine, index=False, if_exists='replace')
# If you're adding to an existig table, you must use
# df.to_sql('raw', engine, index=False, if_exists='append')

# For challenge 1, you can use cursors OR beekeeper studio to run
query = '''
INSERT INTO recovery (color)
SELECT recovery_level_cat 
FROM raw
'''
# This will fail, unless you do one of two things:
# 1. SELECT DISTINCT
# 2. ON CONFLICT DO NOTHING


query2 = '''
INSERT INTO timepoints (timepoint, heartrate, recovery_id)
SELECT timepoint, heartrate, recovery_level_cat
FROM raw
JOIN recovery AS rec
    ON rec.color = raw.recovery_level_cat
'''
