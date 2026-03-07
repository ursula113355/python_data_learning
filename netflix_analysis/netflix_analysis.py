import pandas as pd
df = pd.read_csv("netflix_titles.csv")
print(df.head())
print(df.info())
type_count = df["type"].value_counts()
print(type_count)