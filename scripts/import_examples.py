import pandas as pd

from fast_ds import functional_xgb_model_creator as func
from fast_ds import model_pipeline

# Option 1 is running this as a script
df = func.read_data('data/boston_house_prices.csv')
model = func.train_model(df)

# Option 2 is creating a pipeline function that calls other functions
# in our library
model = model_pipeline.train_xgb_model('data/boston_house_prices.csv')

# Check our data
df = pd.read_csv('data/boston_house_prices.csv', skiprows=1)
print(df.columns)
print(df.describe())
