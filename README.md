# fast_ds

Data science at high speed

# 0. How to set up git repository

1. Go to git, press + and create new repository
2. Copy the SSH clone
3. Type `git clone <repository> fast_ds/` in terminal
4. Open up new VSCode window clicking on the directory fast_ds BUT NOT OPENING IT.
5. Make fast_ds directory within fast_ds for future imports
6. Create **init**.py file in EVERY subfolder (it can be empty)
7. If you use conda, you should be fine. you can always make a conda environment if you would like. If you use pip, then set up a virtual environment using `python -m venv venv/`. Then activate it using `source venv/bin/activate`
8. Add in a `.vscode` directory, and inside put the launch.json and settings.json. Copy everything, but you can skip the default interpreter path, which is specific to my computer.

# 1. Create models

Structure in five functions for reuse

# 2. Groupby-apply + Github

1. Create a new repository and add your model creation code
2. Create categorical variables in your data
3. Use groupby-apply in 3 ways: Series vs. DataFrame, as a "reduce". In the case of map, you can just run groupby().apply(np.mean)
   - https://realpython.com/pandas-groupby/
   - https://www.youtube.com/watch?v=qy0fDqoMJx8
4. Test out the idea of a class

## SQL

Interact with SQL in three ways:

1. Using Beekeeper Studio https://github.com/beekeeper-studio/beekeeper-studio/releases/tag/v3.9.9 and directly calling SQL
2. Calling SQL queries using sqlite connections and cursors
3. Using Pandas via SQLAlchemy

4. Take an existing dataset, fda_data.csv, and separate it into a relational model of companies (applicant in the data) and drugs (both proper_name and proprietary_name).

- Can you do it both via Python and SQL?
- Which approach is better for a large-scale database?

### Directly calling SQL

For Sqlite, use `INSERT OR IGNORE INTO` rather than `ON CONFLICT IGNORE` or `ON CONFLICT DO NOTHING`

Also can use `table_id INTEGER REFERENCES table(id)`

### Using SQLAlchemy/Pandas

Note that Pandas and SQLAlchemy have different versions, so sometimes you cannot directly use the engine.

Rather than:

```
df.to_sql('raw', engine, index=False, if_exists='append')
```

Use:

```
with engine.connect() as conn:
   df.to_sql('raw', conn, index=False, if_exists='append')
```

## Entity resolution/deduplication

Strings can overlap in the following ways (amongst many):

1. One string is a substring. If Janssen is there, and Janssen Pharmaceuticals, that's a comfortable overlap.
2. Fraction of words that overlap
3. Number of changes to get from one string to another (Levenshtein distance and my preferred one, Jarowinkler similarity/distance) `conda install jarowinkler`
4. Consider `fuzzywuzzy`
5. XGBoost?
6. How do we generate features and labels using only a list of companies
7. Consider sets

### Output

A bridge table, which connects one id to another. It's just a list of pairs of ids.

Connect one id from a company table to another id.

### Creating labels

1. Manually get a set of easy matches and nonmatches
   - Can even make them up (10-30 examples)
   - Three columns: name1, name2, ismatch
2. Calculate features from the names in 1
3. Train an xgboost model from the output of 2
4. Run the xgboost model on a big batch of data (100?, 1000?, 10_000?), predicting proba
5. Sample 3 examples from each chunk 0-0.1, 0.1-0.2, 0.2-0.3...
   - This is making it so that we actually find the hardest examples, but keep a few easy ones
6. Hand-check the output of 5 to create the final xgboost training set
7. Use the output of 6 to create the final xgboost entity resolution model
8. Run the xgboost model on everything, saving ismatch where it is true, and save the ids of the two names that did match
9. Bridge table is the one place without primary key id, because it's not necessary, but it instead references two other tables to describe pairs
