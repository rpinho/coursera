-- SQL Movie-Rating Query Exercises (core set)

-- 1. Find the titles of all movies directed by Steven Spielberg.

SELECT title
FROM movie
WHERE director = "Steven Spielberg"


-- 2. Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order.

SELECT DISTINCT year
FROM movie m
JOIN rating r
ON m.mID = r.mID
WHERE stars > 3
ORDER BY year ASC;


-- 3. Find the titles of all movies that have no ratings.

SELECT title
FROM movie m
LEFT OUTER JOIN rating r
ON m.mID = r.mID
WHERE r.mID is NULL


-- 4. Some reviewers didn't provide a date with their rating. Find the names of all reviewers who have ratings with a NULL value for the date.

SELECT name
FROM Reviewer rv
JOIN Rating rt
ON rv.rID = rt.rID
AND ratingDate IS NULL


-- 5. Write a query to return the ratings data in a more readable format: reviewer name, movie title, stars, and ratingDate. Also, sort the data, first by reviewer name, then by movie title, and lastly by number of stars. 

SELECT name, title, stars, ratingdate
FROM movie m
JOIN reviewer rv
JOIN rating rt
ON m.mID = rt.mID
AND rv.rID = rt.rID
ORDER BY name, title, stars


-- 6.For all cases where the same reviewer rated the same movie twice and gave it a higher rating the second time, return the reviewer's name and the title of the movie.  

SELECT name, title
FROM Movie m
JOIN Reviewer rv
JOIN rating rt1
JOIN rating rt2
ON m.mID = rt1.mID
AND rt1.mID = rt2.mID
AND rt1.rID = rt2.rID
AND rv.rID = rt1.rID
AND rt2.stars > rt1.stars
AND rt2.ratingDate > rt1.ratingDate


-- 7. For each movie that has at least one rating, find the highest number of stars that movie received. Return the movie title and number of stars. Sort by movie title. 

SELECT title, MAX(stars)
FROM Movie m
JOIN Rating r
ON m.mID = r.mID
GROUP BY title


-- 8. For each movie, return the title and the 'rating spread', that is, the difference between highest and lowest ratings given to that movie. Sort by rating spread from highest to lowest, then by movie title

SELECT title, (max(stars) - min(stars)) as spread
FROM movie join rating
ON movie.mid = rating.mid
GROUP BY rating.mid
ORDER BY spread DESC, title ASC;


-- 9. Find the difference between the average rating of movies released before 1980 and the average rating of movies released after 1980. (Make sure to calculate the average rating for each movie, then the average of those averages for movies before 1980 and movies after. Don't just calculate the overall average rating before and after 1980.)

SELECT avg(T1.stars) - avg(T2.stars)
FROM
    (SELECT m.title, AVG(stars) stars
    FROM movie m
    JOIN rating r
    ON m.mID = r.mID
    GROUP BY r.mID
    HAVING year < 1980) T1
    JOIN
    (SELECT m.title, AVG(stars) stars
    FROM movie m
    JOIN rating r
    ON m.mID = r.mID
    GROUP BY r.mID
    HAVING year > 1980) T2
