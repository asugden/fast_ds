# There are variety of SQL flavors
# Postgres is common and what I usually use
# But, let's use a local database called sqlite for today

import sqlite3

# integer primary key means
# unique, not null, autoincrementing
# must not have final comma
# end with semicolon

recovery_level = '''
CREATE TABLE recovery IF NOT EXISTS {
    id INTEGER PRIMARY KEY,  
    color VARCHAR(10) NOT NULL,
    description VARCHAR(250)
};
'''

# Can you fill out timepoints such that has all of the columns that
# you're interested in, with the consideration that you might want more
# relational tables.
timepoints = '''
CREATE TABLE timepoints IF NOT EXISTS {
    id INTEGER PRIMARY KEY,
    timestamp DATETIME,
    heartrate FLOAT NOT NULL,
    recovery INTEGER REFERENCES recovery(id)
}
'''

# Let's connect to a database


def create_rel_tables(path_to_db: str, queries: list[str]):
    conn = sqlite3.connect(path_to_db)
    cursor = conn.cursor()
    for query in queries:
        cursor.execute(query)
    cursor.close()


# Only add name = main if in a functional file, not a script file
# if __name__ == '__main__':
# anything after name = main is run ONLY if the file that contains it
# is the one being run
create_rel_tables('data/whoop.db', queries=[recovery_level, timepoints])


# RAW SQL challenge:
# Upload the entire dataset in one operation into a raw table
# And use SQL to split the data into timepoints and recovery

# Alternative, split in python and upload separately
