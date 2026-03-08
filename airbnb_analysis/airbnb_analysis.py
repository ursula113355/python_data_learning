import pandas as pd
df = pd.read_csv("listings.csv")
print(df.head())
print(df.info())#can use room_type, price
print(df["price"].head(10))
print(df["price"].dtype)
df["price"] = df["price"].replace("[$,]", "", regex=True)
df["price"] = df["price"].astype(float)
print(df["price"].describe())