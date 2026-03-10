## Questions to practice SQL thinking(day_1)
1. What are the ages of the top 10 users who spent most of the money on our platform?
2. What is the most often used platform for the users over 20?
3. Where is the most often visited place for users who live in Boston?

## Questions(day_2_morning)
1. What is the average renting price of supermarket in the block?
2. Who spent most of the money in the supermarket today?
3. How many people visited the each part of the zoo today?

## Questions(day_2_afternoon)
1. What is the mostly used app?
2. Which app has the highest population of people between 20-40?
3. Which country has the least population?
    SELECT country, COUNT(*)
    FROM table
    ORDER BY population ASC
    LIMIT 1;
4. What is the average price of each regular meals of a day in our restaurant?
5. Which city owns the largest amount of people who use our app?
6. What is the average salary of people work in restaurant
    SELECT AVG(salary)
    FROM table
    WHERE workplace LIKE "restaurant";
7. What are the mostly visited parks of people from each city?
8. What is the time that has most of the people under 18 visited our shopping mall?
9.  What is the mostly used apps for each generation?
    SELECT app_name, COUNT(*), generation
    FROM table
    GROUP BY generation,app_name
    ORDER BY COUNT(*) DESC;
10. How many employees does each restaurant has?