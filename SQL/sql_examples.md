# lesson1 - lesson 6
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
    ON id.users = id.background

# lesson7 - lesson 11
SELECT col_1,col_2
FROM table_1
LEFT JOIN table_2
    ON id.table_1 = id.table_2
WHERE col_2 IS NOT NULL

SELECT col_1*2 AS half_col_1
FROM table

SELECT COUNT(*)
FROM table

SELECT SUM(col_1)
FROM table

SELECT AVG(col_1)
FROM table

SELECT MAX(col_1)
FROM table

SELECT MIN(col_1)
FROM table

SELECT *
FROM table
GROUP BY col_1

SELECT *
FROM table
GROUP BY col_1
HAVING col_2 = 2

# SQL data analysis example
1. 统计每个城市用户数量
SELECT COUNT(users), city
FROM table
GROUP BY city;

2. 统计每个城市的平均年龄
SELECT AVG(age)，city
FROM table
GROUP BY city;

3. 找出年龄最大的用户
SELECT MAX(age), user
FROM table;

4. 找出用户数量最多的城市
SELECT COUNT(*), city
FROM table
GROUP BY city
ORDER BY COUNT(*) DESC
LIMIT 1;

5. 统计每个平台用户数量
SELECT COUNT(*),platform
FROM users
GROUP BY platform;

# SQL vs Pandas(groupby analysis)
SQL:
SELECT city, COUNT(*)
FROM table
GROUP BY COUNT(*)

Pandas:
df.groupby("city").size()

SQL:
SELECT city, AVG(age)
FROM table
GROUP BY city

Pandas:
df.groupby("city")["age"].mean()