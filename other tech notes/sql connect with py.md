# MySQL + Python Complete Notes

> These notes cover how to connect a Python application with a real MySQL database server using MySQL Connector/Python.

---

# 1. What is MySQL?

MySQL is a relational database management system (RDBMS).

It stores data in:

    Database
       ↓
    Tables
       ↓
    Rows + Columns

Example:

    Database: college

    students
    ┌────┬─────────┬─────┬───────┐
    │ id │ name    │ age │ marks │
    ├────┼─────────┼─────┼───────┤
    │ 1  │ Tanishk │ 19  │ 85    │
    │ 2  │ Rahul   │ 20  │ 78    │
    │ 3  │ Aman    │ 19  │ 92    │
    └────┴─────────┴─────┴───────┘

---

# 2. MySQL vs SQLite

MySQL is a server-based database.

SQLite is a file-based database.

MySQL:

    Python Application
          ↓
    MySQL Connector
          ↓
    MySQL Server
          ↓
    Database
          ↓
    Tables

SQLite:

    Python
       ↓
    SQLite Library
       ↓
    database.db

For real backend applications with multiple users, MySQL is commonly used.

---

# 3. What Do We Need?

To connect Python with MySQL, we need:

1. MySQL Server
2. Python
3. MySQL Connector/Python

---

# 4. MySQL Server

MySQL Server is the actual database server.

It stores:

- Databases
- Tables
- Records
- Users
- Permissions

Python does not directly become the database.

Python communicates with the MySQL server.

---

# 5. MySQL Client

A client is a program that allows you to interact with MySQL Server.

Examples:

- MySQL Command Line Client
- MySQL Workbench
- Other database tools

You can execute SQL queries using these tools.

---

# 6. Python MySQL Driver

Python needs a driver to communicate with MySQL.

A commonly used official connector is:

    mysql-connector-python

Install it:

    pip install mysql-connector-python

Verify installation:

    pip show mysql-connector-python

---

# 7. Import Connector

    import mysql.connector

Now Python can communicate with MySQL.

---

# 8. Basic MySQL Connection

    import mysql.connector

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="college"
    )

---

# 9. Connection Parameters

Common parameters:

    host
    user
    password
    database
    port

Example:

    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="your_password",
        database="college"
    )

---

# 10. What is localhost?

`localhost` means the MySQL server is running on your own computer.

Example:

    host="localhost"

The default MySQL port is usually:

    3306

So:

    localhost:3306

means:

    MySQL Server running locally on port 3306

---

# 11. MySQL User

MySQL requires authentication.

Example:

    user="root"

`root` is commonly created as an administrative MySQL user.

For applications, it is better to create a dedicated database user with only the permissions it needs.

---

# 12. Password

Example:

    password="mypassword"

Never hard-code real production passwords directly into your source code.

For learning, you may temporarily write it directly.

For real projects, use environment variables or a secrets manager.

---

# 13. Database Parameter

Example:

    database="college"

This tells Python which MySQL database to use after connecting.

---

# 14. Check Connection

    import mysql.connector

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="college"
    )

    if connection.is_connected():
        print("Connected to MySQL")

---

# 15. Create Database

You can create a database using SQL.

    CREATE DATABASE college;

Then select it:

    USE college;

Or create it from Python.

    import mysql.connector

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"
    )

    cursor = connection.cursor()

    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS college"
    )

    cursor.close()
    connection.close()

---

# 16. Connect Without Selecting Database

You can connect to MySQL Server without specifying a database.

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"
    )

This is useful when you want to create a database first.

---

# 17. Cursor

A cursor allows Python to execute SQL queries.

Create cursor:

    cursor = connection.cursor()

Now:

    cursor.execute()

can execute SQL commands.

---

# 18. Basic Connection Structure

    import mysql.connector

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="college"
    )

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()

---

# 19. Create Table

SQL:

    CREATE TABLE students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT,
        marks FLOAT
    );

Python:

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT,
            marks FLOAT
        )
    """)

---

# 20. MySQL Data Types

Common MySQL data types:

## Integer

    INT

Example:

    age INT

## Decimal

    DECIMAL(10,2)

Useful for values requiring exact decimal representation, such as money.

## Floating Point

    FLOAT

## String

    VARCHAR(100)

## Long Text

    TEXT

## Date

    DATE

## Date + Time

    DATETIME

## Boolean-like value

    BOOLEAN

---

# 21. Primary Key

A primary key uniquely identifies each row.

Example:

    id INT PRIMARY KEY

Common pattern:

    id INT AUTO_INCREMENT PRIMARY KEY

Example:

    id
    --
    1
    2
    3
    4

Every row gets a unique ID.

---

# 22. AUTO_INCREMENT

Example:

    id INT AUTO_INCREMENT PRIMARY KEY

When inserting:

    INSERT INTO students
    (name, age, marks)
    VALUES
    ('Tanishk', 19, 85);

You don't need to provide `id`.

MySQL automatically generates it.

---

# 23. NOT NULL

`NOT NULL` means a column cannot contain NULL.

Example:

    name VARCHAR(100) NOT NULL

---

# 24. UNIQUE

Ensures values are unique.

Example:

    email VARCHAR(150) UNIQUE

Two users cannot have the same email.

---

# 25. DEFAULT

Provides a default value.

Example:

    status VARCHAR(20)
    DEFAULT 'active'

---

# 26. Create a Better Users Table

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(150) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

This is a common type of structure for a user table.

---

# 27. INSERT Data

SQL:

    INSERT INTO students
    (name, age, marks)
    VALUES
    ('Tanishk', 19, 85);

Python:

    query = """
        INSERT INTO students
        (name, age, marks)
        VALUES (%s, %s, %s)
    """

    values = (
        "Tanishk",
        19,
        85
    )

    cursor.execute(
        query,
        values
    )

    connection.commit()

---

# 28. Why %s?

MySQL Connector/Python uses `%s` as the parameter placeholder.

Example:

    query = """
        SELECT *
        FROM students
        WHERE age = %s
    """

    cursor.execute(
        query,
        (19,)
    )

Do not confuse this with Python string formatting.

The connector handles parameter binding.

---

# 29. Parameterized Queries

Always use parameterized queries for values supplied by users.

Good:

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email = %s
        """,
        (email,)
    )

Bad:

    query = f"""
        SELECT *
        FROM users
        WHERE email = '{email}'
    """

---

# 30. Why Parameterized Queries?

They help:

- Prevent SQL injection
- Handle values safely
- Separate SQL code from data
- Avoid many quoting/escaping problems

---

# 31. Insert Multiple Rows

Use `executemany()`.

    query = """
        INSERT INTO students
        (name, age, marks)
        VALUES (%s, %s, %s)
    """

    students = [
        ("Tanishk", 19, 85),
        ("Rahul", 20, 78),
        ("Aman", 19, 92)
    ]

    cursor.executemany(
        query,
        students
    )

    connection.commit()

---

# 32. lastrowid

After inserting one row, you can often get the generated ID:

    cursor.execute(
        query,
        values
    )

    connection.commit()

    student_id = cursor.lastrowid

    print(student_id)

---

# 33. SELECT

Read data:

    cursor.execute(
        "SELECT * FROM students"
    )

---

# 34. fetchone()

Fetch one row:

    cursor.execute(
        "SELECT * FROM students"
    )

    row = cursor.fetchone()

    print(row)

Example:

    (1, 'Tanishk', 19, 85.0)

---

# 35. fetchall()

Fetch all rows:

    cursor.execute(
        "SELECT * FROM students"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

---

# 36. fetchmany()

Fetch a specific number of rows:

    cursor.execute(
        "SELECT * FROM students"
    )

    rows = cursor.fetchmany(5)

---

# 37. SELECT Specific Columns

    cursor.execute(
        """
        SELECT name, marks
        FROM students
        """
    )

    rows = cursor.fetchall()

---

# 38. WHERE

Filter records:

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE marks > %s
        """,
        (80,)
    )

---

# 39. Multiple Conditions

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE age > %s
        AND marks > %s
        """,
        (18, 80)
    )

---

# 40. OR Condition

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE course = %s
        OR course = %s
        """,
        ("AI/ML", "CSE")
    )

---

# 41. LIKE

Search text:

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE name LIKE %s
        """,
        ("Tan%",)
    )

`%` represents any sequence of characters.

Examples:

    "Tan%"
        ↓
    Starts with Tan

    "%sh"
        ↓
    Ends with sh

    "%ani%"
        ↓
    Contains ani

---

# 42. ORDER BY

Ascending:

    cursor.execute(
        """
        SELECT *
        FROM students
        ORDER BY marks ASC
        """
    )

Descending:

    cursor.execute(
        """
        SELECT *
        FROM students
        ORDER BY marks DESC
        """
    )

---

# 43. LIMIT

Get top 5 students:

    cursor.execute(
        """
        SELECT *
        FROM students
        ORDER BY marks DESC
        LIMIT 5
        """
    )

---

# 44. UPDATE

Update a record:

    query = """
        UPDATE students
        SET marks = %s
        WHERE id = %s
    """

    values = (
        95,
        1
    )

    cursor.execute(
        query,
        values
    )

    connection.commit()

---

# 45. Update Multiple Columns

    query = """
        UPDATE students
        SET age = %s,
            marks = %s
        WHERE id = %s
    """

    values = (
        20,
        90,
        1
    )

    cursor.execute(
        query,
        values
    )

    connection.commit()

---

# 46. DELETE

Delete one record:

    query = """
        DELETE FROM students
        WHERE id = %s
    """

    cursor.execute(
        query,
        (1,)
    )

    connection.commit()

Always be careful with DELETE.

---

# 47. Dangerous DELETE

This deletes every row:

    DELETE FROM students;

Never run this accidentally.

Always check your `WHERE` condition.

---

# 48. CRUD

CRUD means:

    C → Create
    R → Read
    U → Update
    D → Delete

SQL:

    INSERT → Create
    SELECT → Read
    UPDATE → Update
    DELETE → Delete

---

# 49. Complete CRUD Example

    import mysql.connector

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="college"
    )

    cursor = connection.cursor()

    # CREATE
    cursor.execute(
        """
        INSERT INTO students
        (name, age, marks)
        VALUES (%s, %s, %s)
        """,
        ("Tanishk", 19, 85)
    )

    connection.commit()

    # READ
    cursor.execute(
        "SELECT * FROM students"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # UPDATE
    cursor.execute(
        """
        UPDATE students
        SET marks = %s
        WHERE id = %s
        """,
        (90, 1)
    )

    connection.commit()

    # DELETE
    cursor.execute(
        """
        DELETE FROM students
        WHERE id = %s
        """,
        (1,)
    )

    connection.commit()

    cursor.close()
    connection.close()

---

# 50. Transactions

A transaction is a group of database operations treated as a unit.

Example:

    Start Transaction
          ↓
       INSERT
          ↓
       UPDATE
          ↓
       INSERT
          ↓
       COMMIT

If something goes wrong:

    ROLLBACK

---

# 51. commit()

Save changes:

    connection.commit()

Usually required after:

    INSERT
    UPDATE
    DELETE

---

# 52. rollback()

Undo uncommitted changes:

    connection.rollback()

Example:

    try:

        cursor.execute(
            query,
            values
        )

        connection.commit()

    except Exception:

        connection.rollback()

---

# 53. Error Handling

Use `try-except`.

    import mysql.connector

    try:

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="college"
        )

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students"
        )

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except mysql.connector.Error as error:

        print(
            "Database error:",
            error
        )

    finally:

        if "cursor" in locals():
            cursor.close()

        if "connection" in locals() and connection.is_connected():
            connection.close()

---

# 54. Common MySQL Errors

## Access denied

Possible causes:

- Wrong username
- Wrong password
- User permissions problem

---

## Unknown database

Example:

    mysql.connector.errors.ProgrammingError

Possible cause:

Database doesn't exist.

---

## Can't connect to MySQL server

Possible causes:

- MySQL Server isn't running
- Wrong host
- Wrong port
- Network/firewall problem

---

## Table doesn't exist

Possible cause:

The table hasn't been created or you're using the wrong database.

---

# 55. Check MySQL Server

From MySQL command line:

    SHOW DATABASES;

Select database:

    USE college;

Show tables:

    SHOW TABLES;

Describe table:

    DESCRIBE students;

---

# 56. Useful SQL Commands

Show databases:

    SHOW DATABASES;

Create database:

    CREATE DATABASE college;

Use database:

    USE college;

Show tables:

    SHOW TABLES;

Describe table:

    DESCRIBE students;

Delete database:

    DROP DATABASE college;

Delete table:

    DROP TABLE students;

Be very careful with:

    DROP DATABASE
    DROP TABLE

They can permanently remove data.

---

# 57. Python Database Helper Function

Instead of repeating connection code everywhere:

    import mysql.connector

    def get_connection():

        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="college"
        )

Use:

    connection = get_connection()

---

# 58. Create a Database Module

Project:

    project/
    │
    ├── main.py
    ├── database.py
    └── config.py

database.py:

    import mysql.connector

    def get_connection():

        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="college"
        )

main.py:

    from database import get_connection

    connection = get_connection()

    cursor = connection.cursor()

---

# 59. Environment Variables

Never put production database credentials directly into source code.

Bad:

    password="MyRealPassword123"

Better:

    import os

    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

Then:

    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

---

# 60. .env File

A common development approach is using a `.env` file.

Example:

    DB_HOST=localhost
    DB_USER=app_user
    DB_PASSWORD=your_password
    DB_NAME=college

Use a suitable environment-variable loader such as `python-dotenv` when needed.

Never commit `.env` to GitHub.

Add:

    .env

to:

    .gitignore

---

# 61. Dedicated Database User

For applications, avoid using the MySQL root account.

Concept:

    root
      ↓
    Administration

    app_user
      ↓
    Application

The application user should receive only the permissions it actually needs.

---

# 62. Create MySQL User

Example SQL:

    CREATE USER
    'app_user'@'localhost'
    IDENTIFIED BY 'strong_password';

Grant permissions:

    GRANT SELECT, INSERT, UPDATE, DELETE
    ON college.*
    TO 'app_user'@'localhost';

Apply changes if required by your MySQL setup:

    FLUSH PRIVILEGES;

For production, use carefully scoped permissions rather than giving unnecessary administrative access.

---

# 63. Foreign Keys

Suppose:

    students
    --------
    id
    name

    marks
    -----
    id
    student_id
    marks

Create:

    CREATE TABLE marks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT NOT NULL,
        marks FLOAT,

        FOREIGN KEY (student_id)
        REFERENCES students(id)
    );

This creates a relationship between the tables.

---

# 64. JOIN

Suppose:

students:

    id | name
    ---|-------
    1  | Tanishk
    2  | Rahul

marks:

    student_id | marks
    -----------|------
    1          | 85
    2          | 90

Query:

    SELECT
        students.name,
        marks.marks
    FROM students
    INNER JOIN marks
        ON students.id = marks.student_id;

Python:

    cursor.execute(
        """
        SELECT
            students.name,
            marks.marks
        FROM students
        INNER JOIN marks
            ON students.id = marks.student_id
        """
    )

    rows = cursor.fetchall()

---

# 65. INNER JOIN

Returns matching records from both tables.

    SELECT *
    FROM students
    INNER JOIN marks
        ON students.id = marks.student_id;

---

# 66. LEFT JOIN

Returns all records from the left table and matching records from the right table.

    SELECT *
    FROM students
    LEFT JOIN marks
        ON students.id = marks.student_id;

---

# 67. GROUP BY

Example:

    cursor.execute(
        """
        SELECT
            course,
            AVG(marks)
        FROM students
        GROUP BY course
        """
    )

---

# 68. Aggregate Functions

Common SQL aggregation functions:

    COUNT()
    SUM()
    AVG()
    MIN()
    MAX()

Example:

    cursor.execute(
        """
        SELECT
            AVG(marks)
        FROM students
        """
    )

    average = cursor.fetchone()[0]

---

# 69. SQL + Python + Pandas

This is especially useful for Data Science.

Architecture:

    MySQL
       ↓
    SQL Query
       ↓
    Python
       ↓
    Pandas DataFrame
       ↓
    EDA
       ↓
    Matplotlib
       ↓
    Machine Learning

---

# 70. Install Pandas

    pip install pandas

---

# 71. Load MySQL Data into Pandas

One simple approach is to execute the query through the connector and build a DataFrame.

    import pandas as pd

    cursor.execute(
        "SELECT * FROM students"
    )

    rows = cursor.fetchall()

    columns = [
        column[0]
        for column in cursor.description
    ]

    df = pd.DataFrame(
        rows,
        columns=columns
    )

    print(df)

---

# 72. MySQL + Pandas + SQLAlchemy

For larger data-analysis workflows, SQLAlchemy can also be used as a database abstraction layer.

Install:

    pip install sqlalchemy

MySQL connection URL concept:

    mysql+mysqlconnector://USER:PASSWORD@HOST/DATABASE

Example:

    from sqlalchemy import create_engine
    import pandas as pd

    engine = create_engine(
        "mysql+mysqlconnector://root:password@localhost/college"
    )

    df = pd.read_sql(
        "SELECT * FROM students",
        engine
    )

For real projects, keep credentials outside source code.

---

# 73. MySQL + Python Backend

A web application can use:

    Frontend
       ↓
    HTTP Request
       ↓
    Python Backend
       ↓
    MySQL Connector
       ↓
    MySQL
       ↓
    Query Result
       ↓
    Python Backend
       ↓
    HTTP Response
       ↓
    Frontend

Possible Python backend frameworks:

    Flask
    FastAPI
    Django

For API-focused projects:

    FastAPI
       +
    MySQL

is a useful combination.

---

# 74. Example Backend Flow

User sends:

    POST /login

Request:

    {
        "email": "user@example.com",
        "password": "..."
    }

Python backend:

    ↓
    Validate input
    ↓
    Query MySQL
    ↓
    Find user
    ↓
    Verify password hash
    ↓
    Return response

---

# 75. Password Storage

NEVER store passwords like:

    password = "123456"

in a real application.

Instead store:

    password_hash

Use a secure password hashing system.

Concept:

    User Password
         ↓
    Password Hashing
         ↓
    Hash
         ↓
    MySQL

During login:

    Entered Password
         ↓
    Verify Against Hash
         ↓
    Success / Failure

---

# 76. SQL Injection

SQL injection is a security vulnerability caused by unsafe construction of SQL queries.

Bad:

    username = input()

    query = (
        "SELECT * FROM users "
        + "WHERE username = '"
        + username
        + "'"
    )

Good:

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username = %s
        """,
        (username,)
    )

Remember:

> Never concatenate untrusted user input directly into SQL queries.

---

# 77. Connection Pooling

In a web application, many users may send requests.

Creating a completely new connection for every operation can be inefficient.

Connection pooling allows reusable database connections.

Concept:

    Connection Pool
       │
       ├── Connection 1
       ├── Connection 2
       ├── Connection 3
       └── Connection 4

Applications can borrow and return connections from the pool.

---

# 78. MySQL Connection Pool

MySQL Connector/Python provides pooling functionality.

Conceptually:

    from mysql.connector import pooling

    pool = pooling.MySQLConnectionPool(
        pool_name="mypool",
        pool_size=5,
        host="localhost",
        user="app_user",
        password="password",
        database="college"
    )

    connection = pool.get_connection()

For real applications, configure pooling according to expected traffic and deployment environment.

---

# 79. Repository / Database Layer

For larger projects, don't put every SQL query inside the main application file.

Better structure:

    project/
    │
    ├── app.py
    │
    ├── database/
    │   ├── connection.py
    │   └── queries.py
    │
    ├── models/
    │
    ├── services/
    │
    └── routes/

Concept:

    API Route
       ↓
    Service Layer
       ↓
    Database Layer
       ↓
    MySQL

This keeps code organized.

---

# 80. Simple Student Management Architecture

    student_project/
    │
    ├── main.py
    ├── database.py
    ├── student_service.py
    ├── requirements.txt
    ├── .env
    └── .gitignore

Flow:

    main.py
       ↓
    student_service.py
       ↓
    database.py
       ↓
    MySQL

---

# 81. Student CRUD Functions

Example:

    def add_student(
        name,
        age,
        marks
    ):
        pass

    def get_students():
        pass

    def get_student(
        student_id
    ):
        pass

    def update_student(
        student_id,
        name,
        age,
        marks
    ):
        pass

    def delete_student(
        student_id
    ):
        pass

These functions can contain the corresponding SQL operations.

---

# 82. Example get_students()

    def get_students():

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students"
        )

        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        return rows

---

# 83. Example add_student()

    def add_student(
        name,
        age,
        marks
    ):

        connection = get_connection()

        cursor = connection.cursor()

        query = """
            INSERT INTO students
            (name, age, marks)
            VALUES (%s, %s, %s)
        """

        cursor.execute(
            query,
            (name, age, marks)
        )

        connection.commit()

        cursor.close()
        connection.close()

---

# 84. SQL + Python Project Ideas

## Beginner

1. Student Management System
2. Employee Management System
3. Library Management System
4. Contact Management System

## Intermediate

5. Expense Tracker
6. Inventory Management System
7. Login/Register System
8. Online Book Store Backend

## Advanced

9. FastAPI + MySQL REST API
10. Authentication System
11. E-commerce Backend
12. ML API + MySQL
13. Analytics Dashboard
14. Recommendation System with MySQL

---

# 85. Mini Project — Student Management System

Database:

    college

Table:

    students

Columns:

    id
    name
    age
    course
    marks

Features:

    Add Student
    View Students
    Search Student
    Update Student
    Delete Student

Technology:

    Python
    MySQL

---

# 86. Mini Project — Expense Tracker

Database:

    expense_db

Table:

    expenses

Columns:

    id
    title
    amount
    category
    expense_date

Features:

    Add Expense
    View Expenses
    Update Expense
    Delete Expense
    Total Expenses
    Category-wise Expenses
    Monthly Expenses

Upgrade:

    Python
       ↓
    MySQL
       ↓
    Pandas
       ↓
    Matplotlib

---

# 87. Mini Project — Login System

Database:

    authentication

Table:

    users

Columns:

    id
    name
    email
    password_hash
    created_at

Features:

    Register
    Login
    Logout

Technology:

    Python
    MySQL
    Password Hashing
    FastAPI/Flask

---

# 88. SQL + Python Learning Roadmap

Follow this order:

    1. MySQL Basics
           ↓
    2. Database + Tables
           ↓
    3. CREATE
           ↓
    4. INSERT
           ↓
    5. SELECT
           ↓
    6. WHERE
           ↓
    7. ORDER BY
           ↓
    8. GROUP BY
           ↓
    9. JOIN
           ↓
    10. UPDATE
           ↓
    11. DELETE
           ↓
    12. MySQL User & Permissions
           ↓
    13. Python MySQL Connector
           ↓
    14. Connection
           ↓
    15. Cursor
           ↓
    16. Execute Query
           ↓
    17. fetchone / fetchall
           ↓
    18. CRUD
           ↓
    19. Transactions
           ↓
    20. Error Handling
           ↓
    21. Parameterized Queries
           ↓
    22. Environment Variables
           ↓
    23. Connection Pooling
           ↓
    24. Python Backend + MySQL
           ↓
    25. Pandas + MySQL
           ↓
    26. SQLAlchemy
           ↓
    27. Real Projects

---

# 89. Important MySQL + Python Cheat Sheet

## Install

    pip install mysql-connector-python

## Import

    import mysql.connector

## Connect

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="college"
    )

## Cursor

    cursor = connection.cursor()

## Execute

    cursor.execute(
        query,
        values
    )

## Multiple Records

    cursor.executemany(
        query,
        values
    )

## Fetch One

    cursor.fetchone()

## Fetch All

    cursor.fetchall()

## Save

    connection.commit()

## Rollback

    connection.rollback()

## Close

    cursor.close()
    connection.close()

---

# 90. Complete MySQL + Python Example

    import mysql.connector

    try:

        # 1. Connect to MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="college"
        )

        # 2. Create cursor
        cursor = connection.cursor()

        # 3. Create table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT,
                course VARCHAR(100),
                marks FLOAT
            )
        """)

        # 4. Insert
        insert_query = """
            INSERT INTO students
            (name, age, course, marks)
            VALUES (%s, %s, %s, %s)
        """

        values = (
            "Tanishk",
            19,
            "AI/ML",
            85
        )

        cursor.execute(
            insert_query,
            values
        )

        connection.commit()

        # 5. Read
        cursor.execute(
            "SELECT * FROM students"
        )

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except mysql.connector.Error as error:

        print(
            "MySQL Error:",
            error
        )

        if "connection" in locals() and connection.is_connected():
            connection.rollback()

    finally:

        if "cursor" in locals():
            cursor.close()

        if "connection" in locals() and connection.is_connected():
            connection.close()

---

# 91. Mental Model

Remember these five things:

    Connection
         ↓
    Cursor
         ↓
    Execute
         ↓
    Fetch / Commit
         ↓
    Close

For SELECT:

    Connection
         ↓
    Cursor
         ↓
    SELECT
         ↓
    fetchone/fetchall
         ↓
    Close

For INSERT/UPDATE/DELETE:

    Connection
         ↓
    Cursor
         ↓
    Query
         ↓
    commit()
         ↓
    Close

---

# 92. MySQL + Python + Data Science

A powerful workflow:

    MySQL
       ↓
    Store Raw Data
       ↓
    Python
       ↓
    Fetch Data
       ↓
    Pandas
       ↓
    Clean Data
       ↓
    Matplotlib / Seaborn
       ↓
    EDA
       ↓
    Scikit-Learn
       ↓
    Machine Learning
       ↓
    Prediction
       ↓
    MySQL / API

---

# 93. MySQL + Python + Backend

For application development:

    User
      ↓
    HTML/CSS/JavaScript
      ↓
    FastAPI / Flask
      ↓
    Python
      ↓
    MySQL Connector
      ↓
    MySQL
      ↓
    Data
      ↓
    Python
      ↓
    JSON Response
      ↓
    Frontend

---

# 94. What You Should Be Able to Do After These Notes

You should be able to:

- Install MySQL Connector/Python
- Connect Python to MySQL Server
- Create databases
- Create tables
- Define primary keys
- Define foreign keys
- Insert data
- Insert multiple rows
- Read data
- Filter data
- Sort data
- Update data
- Delete data
- Use CRUD
- Use JOINs
- Use GROUP BY
- Use aggregate functions
- Use transactions
- Use commit()
- Use rollback()
- Handle database errors
- Use parameterized queries
- Understand SQL injection
- Use environment variables
- Create dedicated application users
- Use connection pooling
- Build database layers
- Connect MySQL with Pandas
- Connect MySQL with Python backend
- Build real database-backed projects

---

# ⭐ Recommended Practice Order

Don't just memorize these notes.

Practice in this order:

    MySQL
      ↓
    Create Database
      ↓
    Create Table
      ↓
    Insert Data
      ↓
    SELECT
      ↓
    WHERE
      ↓
    UPDATE
      ↓
    DELETE
      ↓
    JOIN
      ↓
    GROUP BY
      ↓
    Python Connection
      ↓
    CRUD using Python
      ↓
    Error Handling
      ↓
    Parameterized Queries
      ↓
    Student Management System
      ↓
    MySQL + Pandas
      ↓
    MySQL + FastAPI
      ↓
    Real Project

---

# 🚀 Final Stack

For your current AI/ML + development journey:

    Python
       ↓
    NumPy
       ↓
    Pandas
       ↓
    Matplotlib
       ↓
    MySQL
       ↓
    Python + MySQL
       ↓
    Seaborn
       ↓
    EDA
       ↓
    Scikit-Learn
       ↓
    Machine Learning
       ↓
    FastAPI
       ↓
    MySQL
       ↓
    ML API
       ↓
    Deployment

> Python handles the application logic.
>
> MySQL stores structured application data.
>
> SQL retrieves and manipulates that data.
>
> MySQL Connector/Python allows Python to communicate with MySQL.
>
> Pandas can bring SQL data into DataFrames for analysis.
>
> FastAPI/Flask can expose Python + MySQL functionality through APIs.