-- SQL Social-Network Query Exercises (core set)

-- 1 Find the names of all students who are friends with someone named Gabriel.

SELECT h1.name
FROM highschooler h1
JOIN highschooler h2
JOIN friend f
ON h1.ID = f.ID1
AND h2.ID = f.ID2
AND h2.name == 'Gabriel'


-- 2. For every student who likes someone 2 or more grades younger than themselves, return that student's name and grade, and the name and grade of the student they like. 

SELECT h1.name, h1.grade, h2.name, h2.grade
FROM Highschooler h1
JOIN Highschooler h2
JOIN Likes l
ON h1.ID = l.ID1
ON h2.ID = l.ID2
AND h1.grade >= h2.grade + 2


-- 3. For every pair of students who both like each other, return the name and grade of both students. Include each pair only once, with the two names in alphabetical order.

SELECT h1.name, h1.grade, h2.name, h2.grade
FROM Highschooler h1
JOIN Highschooler h2
JOIN Likes l1
JOIN Likes l2
ON h1.id = l1.id1
AND h2.id = l1.id2
AND l1.id1 = l2.id2
AND l1.id2 = l2.id1
AND h1.name < h2.name


-- 4. Find all students who do not appear in the Likes table (as a student who likes or is liked) and return their names and grades. Sort by grade, then by name within each grade.
