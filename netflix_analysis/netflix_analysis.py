import pandas as pd
import matplotlib.pyplot as plt
#load dataset
df = pd.read_csv("netflix_titles.csv")
print(df.head())
print(df.info())
#count movie vs tv show
type_count = df["type"].value_counts()
print(type_count)
#count year distribution
release_year_count = df["release_year"].value_counts().sort_index()
print(release_year_count)
#count country distribution
country_count = df["country"].value_counts()
print(country_count.head(10))
#create bar chart of movie vs tv show
type_count.plot(kind="bar")
plt.title("Distribution of Movies vs TV series on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.savefig("type_distribution.png")
plt.show()
#create bar chart of release year distribution(after 1999)
release_year_count = release_year_count[release_year_count.index >= 2000]
release_year_count.plot(kind="bar")
plt.title("Netflix content by release year")
plt.xlabel("Year")
plt.ylabel("Number of titles")
plt.savefig("release_year_distribution.png")
plt.show()
#create bar chart of country distribution(top 10 countries)
country_count = country_count.head(10)
country_count.plot(kind="bar")
plt.xlabel("Country")
plt.ylabel("Number of titles")
plt.savefig("country_distribution.png")
plt.show()