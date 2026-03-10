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

## Questions to practice SQL thinking
1. What are the ages of the top 10 users who spent most of the money on our platform?
2. What is the most often used platform for the users over 20?
3. Where is the most often visited place for users who live in Boston?

## What I learned today
1. SELECT FROM: chose column
2. WHERE: filter row
3. DISTINCT: exclude same content
4. ORDER BY: ascending or descending
5. LIMIT: only show how many rows
6. OFFSET: exclude the first several rows
7. INNER JOIN ON:connect with other tables which has the same key

- sql's function is similar to pandas,but it works directly with databases
