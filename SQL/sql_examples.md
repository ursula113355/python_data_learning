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
