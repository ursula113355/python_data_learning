## SQL vs Pandas
SQL: SELECT * FROM table
Pandas: df

SQL: SELECT name FROM table
Pandas: df["name"]

SQL: SELECT * FROM table
WHERE age = 20
Pandas: df = df[df["age"] == 20]

SQL: SELECT * FROM table
LIMIT 10
Pandas: df.head(10)

SQL:
SELECT city,COUNT(*)
FROM users
GROUP BY city;

Pandas:
df.groupby("city").size()

SQL:
SELECT city, AVG(salary)
FROM users
GROUP BY city

Pandas:
df.groupby("city")["salary"].mean()

## What I learned today
1. SELECT FROM: chose column
2. WHERE: filter row
3. DISTINCT: exclude same content
4. ORDER BY: ascending or descending
5. LIMIT: only show how many rows
6. OFFSET: exclude the first several rows
7. INNER JOIN ON:connect with other tables which has the same key

- sql's function is similar to pandas,but it works directly with databases

## What sql is good at
1. SQL is good at filtering grouping and summarizing data directly from database
2. Compare to Pandas, SQL is usually used before analysis to extract required dataset

## SQL thinking pattern
Most sql queries follow the following patterns
SELECT column
FROM table
WHERE column_condition
GROUP BY column
ORDER BY column ASC/DESC
LIMIT OFFSET