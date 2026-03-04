import pandas as pd

df = pd.read_csv('/Users/mka/Desktop/personal projects/Youtube/YT_Stats/Feb26/Table data.csv')
df = df.dropna()

print("initial data")
print(df)
print("head of data")
print(df.head())
print("info of data")
print(df.shape)
print(df.columns)
print(df.info)
print(df.describe())

print("data sorted by views")
print(df.sort_values("Views", ascending=False).head(10))

