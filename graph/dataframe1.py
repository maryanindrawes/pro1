import pandas as pd

df = pd.read_csv('car data.csv')
print(df.columns)
print(df.head())
print(df["Car_Name"].head())
print(df.tail())
print(df.loc[0])
dic = {"colum_1 ": [10, 20, 300], "colum_2": [30, 10, 100]}
df2 = pd.DataFrame(dic)
print(df2.head(2))
print(df.shape)
