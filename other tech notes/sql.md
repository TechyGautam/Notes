# SQL Notes

> SQL = Structured Query Language  
> SQL is used to store, retrieve, manipulate and manage data in relational databases.

---

# 1. What is SQL?

SQL (Structured Query Language) is a language used to communicate with relational databases.

Using SQL, we can:

- Create databases
- Create tables
- Insert data
- Retrieve data
- Update data
- Delete data
- Filter data
- Sort data
- Group data
- Join multiple tables
- Perform calculations
- Manage database structure

---

# 2. What is a Database?

A database is an organized collection of data.

Example:

A college database may contain:

- Students
- Teachers
- Courses
- Marks
- Attendance

Example table:

| id | name | age | course |
|---|---|---|---|
| 1 | Tanishk | 19 | AI/ML |
| 2 | Rahul | 20 | CSE |
| 3 | Aman | 19 | AI/ML |

### Row

A row represents one complete record.

Example:

    1 | Tanishk | 19 | AI/ML

### Column

A column represents one attribute.

Example:

    name
    age
    course

---

# 3. What is a Relational Database?

A relational database stores data in tables.

A table contains:

- Rows
- Columns

Example:

    +----+---------+-----+-------+
    | id | name    | age | marks |
    +----+---------+-----+-------+
    | 1  | Tanishk | 19  | 85    |
    | 2  | Rahul   | 20  | 78    |
    | 3  | Aman    | 19  | 92    |
    +----+---------+-----+-------+

---

# 4. SQL vs Database

SQL is a language.

A database is where data is stored.

Popular relational database systems:

- MySQL
- PostgreSQL
- SQLite
- Oracle Database
- Microsoft SQL Server

---

# 5. SQL Command Categories

## DDL — Data Definition Language

Used to define database structure.

- CREATE
- ALTER
- DROP
- TRUNCATE

## DML — Data Manipulation Language

Used to modify data.

- INSERT
- UPDATE
- DELETE

## DQL — Data Query Language

Used to retrieve data.

- SELECT

## DCL — Data Control Language

Used for permissions.

- GRANT
- REVOKE

## TCL — Transaction Control Language

Used to manage transactions.

- COMMIT
- ROLLBACK
- SAVEPOINT

---

# 6. Creating a Database

    CREATE DATABASE college;

Select the database:

    USE college;

> SQLite normally does not use CREATE DATABASE or USE. A SQLite database is usually represented by a database file.

---

# 7. Creating a Table

Syntax:

    CREATE TABLE table_name (
        column1 datatype,
        column2 datatype,
        column3 datatype
    );

Example:

    CREATE TABLE students (
        id INT,
        name VARCHAR(100),
        age INT,
        marks INT
    );

---

# 8. SQL Data Types

## Numeric

- INT
- DECIMAL
- FLOAT
- DOUBLE

Example:

    age INT
    salary DECIMAL(10,2)

## String

- CHAR
- VARCHAR
- TEXT

Example:

    name VARCHAR(100)
    description TEXT

## Date and Time

- DATE
- TIME
- DATETIME
- TIMESTAMP

---

# 9. Primary Key

A Primary Key uniquely identifies every row in a table.

Example:

    CREATE TABLE students (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    );

Rules:

- Must be unique
- Cannot normally contain NULL
- A table has one primary key constraint
- A primary key can contain multiple columns (composite key)

---

# 10. INSERT

Used to add data.

    INSERT INTO students
    VALUES (1, 'Tanishk', 19);

Insert specific columns:

    INSERT INTO students (id, name, age)
    VALUES (2, 'Rahul', 20);

Insert multiple rows:

    INSERT INTO students (id, name, age)
    VALUES
    (3, 'Aman', 19),
    (4, 'Rohit', 21),
    (5, 'Priya', 20);

---

# 11. SELECT

Used to retrieve data.

    SELECT * FROM students;

`*` means all columns.

Select specific columns:

    SELECT name, age
    FROM students;

---

# 12. WHERE

Used to filter records.

    SELECT *
    FROM students
    WHERE age = 19;

Example:

    SELECT *
    FROM students
    WHERE marks > 80;

---

# 13. Comparison Operators

| Operator | Meaning |
|---|---|
| = | Equal |
| != | Not equal |
| <> | Not equal |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal |
| <= | Less than or equal |

Example:

    SELECT *
    FROM students
    WHERE marks >= 80;

---

# 14. AND

Both conditions must be true.

    SELECT *
    FROM students
    WHERE age = 19
    AND marks > 80;

---

# 15. OR

At least one condition must be true.

    SELECT *
    FROM students
    WHERE age = 19
    OR marks > 80;

---

# 16. NOT

Negates a condition.

    SELECT *
    FROM students
    WHERE NOT age = 19;

---

# 17. BETWEEN

Checks whether a value lies within a range.

    SELECT *
    FROM students
    WHERE marks BETWEEN 70 AND 90;

`BETWEEN` is generally inclusive of the boundary values.

---

# 18. IN

Used to match multiple possible values.

    SELECT *
    FROM students
    WHERE age IN (18, 19, 20);

Instead of:

    WHERE age = 18
    OR age = 19
    OR age = 20

---

# 19. LIKE

Used for pattern matching.

### Starts with A

    SELECT *
    FROM students
    WHERE name LIKE 'A%';

### Ends with n

    SELECT *
    FROM students
    WHERE name LIKE '%n';

### Contains "an"

    SELECT *
    FROM students
    WHERE name LIKE '%an%';

### `_` represents one character

    SELECT *
    FROM students
    WHERE name LIKE 'A__';

---

# 20. NULL

NULL means missing or unknown value.

NULL is NOT the same as:

- 0
- ''
- FALSE

Check NULL:

    SELECT *
    FROM students
    WHERE marks IS NULL;

Check NOT NULL:

    SELECT *
    FROM students
    WHERE marks IS NOT NULL;

Do NOT use:

    WHERE marks = NULL

Use:

    WHERE marks IS NULL

---

# 21. ORDER BY

Used to sort results.

Ascending:

    SELECT *
    FROM students
    ORDER BY marks ASC;

Descending:

    SELECT *
    FROM students
    ORDER BY marks DESC;

`ASC` is the default in many SQL systems.

---

# 22. LIMIT

Used to restrict the number of returned rows.

    SELECT *
    FROM students
    LIMIT 5;

Top 3 students:

    SELECT *
    FROM students
    ORDER BY marks DESC
    LIMIT 3;

> Syntax differs between database systems. SQL Server commonly uses TOP or OFFSET/FETCH.

---

# 23. DISTINCT

Removes duplicate values.

    SELECT DISTINCT age
    FROM students;

Example:

    SELECT DISTINCT course
    FROM students;

---

# 24. UPDATE

Used to modify existing data.

Syntax:

    UPDATE table_name
    SET column = value
    WHERE condition;

Example:

    UPDATE students
    SET marks = 90
    WHERE id = 1;

> Always be careful with UPDATE. Without WHERE, many/all rows may be updated.

---

# 25. DELETE

Used to delete rows.

    DELETE FROM students
    WHERE id = 5;

> Without WHERE, all rows can be deleted.

---

# 26. DELETE vs TRUNCATE vs DROP

## DELETE

Removes rows.

    DELETE FROM students
    WHERE id = 1;

The table remains.

## TRUNCATE

Removes all rows from a table.

    TRUNCATE TABLE students;

The table structure remains.

> SQLite does not provide a standard TRUNCATE TABLE command.

## DROP

Removes the table itself.

    DROP TABLE students;

After this, the table no longer exists.

---

# 27. ALTER TABLE

Used to modify table structure.

Add a column:

    ALTER TABLE students
    ADD email VARCHAR(100);

Other ALTER operations vary between database systems.

---

# 28. Constraints

Constraints are rules applied to table columns.

Common constraints:

- PRIMARY KEY
- FOREIGN KEY
- NOT NULL
- UNIQUE
- CHECK
- DEFAULT

---

# 29. NOT NULL

Prevents a column from containing NULL values.

    CREATE TABLE students (
        id INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    );

---

# 30. UNIQUE

Ensures values are unique.

    CREATE TABLE students (
        id INT PRIMARY KEY,
        email VARCHAR(100) UNIQUE
    );

---

# 31. DEFAULT

Provides a default value.

    CREATE TABLE students (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        country VARCHAR(50) DEFAULT 'India'
    );

---

# 32. CHECK

Used to enforce a condition.

    CREATE TABLE students (
        id INT PRIMARY KEY,
        age INT CHECK (age >= 18)
    );

---

# 33. Foreign Key

A Foreign Key creates a relationship between tables.

Students:

    student_id | name
    -----------|-------
    1          | Tanishk
    2          | Rahul

Courses:

    course_id | student_id | course
    ----------|------------|-------
    101       | 1          | AI/ML
    102       | 2          | CSE

`student_id` in courses can reference `student_id` in students.

Example:

    CREATE TABLE courses (
        course_id INT PRIMARY KEY,
        student_id INT,
        course VARCHAR(100),

        FOREIGN KEY (student_id)
        REFERENCES students(student_id)
    );

---

# 34. Aggregate Functions

Aggregate functions perform calculations on multiple rows.

Common functions:

- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()

## COUNT

    SELECT COUNT(*)
    FROM students;

## SUM

    SELECT SUM(marks)
    FROM students;

## AVG

    SELECT AVG(marks)
    FROM students;

## MIN

    SELECT MIN(marks)
    FROM students;

## MAX

    SELECT MAX(marks)
    FROM students;

---

# 35. GROUP BY

Used to group rows with the same value.

    SELECT course, COUNT(*)
    FROM students
    GROUP BY course;

Example result:

    course      count
    ----------  -----
    AI/ML       10
    CSE         15
    ECE         8

---

# 36. HAVING

Used to filter groups.

    SELECT course, COUNT(*)
    FROM students
    GROUP BY course
    HAVING COUNT(*) > 10;

### WHERE vs HAVING

| WHERE | HAVING |
|---|---|
| Filters rows | Filters groups |
| Used before GROUP BY | Used after GROUP BY |
| Usually filters individual records | Usually filters aggregate results |

---

# 37. SQL Logical Execution Order

A simplified logical order is:

    FROM
    WHERE
    GROUP BY
    HAVING
    SELECT
    DISTINCT
    ORDER BY
    LIMIT

Example:

    SELECT course, COUNT(*)
    FROM students
    WHERE marks >= 50
    GROUP BY course
    HAVING COUNT(*) > 5
    ORDER BY COUNT(*) DESC
    LIMIT 3;

---

# 38. Aliases

Aliases give temporary names to columns or tables.

## Column Alias

    SELECT
        name AS student_name,
        marks AS score
    FROM students;

## Table Alias

    SELECT s.name
    FROM students AS s;

---

# 39. SQL Functions

Common functions:

- UPPER()
- LOWER()
- LENGTH()
- ROUND()
- COALESCE()

Example:

    SELECT UPPER(name)
    FROM students;

---

# 40. CASE

CASE works like conditional logic.

    SELECT
        name,
        marks,
        CASE
            WHEN marks >= 90 THEN 'Excellent'
            WHEN marks >= 75 THEN 'Good'
            WHEN marks >= 50 THEN 'Average'
            ELSE 'Poor'
        END AS performance
    FROM students;

---

# 41. JOINS

Joins combine data from multiple tables.

Main types:

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL OUTER JOIN
- CROSS JOIN

---

# 42. INNER JOIN

Returns matching records from both tables.

    SELECT
        students.name,
        courses.course
    FROM students
    INNER JOIN courses
    ON students.id = courses.student_id;

Only matching records are returned.

---

# 43. LEFT JOIN

Returns all rows from the left table and matching rows from the right table.

    SELECT
        students.name,
        courses.course
    FROM students
    LEFT JOIN courses
    ON students.id = courses.student_id;

If a student has no course, the course columns may contain NULL.

---

# 44. RIGHT JOIN

Returns all rows from the right table and matching rows from the left table.

    SELECT
        students.name,
        courses.course
    FROM students
    RIGHT JOIN courses
    ON students.id = courses.student_id;

> RIGHT JOIN support depends on the database system/version.

---

# 45. FULL OUTER JOIN

Returns:

- Matching rows
- Unmatched rows from left table
- Unmatched rows from right table

    SELECT
        students.name,
        courses.course
    FROM students
    FULL OUTER JOIN courses
    ON students.id = courses.student_id;

> Support varies by database system.

---

# 46. CROSS JOIN

Produces every possible combination of rows.

    SELECT *
    FROM students
    CROSS JOIN courses;

If:

    students = 3 rows
    courses = 4 rows

Then:

    3 × 4 = 12 rows

---

# 47. Subquery

A query inside another query.

Example:

    SELECT *
    FROM students
    WHERE marks > (
        SELECT AVG(marks)
        FROM students
    );

This finds students whose marks are above average.

---

# 48. EXISTS

Checks whether a subquery returns at least one row.

    SELECT *
    FROM students s
    WHERE EXISTS (
        SELECT 1
        FROM courses c
        WHERE c.student_id = s.id
    );

This finds students who have at least one matching course.

---

# 49. UNION

Combines results of two SELECT queries and removes duplicates.

    SELECT name FROM students
    UNION
    SELECT name FROM teachers;

The queries must have compatible numbers and types of columns.

---

# 50. UNION ALL

Combines results but keeps duplicates.

    SELECT name FROM students
    UNION ALL
    SELECT name FROM teachers;

UNION ALL is usually faster when duplicate removal is not required.

---

# 51. Primary Key vs Foreign Key

| Primary Key | Foreign Key |
|---|---|
| Uniquely identifies a row | References a key in another table |
| Usually unique | Can contain repeated values |
| Cannot normally be NULL | May be NULL depending on constraints |
| Identifies a record | Creates relationships |

---

# 52. Normalization

Normalization is the process of organizing data to reduce unnecessary duplication and improve data integrity.

Common normal forms:

- 1NF
- 2NF
- 3NF
- BCNF

For beginner/intermediate SQL, focus mainly on:

- 1NF
- 2NF
- 3NF

---

# 53. 1NF

A table is in First Normal Form when:

- Each column contains atomic values
- There are no repeating groups

Bad:

    student_id | phone_numbers
    -----------|--------------
    1          | 9999, 8888

Better:

    student_id | phone
    -----------|------
    1          | 9999
    1          | 8888

---

# 54. 2NF

A table should:

- Be in 1NF
- Have no partial dependency on part of a composite key

This mainly matters when a table has a composite primary key.

---

# 55. 3NF

A table should:

- Be in 2NF
- Have no unnecessary transitive dependencies

The goal is to ensure non-key attributes depend on the key rather than another non-key attribute.

---

# 56. Index

An index helps the database find rows faster.

Example:

    CREATE INDEX idx_student_name
    ON students(name);

Indexes can:

- Improve search performance
- Consume storage
- Slow down INSERT/UPDATE/DELETE
- Need to be created thoughtfully

---

# 57. Transactions

A transaction is a group of operations treated as one logical unit.

Example:

    BEGIN;

    UPDATE accounts
    SET balance = balance - 500
    WHERE id = 1;

    UPDATE accounts
    SET balance = balance + 500
    WHERE id = 2;

    COMMIT;

If something goes wrong:

    ROLLBACK;

---

# 58. ACID Properties

## Atomicity

All operations happen or none happen.

## Consistency

Database remains valid before and after the transaction.

## Isolation

Concurrent transactions should not improperly interfere with each other.

## Durability

Committed changes should persist.

---

# 59. SQL Injection

SQL Injection is a security vulnerability where malicious input changes the intended SQL query.

Bad example in Python:

    query = "SELECT * FROM users WHERE username = '" + username + "'"

Never build SQL queries by directly concatenating untrusted user input.

Use parameterized queries.

SQLite example:

    cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    )

For MySQL connectors, the placeholder syntax may be `%s`.

---

# 60. SQL with Python

Python can communicate with databases using database libraries.

SQLite example:

    import sqlite3

    connection = sqlite3.connect("college.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        marks INTEGER
    )
    """)

    connection.commit()

    connection.close()

---

# 61. Important SQLite Methods

Python's sqlite3 commonly uses:

- connect()
- cursor()
- execute()
- fetchone()
- fetchall()
- commit()
- close()

Example:

    import sqlite3

    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

---

# 62. SQLite vs MySQL

| SQLite | MySQL |
|---|---|
| Lightweight | Full database server |
| Database is usually a file | Uses a database server |
| Easy for local applications | Good for client-server applications |
| Excellent for learning/projects | Common in web/backend systems |
| Minimal setup | Requires server/database setup |

### For learning

SQLite is excellent.

### For backend/web development

MySQL or PostgreSQL are important to learn.

---

# 63. Practical SQL Example

Create table:

    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INTEGER,
        course VARCHAR(50),
        marks INTEGER
    );

Insert data:

    INSERT INTO students
    (id, name, age, course, marks)
    VALUES
    (1, 'Tanishk', 19, 'AI/ML', 85),
    (2, 'Rahul', 20, 'CSE', 78),
    (3, 'Aman', 19, 'AI/ML', 92),
    (4, 'Rohit', 21, 'CSE', 65),
    (5, 'Priya', 20, 'ECE', 88);

Find all students:

    SELECT *
    FROM students;

Find AI/ML students:

    SELECT *
    FROM students
    WHERE course = 'AI/ML';

Find students scoring above 80:

    SELECT name, marks
    FROM students
    WHERE marks > 80;

Sort by marks:

    SELECT *
    FROM students
    ORDER BY marks DESC;

Find highest marks:

    SELECT MAX(marks)
    FROM students;

Find average marks:

    SELECT AVG(marks)
    FROM students;

Count students:

    SELECT COUNT(*)
    FROM students;

Count students by course:

    SELECT course, COUNT(*)
    FROM students
    GROUP BY course;

---

# 64. Important SQL Query Patterns

## Top N Records

    SELECT *
    FROM students
    ORDER BY marks DESC
    LIMIT 5;

## Records Above Average

    SELECT *
    FROM students
    WHERE marks > (
        SELECT AVG(marks)
        FROM students
    );

## Find Duplicate Values

    SELECT email, COUNT(*)
    FROM users
    GROUP BY email
    HAVING COUNT(*) > 1;

## Count Records by Category

    SELECT course, COUNT(*)
    FROM students
    GROUP BY course;

## Filter Grouped Results

    SELECT course, AVG(marks)
    FROM students
    GROUP BY course
    HAVING AVG(marks) > 75;

---

# 65. SQL Learning Roadmap

Follow this order:

    Database Basics
          ↓
    CREATE TABLE
          ↓
    INSERT
          ↓
    SELECT
          ↓
    WHERE
          ↓
    ORDER BY
          ↓
    LIMIT
          ↓
    UPDATE
          ↓
    DELETE
          ↓
    Constraints
          ↓
    Aggregate Functions
          ↓
    GROUP BY
          ↓
    HAVING
          ↓
    JOINs
          ↓
    Subqueries
          ↓
    CASE
          ↓
    UNION
          ↓
    Indexes
          ↓
    Transactions
          ↓
    Normalization
          ↓
    SQL + Python
          ↓
    Real Projects

---

# 66. Practice Projects

## Project 1 — Student Management System

Features:

- Add student
- Delete student
- Update student
- Search student
- Display all students

Tech:

- Python
- SQLite

---

## Project 2 — Expense Tracker

Tables:

- expenses
- categories

Features:

- Add expense
- Delete expense
- Monthly expenses
- Category-wise expenses
- Total spending

---

## Project 3 — Login System

Table:

- users

Fields:

- id
- username
- email
- password_hash
- created_at

Features:

- Register
- Login
- User validation
- Database storage

> Store passwords using secure password hashing rather than plain text.

---

## Project 4 — Library Management System

Tables:

- students
- books
- borrow_records

Practice:

- PRIMARY KEY
- FOREIGN KEY
- JOIN
- GROUP BY
- SUBQUERY

---

# 67. SQL Interview Topics

Before an internship/job, understand:

- Primary Key
- Foreign Key
- Constraints
- NULL
- WHERE
- GROUP BY
- HAVING
- ORDER BY
- Aggregate Functions
- JOINs
- Subqueries
- UNION vs UNION ALL
- DELETE vs TRUNCATE vs DROP
- Indexes
- Normalization
- Transactions
- ACID
- SQL Injection
- Query optimization basics

---

# 68. Most Important SQL Commands

    CREATE DATABASE
    CREATE TABLE
    ALTER TABLE
    DROP TABLE

    INSERT INTO

    SELECT
    WHERE
    DISTINCT
    ORDER BY
    LIMIT

    UPDATE
    DELETE

    GROUP BY
    HAVING

    JOIN
    INNER JOIN
    LEFT JOIN
    RIGHT JOIN
    FULL OUTER JOIN

    UNION
    UNION ALL

    CASE

    CREATE INDEX

    COMMIT
    ROLLBACK

---

# 69. How to Actually Learn SQL

Don't learn SQL by only reading queries.

Use this cycle:

    Learn concept
          ↓
    Write query yourself
          ↓
    Run query
          ↓
    Break the query intentionally
          ↓
    Understand the error
          ↓
    Solve 5–10 problems
          ↓
    Use it in a project

---

# 70. Final Goal

After completing these notes, you should be able to:

- Design basic relational databases
- Create tables
- Insert and modify data
- Write complex SELECT queries
- Filter and sort data
- Group data
- Use aggregate functions
- Join multiple tables
- Write subqueries
- Understand database relationships
- Use SQL from Python
- Build database-backed projects
- Answer common SQL interview questions

---

# ⭐ Next Level SQL

After completing the above topics, learn:

1. CTE — Common Table Expressions
2. Window Functions
3. ROW_NUMBER()
4. RANK()
5. DENSE_RANK()
6. PARTITION BY
7. Advanced JOIN problems
8. Query Optimization
9. Index Optimization
10. Real-world SQL interview problems