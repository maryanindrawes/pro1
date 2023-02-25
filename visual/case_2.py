import pandas as pd

df = pd.read_csv("car data.csv")
df.info()
# df['Selling_Price_2'] = df['Selling_Price'].astype(float)
df['string'] = df['Selling_Price'].astype(str)
df.info()

df['Selling_Price_2'] = pd.to_numeric(df['string'])
df['max'] = df['Selling_Price'] * 2
print(df.head())
df.info()
