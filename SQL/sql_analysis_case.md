## 问题1
How many users are in each city?

SELECT city, COUNT(*)
FROM users
GROUP BY city;

## 问题2
What is the average salary in each city?

SELECT AVG(salary), city
FROM users
GROUP BY city;

## 问题3
Which city has the highest average salary?

SELECT city, AVG(salary)
FROM users
GROUP BY city
ORDER BY AVG(salary) ASC
LIMIT 1;

## 问题4
What are the top 5 highest salaries?

SELECT *
FROM users
ORDER BY salary ASC
LIMIT 5;

## 问题5
How many users use each app?

SELECT COUNT(*), app
FROM users
GROUP BY app;

