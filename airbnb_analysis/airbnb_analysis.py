import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("listings.csv")
print(df.head())
print(df.info())#can use room_type, price
print(df["price"].head(10))
print(df["price"].dtype)
df["price"] = df["price"].replace("[$,]", "", regex=True)
df["price"] = df["price"].astype(float)
print(df["price"].describe())
df = df[df["price"] < 500]
df["price"].hist(bins=50)
plt.title("Price distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()
room_price = df.groupby("room_type")["price"].mean()
room_price.plot(kind="bar")
plt.title("Average price by room type")
plt.xlabel("Room type")
plt.ylabel("Average price")
plt.show()