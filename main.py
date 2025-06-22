import pandas as pd
import numpy as np
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


try:
    df_raw = pd.read_csv('afa2e701598d20110228.csv', sep=';')
    print(df_raw.head())
    print(df_raw.info())
    print(df_raw.shape())
    print(df_raw.describe().T)


except FileNotFoundError:
    print("Error: 'afa2e701598d20110228.csv' not found.")

missing_val = df_raw.isnull().sum()
missing_per = (missing_val / len(df_raw)) * 100
print("\nMissing Values : \n", missing_val)
print("\nMissing Value percentage : \n", missing_per)

df_raw['date'] = pd.to_datetime(df_raw['date'], format='%d.%m.%y')
print(df_raw.info())

df_raw = df_raw.sort_values(by=('id', 'date'))
print(df_raw.head())

df_raw['year'] = df_raw['date'].dt.year
df_raw['month'] = df_raw['date'].dt.month
print(df_raw.head())




