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