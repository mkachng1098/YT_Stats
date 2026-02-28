import pandas as pd
from pandas import read_csv

df = pd.read_csv('/Users/mka/Desktop/personal projects/Youtube/YT_Stats/Feb26/Table data.csv')

print(df.head())
df = df.dropna()
df.duplicated().sum()
print(df)