import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("car data.csv")
df.info()
# print(df["fuel_Type"].head())
print(df.describe())

df["Selling_Price"].plot()
# df["Year"].plot(kind='scatter')
df["Year"].hist()
df.plot.scatter(x="Year", y="Selling_Price")
plt.show()

