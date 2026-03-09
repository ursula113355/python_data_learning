SELECT *
FROM users

SELECT name
FROM users

SELECT age
FROM users
WHERE age >= 20

SELECT DISTINCT name
FROM users

SELECT name,age
FROM users
ORDER BY age ASC
LIMIT 20 OFFSET 20

SELECT name, hobby
FROM users
INNER JOIN background
    ON id(in users) = id(in background)


## SQL vs Pandas
SQL: SELECT * FROM table
Pandas: df

SQL: SELECT name FROM table
Pandas: df["name"]

SQL: SELECT * FROM table
WHERE age = 20
Pandas: df=df[df["age"] = 20]

SQL: SELECT * FROM table
LIMIT 10
Pandas: df.head(10)

## Questions to practice SQL thinking
1. What are the ages of the top 10 users who spent most of the money on our platform?
2. What is the most often used platform for the users over 20?
3. Where is the most often visited place for users who live in Boston?
