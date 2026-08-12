# Pandas Notes

> Pandas = Python library for data manipulation, data analysis, and working with structured/tabular data.
>
> Pandas is especially useful for CSV, Excel, SQL, JSON, and other datasets.

---

# 1. What is Pandas?

Pandas is an open-source Python library used for:

- Data manipulation
- Data analysis
- Data cleaning
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Working with CSV files
- Working with Excel files
- Working with SQL databases
- Handling missing values
- Filtering and sorting data
- Grouping data
- Combining datasets

Import Pandas:

    import pandas as pd

`pd` is the commonly used alias for Pandas.

---

# 2. Why Pandas?

Suppose we have student data:

    Name      Age    Marks
    Tanishk   19     85
    Rahul     20     78
    Aman      19     92

Pandas allows us to easily:

- Read this data
- Filter rows
- Select columns
- Calculate statistics
- Find missing values
- Sort data
- Group data
- Clean data
- Visualize data

---

# 3. Main Pandas Data Structures

Pandas mainly provides two important data structures:

1. Series
2. DataFrame

---

# 4. Series

A Series is a one-dimensional labeled array.

Example:

    import pandas as pd

    marks = pd.Series([85, 78, 92, 88])

    print(marks)

Output:

    0    85
    1    78
    2    92
    3    88

The left side is the index.

The right side is the value.

---

# 5. Creating Series

From a list:

    s = pd.Series([10, 20, 30, 40])

From a NumPy array:

    import numpy as np

    arr = np.array([10, 20, 30])

    s = pd.Series(arr)

---

# 6. Custom Index in Series

    marks = pd.Series(
        [85, 78, 92],
        index=["Tanishk", "Rahul", "Aman"]
    )

Access value:

    print(marks["Tanishk"])

Output:

    85

---

# 7. DataFrame

A DataFrame is a two-dimensional labeled data structure.

It looks like a table.

Example:

    data = {
        "Name": ["Tanishk", "Rahul", "Aman"],
        "Age": [19, 20, 19],
        "Marks": [85, 78, 92]
    }

    df = pd.DataFrame(data)

    print(df)

Output:

          Name  Age  Marks
    0  Tanishk   19     85
    1    Rahul   20     78
    2     Aman   19     92

---

# 8. DataFrame Components

A DataFrame contains:

- Rows
- Columns
- Index
- Values

Example:

          Name  Age
    0  Tanishk   19
    1    Rahul   20

Here:

    Columns = Name, Age
    Index   = 0, 1
    Rows    = 2
    Values  = Tanishk, 19, Rahul, 20

---

# 9. Creating DataFrame from List

    data = [
        ["Tanishk", 19, 85],
        ["Rahul", 20, 78],
        ["Aman", 19, 92]
    ]

    df = pd.DataFrame(
        data,
        columns=["Name", "Age", "Marks"]
    )

---

# 10. Creating DataFrame from Dictionary

    data = {
        "Name": ["Tanishk", "Rahul", "Aman"],
        "Age": [19, 20, 19],
        "Marks": [85, 78, 92]
    }

    df = pd.DataFrame(data)

This is one of the most common ways to create a DataFrame.

---

# 11. Reading CSV File

CSV = Comma-Separated Values.

Read CSV:

    df = pd.read_csv("students.csv")

Display:

    print(df)

CSV files are extremely common in:

- Data Science
- Machine Learning
- Data Analysis
- EDA

---

# 12. Reading Excel File

    df = pd.read_excel("students.xlsx")

Depending on the environment, an appropriate Excel engine/package may be required.

---

# 13. Reading JSON

    df = pd.read_json("students.json")

---

# 14. Reading SQL Data

Pandas can work with SQL databases.

Example:

    df = pd.read_sql_query(
        "SELECT * FROM students",
        connection
    )

This is useful when working with:

- SQLite
- MySQL
- PostgreSQL
- Other supported databases

---

# 15. Saving DataFrame to CSV

    df.to_csv("output.csv", index=False)

`index=False` prevents Pandas from writing the DataFrame index as an extra column.

---

# 16. Saving DataFrame to Excel

    df.to_excel("output.xlsx", index=False)

---

# 17. Saving DataFrame to JSON

    df.to_json("output.json")

---

# 18. head()

`head()` displays the first rows.

    df.head()

Default:

    df.head(5)

First 10 rows:

    df.head(10)

---

# 19. tail()

Displays the last rows.

    df.tail()

Last 10 rows:

    df.tail(10)

---

# 20. sample()

Returns random rows.

    df.sample(5)

This is useful for quickly inspecting a dataset.

---

# 21. shape

Returns:

    (rows, columns)

Example:

    df.shape

Output:

    (100, 5)

Meaning:

    100 rows
    5 columns

---

# 22. columns

Returns column names.

    df.columns

Example output:

    Index(["Name", "Age", "Marks"], dtype="object")

Convert to list:

    df.columns.tolist()

---

# 23. index

Returns the DataFrame index.

    df.index

---

# 24. dtypes

Returns the data type of each column.

    df.dtypes

Example:

    Name     object
    Age       int64
    Marks     int64

---

# 25. info()

Provides important information about the DataFrame.

    df.info()

It shows:

- Number of rows
- Column names
- Non-null values
- Data types
- Memory usage

Very important for EDA.

---

# 26. describe()

Provides statistical summary of numerical columns.

    df.describe()

Usually includes:

- count
- mean
- std
- min
- 25%
- 50%
- 75%
- max

---

# 27. describe(include="all")

Can provide summary information for more types of columns.

    df.describe(include="all")

---

# 28. Selecting a Column

Select one column:

    df["Name"]

Select another:

    df["Marks"]

The result is usually a Series.

---

# 29. Selecting Multiple Columns

    df[["Name", "Marks"]]

The result is a DataFrame.

Important:

Single column:

    df["Marks"]

Multiple columns:

    df[["Name", "Marks"]]

---

# 30. Adding a New Column

    df["Passed"] = df["Marks"] >= 40

Example:

    df["Bonus"] = df["Marks"] + 5

---

# 31. Updating a Column

    df["Marks"] = df["Marks"] + 5

This increases every student's marks by 5.

---

# 32. Renaming Columns

Rename one column:

    df.rename(
        columns={"Marks": "Score"},
        inplace=True
    )

Rename multiple columns:

    df.rename(
        columns={
            "Name": "Student_Name",
            "Marks": "Score"
        },
        inplace=True
    )

---

# 33. Dropping a Column

    df.drop(
        columns=["Age"],
        inplace=True
    )

Without modifying the original:

    new_df = df.drop(columns=["Age"])

---

# 34. Dropping Rows

Drop row with index 2:

    df.drop(index=2)

Drop multiple rows:

    df.drop(index=[1, 2, 3])

---

# 35. Resetting Index

After filtering or dropping rows, you may want a clean index.

    df.reset_index(drop=True, inplace=True)

Example:

Before:

    0
    2
    5
    8

After:

    0
    1
    2
    3

---

# 36. Selecting Rows with loc

`loc` is label-based selection.

Example:

    df.loc[0]

Select specific columns:

    df.loc[0, "Name"]

Select multiple rows:

    df.loc[0:2]

Select rows and columns:

    df.loc[0:2, ["Name", "Marks"]]

---

# 37. Selecting Rows with iloc

`iloc` is integer-position based selection.

First row:

    df.iloc[0]

First row, second column:

    df.iloc[0, 1]

First three rows:

    df.iloc[0:3]

First three rows and first two columns:

    df.iloc[0:3, 0:2]

---

# 38. loc vs iloc

| loc | iloc |
|---|---|
| Label-based | Position-based |
| Uses labels | Uses integer positions |
| `df.loc[2]` | `df.iloc[2]` |
| Useful with meaningful indexes | Useful with row/column positions |

---

# 39. Filtering Data

Filter students with marks greater than 80:

    df[df["Marks"] > 80]

Filter age greater than 18:

    df[df["Age"] > 18]

---

# 40. Multiple Conditions

AND condition:

    df[
        (df["Age"] > 18) &
        (df["Marks"] > 80)
    ]

OR condition:

    df[
        (df["Age"] > 18) |
        (df["Marks"] > 80)
    ]

Important:

Use:

    &
    |

instead of Python's:

    and
    or

for element-wise Pandas conditions.

---

# 41. NOT Condition

    df[~(df["Marks"] > 80)]

This selects rows where marks are NOT greater than 80.

---

# 42. isin()

Used to check multiple possible values.

    df[df["Course"].isin(["AI/ML", "CSE"])]

Equivalent idea:

    Course == "AI/ML"
    OR
    Course == "CSE"

---

# 43. between()

Checks whether values are inside a range.

    df[df["Marks"].between(70, 90)]

---

# 44. String Filtering

Use `.str`.

Starts with A:

    df[df["Name"].str.startswith("A")]

Contains "an":

    df[df["Name"].str.contains("an", case=False, na=False)]

Ends with n:

    df[df["Name"].str.endswith("n", na=False)]

---

# 45. Sorting Data

Sort by marks:

    df.sort_values("Marks")

Descending:

    df.sort_values(
        "Marks",
        ascending=False
    )

Sort by multiple columns:

    df.sort_values(
        ["Course", "Marks"],
        ascending=[True, False]
    )

---

# 46. value_counts()

Counts unique values.

    df["Course"].value_counts()

Example:

    AI/ML    20
    CSE      15
    ECE      10

Very useful for categorical data analysis.

---

# 47. unique()

Returns unique values.

    df["Course"].unique()

---

# 48. nunique()

Returns number of unique values.

    df["Course"].nunique()

---

# 49. sum()

Sum values.

    df["Marks"].sum()

---

# 50. mean()

Average value.

    df["Marks"].mean()

---

# 51. median()

Median value.

    df["Marks"].median()

---

# 52. min()

Minimum value.

    df["Marks"].min()

---

# 53. max()

Maximum value.

    df["Marks"].max()

---

# 54. std()

Standard deviation.

    df["Marks"].std()

---

# 55. var()

Variance.

    df["Marks"].var()

---

# 56. count()

Counts non-null values.

    df["Marks"].count()

Important:

`count()` ignores missing values.

---

# 57. Missing Values

Missing values are usually represented as:

    NaN

Check missing values:

    df.isna()

or:

    df.isnull()

---

# 58. Count Missing Values

    df.isna().sum()

This gives the number of missing values in each column.

Example:

    Name      0
    Age       2
    Marks     3

---

# 59. Check Whether DataFrame Contains Missing Values

    df.isna().any()

This tells whether each column contains at least one missing value.

---

# 60. Percentage of Missing Values

    df.isna().mean() * 100

This gives the percentage of missing values in each column.

---

# 61. dropna()

Removes rows containing missing values.

    df.dropna()

Remove rows where all values are missing:

    df.dropna(how="all")

Remove rows with missing values in a specific column:

    df.dropna(subset=["Marks"])

---

# 62. fillna()

Fills missing values.

Fill with 0:

    df["Marks"] = df["Marks"].fillna(0)

Fill with mean:

    df["Marks"] = df["Marks"].fillna(
        df["Marks"].mean()
    )

Fill with median:

    df["Marks"] = df["Marks"].fillna(
        df["Marks"].median()
    )

---

# 63. Forward Fill

Fills missing values using the previous value.

    df["Marks"] = df["Marks"].ffill()

---

# 64. Backward Fill

Fills missing values using the next available value.

    df["Marks"] = df["Marks"].bfill()

---

# 65. Duplicates

Check duplicate rows:

    df.duplicated()

Count duplicate rows:

    df.duplicated().sum()

---

# 66. drop_duplicates()

Remove duplicate rows:

    df.drop_duplicates()

Modify original:

    df.drop_duplicates(inplace=True)

Based on a specific column:

    df.drop_duplicates(
        subset=["Email"]
    )

---

# 67. Handling Data Types

Convert column to integer:

    df["Age"] = df["Age"].astype(int)

Convert to float:

    df["Marks"] = df["Marks"].astype(float)

Convert to string:

    df["Name"] = df["Name"].astype(str)

---

# 68. to_numeric()

Useful when a column contains numeric values stored as strings.

    df["Marks"] = pd.to_numeric(
        df["Marks"],
        errors="coerce"
    )

`errors="coerce"` converts invalid values into NaN.

---

# 69. String Operations

Convert to lowercase:

    df["Name"] = df["Name"].str.lower()

Convert to uppercase:

    df["Name"] = df["Name"].str.upper()

Remove extra spaces:

    df["Name"] = df["Name"].str.strip()

Replace text:

    df["Course"] = df["Course"].str.replace(
        "AI ML",
        "AI/ML",
        regex=False
    )

---

# 70. apply()

`apply()` applies a function to values.

Example:

    df["Marks"] = df["Marks"].apply(
        lambda x: x + 5
    )

Example with function:

    def add_bonus(x):
        return x + 5

    df["Marks"] = df["Marks"].apply(add_bonus)

---

# 71. lambda

A lambda is a small anonymous function.

Example:

    lambda x: x * 2

Using Pandas:

    df["Double_Marks"] = df["Marks"].apply(
        lambda x: x * 2
    )

---

# 72. map()

`map()` is useful for mapping values in a Series.

Example:

    grade_map = {
        "A": 90,
        "B": 80,
        "C": 70
    }

    df["Score"] = df["Grade"].map(grade_map)

---

# 73. replace()

Replace values directly.

    df["Gender"] = df["Gender"].replace(
        {
            "M": "Male",
            "F": "Female"
        }
    )

---

# 74. GroupBy

`groupby()` is one of the most important Pandas concepts.

Example:

    df.groupby("Course")["Marks"].mean()

This calculates average marks for each course.

---

# 75. GroupBy Count

    df.groupby("Course").size()

or:

    df.groupby("Course")["Name"].count()

---

# 76. GroupBy Multiple Columns

    df.groupby(
        ["Course", "Gender"]
    )["Marks"].mean()

This groups data using multiple columns.

---

# 77. Multiple Aggregations

    df.groupby("Course")["Marks"].agg(
        ["mean", "max", "min", "count"]
    )

This calculates multiple statistics.

---

# 78. Named Aggregation

    df.groupby("Course").agg(
        average_marks=("Marks", "mean"),
        highest_marks=("Marks", "max"),
        student_count=("Name", "count")
    )

This creates meaningful output column names.

---

# 79. Pivot Table

A pivot table summarizes data.

Example:

    pd.pivot_table(
        df,
        values="Marks",
        index="Course",
        aggfunc="mean"
    )

---

# 80. Crosstab

Used to create a frequency table.

    pd.crosstab(
        df["Course"],
        df["Gender"]
    )

---

# 81. Combining DataFrames

Pandas provides:

- concat()
- merge()
- join()

These are important when working with multiple datasets.

---

# 82. concat()

Concatenate DataFrames vertically.

    df1 = pd.DataFrame({
        "Name": ["A", "B"],
        "Marks": [80, 90]
    })

    df2 = pd.DataFrame({
        "Name": ["C", "D"],
        "Marks": [70, 85]
    })

    result = pd.concat(
        [df1, df2],
        ignore_index=True
    )

---

# 83. concat() Horizontally

    result = pd.concat(
        [df1, df2],
        axis=1
    )

`axis=0` → rows

`axis=1` → columns

---

# 84. merge()

`merge()` is similar to SQL JOIN.

Example:

Students:

    student_id | name
    -----------|-------
    1          | Tanishk
    2          | Rahul

Marks:

    student_id | marks
    -----------|------
    1          | 85
    2          | 90

Merge:

    result = pd.merge(
        students,
        marks,
        on="student_id"
    )

---

# 85. Merge Types

Common merge types:

- inner
- left
- right
- outer

Inner:

    pd.merge(
        df1,
        df2,
        on="id",
        how="inner"
    )

Left:

    pd.merge(
        df1,
        df2,
        on="id",
        how="left"
    )

Right:

    pd.merge(
        df1,
        df2,
        on="id",
        how="right"
    )

Outer:

    pd.merge(
        df1,
        df2,
        on="id",
        how="outer"
    )

---

# 86. SQL JOIN vs Pandas merge()

Conceptually:

    SQL INNER JOIN
          ↓
    pd.merge(..., how="inner")

    SQL LEFT JOIN
          ↓
    pd.merge(..., how="left")

    SQL RIGHT JOIN
          ↓
    pd.merge(..., how="right")

    SQL FULL OUTER JOIN
          ↓
    pd.merge(..., how="outer")

---

# 87. Joining on Different Column Names

    pd.merge(
        df1,
        df2,
        left_on="student_id",
        right_on="id"
    )

---

# 88. Joining Multiple DataFrames

You can perform multiple merges:

    result = pd.merge(
        students,
        marks,
        on="student_id"
    )

    result = pd.merge(
        result,
        courses,
        on="course_id"
    )

---

# 89. Datetime

Pandas provides powerful datetime functionality.

Convert column to datetime:

    df["Date"] = pd.to_datetime(
        df["Date"]
    )

---

# 90. Extract Date Components

Year:

    df["Date"].dt.year

Month:

    df["Date"].dt.month

Day:

    df["Date"].dt.day

Day of week:

    df["Date"].dt.day_name()

---

# 91. Filtering Dates

    df[
        df["Date"] >= "2026-01-01"
    ]

Date range:

    df[
        (df["Date"] >= "2026-01-01") &
        (df["Date"] <= "2026-12-31")
    ]

---

# 92. Date Difference

Example:

    df["Days"] = (
        df["End_Date"] -
        df["Start_Date"]
    ).dt.days

---

# 93. Index

Every DataFrame has an index.

Example:

    df.index

Set a column as index:

    df.set_index(
        "student_id",
        inplace=True
    )

---

# 94. Reset Index

    df.reset_index(inplace=True)

Useful after setting an index or performing certain transformations.

---

# 95. Rename Index

    df.index.name = "Student_ID"

---

# 96. Query

Pandas `query()` can make filtering more readable.

Example:

    df.query("Marks > 80")

Multiple conditions:

    df.query(
        "Marks > 80 and Age > 18"
    )

---

# 97. Copy DataFrame

Create an independent copy:

    new_df = df.copy()

This is useful when you want to modify a DataFrame without unintentionally modifying the original.

---

# 98. Memory Usage

Check memory usage:

    df.memory_usage()

For detailed information:

    df.info(memory_usage="deep")

---

# 99. Correlation

Correlation measures how numerical variables move in relation to each other.

    df.corr(numeric_only=True)

Values are generally between:

    -1 and +1

Rough interpretation:

    +1 → strong positive relationship
     0 → little/no linear relationship
    -1 → strong negative relationship

Correlation does not automatically mean causation.

---

# 100. Covariance

Covariance measures how two variables vary together.

    df.cov(numeric_only=True)

---

# 101. Rank

Assign ranks to values.

    df["Rank"] = df["Marks"].rank(
        ascending=False
    )

---

# 102. nlargest()

Get the largest values.

    df.nlargest(
        5,
        "Marks"
    )

Returns top 5 rows according to Marks.

---

# 103. nsmallest()

Get the smallest values.

    df.nsmallest(
        5,
        "Marks"
    )

---

# 104. Where

`where()` keeps values where a condition is True and replaces others.

    df["Marks"].where(
        df["Marks"] >= 40,
        0
    )

---

# 105. Clip

Restrict values to a range.

    df["Marks"].clip(
        lower=0,
        upper=100
    )

---

# 106. Reading Large Datasets

For large CSV files, use chunks.

    for chunk in pd.read_csv(
        "large_file.csv",
        chunksize=10000
    ):
        print(chunk.shape)

This avoids loading the entire dataset into memory at once.

---

# 107. Common File Formats

Pandas can work with many formats.

CSV:

    pd.read_csv()
    df.to_csv()

Excel:

    pd.read_excel()
    df.to_excel()

JSON:

    pd.read_json()
    df.to_json()

SQL:

    pd.read_sql()
    pd.read_sql_query()
    df.to_sql()

---

# 108. EDA with Pandas

EDA = Exploratory Data Analysis.

Typical workflow:

    1. Load dataset
            ↓
    2. Understand dataset
            ↓
    3. Check shape
            ↓
    4. Check columns
            ↓
    5. Check data types
            ↓
    6. Check missing values
            ↓
    7. Check duplicates
            ↓
    8. Check statistics
            ↓
    9. Analyze distributions
            ↓
    10. Find relationships
            ↓
    11. Clean data
            ↓
    12. Prepare data for ML

---

# 109. Basic EDA Template

    import pandas as pd

    df = pd.read_csv("data.csv")

    # First rows
    print(df.head())

    # Shape
    print(df.shape)

    # Columns
    print(df.columns)

    # Data types and non-null values
    df.info()

    # Statistical summary
    print(df.describe())

    # Missing values
    print(df.isna().sum())

    # Duplicate rows
    print(df.duplicated().sum())

    # Unique values
    print(df.nunique())

---

# 110. Data Cleaning Workflow

A common data cleaning process:

    Load data
       ↓
    Check shape
       ↓
    Check data types
       ↓
    Check missing values
       ↓
    Check duplicates
       ↓
    Fix incorrect data types
       ↓
    Handle missing values
       ↓
    Remove/fix duplicates
       ↓
    Handle inconsistent values
       ↓
    Validate data
       ↓
    Save cleaned dataset

---

# 111. Common Data Cleaning Problems

Look for:

- Missing values
- Duplicate rows
- Wrong data types
- Incorrect spelling
- Extra spaces
- Invalid dates
- Outliers
- Inconsistent categories
- Invalid numerical values

Example:

    "AI/ML"
    "AI ML"
    "ai/ml"
    " AI/ML "

These may represent the same category but are stored differently.

---

# 112. Pandas + NumPy

Pandas works closely with NumPy.

Example:

    import numpy as np
    import pandas as pd

    df = pd.DataFrame({
        "Marks": [80, 90, 70, 85]
    })

    mean = np.mean(df["Marks"])

You can also use:

    df["Marks"].mean()

---

# 113. Converting DataFrame to NumPy

    arr = df.to_numpy()

or:

    arr = df.values

`to_numpy()` is generally preferred.

---

# 114. Converting Series to NumPy

    arr = df["Marks"].to_numpy()

---

# 115. Pandas + Machine Learning

Pandas is heavily used before Machine Learning.

Typical workflow:

    Dataset
       ↓
    Pandas
       ↓
    Data Cleaning
       ↓
    EDA
       ↓
    Feature Selection
       ↓
    Feature Engineering
       ↓
    NumPy / Scikit-Learn
       ↓
    ML Model

Example:

    X = df[["Age", "Income", "Experience"]]

    y = df["Salary"]

Here:

    X = Features
    y = Target

---

# 116. Important Pandas Functions

## Data Inspection

    head()
    tail()
    sample()
    info()
    describe()
    shape
    columns
    dtypes

## Selection

    loc[]
    iloc[]
    []

## Cleaning

    isna()
    isnull()
    dropna()
    fillna()
    ffill()
    bfill()
    drop_duplicates()
    astype()

## Filtering

    isin()
    between()
    query()

## Sorting

    sort_values()
    sort_index()

## Aggregation

    sum()
    mean()
    median()
    min()
    max()
    std()
    var()
    count()
    value_counts()

## Grouping

    groupby()
    agg()

## Combining

    concat()
    merge()
    join()

## Reshaping

    pivot()
    pivot_table()
    melt()

## Date/Time

    to_datetime()
    .dt.year
    .dt.month
    .dt.day

---

# 117. Pivot and Melt

## pivot_table()

Used to summarize data.

    pd.pivot_table(
        df,
        values="Sales",
        index="City",
        columns="Product",
        aggfunc="sum"
    )

## melt()

Converts wide-format data into long-format data.

    pd.melt(df)

These are useful for data reshaping.

---

# 118. Wide vs Long Data

Wide format:

    Name    Math    Science
    A       80      90
    B       70      85

Long format:

    Name    Subject    Marks
    A       Math       80
    A       Science    90
    B       Math       70
    B       Science    85

Pandas can convert between these formats.

---

# 119. Common Mistakes

## Mistake 1

Using:

    df["Marks"] > 80 and df["Age"] > 18

Use:

    (df["Marks"] > 80) & (df["Age"] > 18)

---

## Mistake 2

Forgetting parentheses:

    df["Marks"] > 80 & df["Age"] > 18

Correct:

    (df["Marks"] > 80) & (df["Age"] > 18)

---

## Mistake 3

Confusing loc and iloc.

Remember:

    loc  → labels
    iloc → positions

---

## Mistake 4

Ignoring missing values.

Always check:

    df.isna().sum()

---

## Mistake 5

Ignoring duplicates.

Check:

    df.duplicated().sum()

---

## Mistake 6

Modifying a DataFrame without understanding whether you are working on a copy or a view.

When an independent DataFrame is needed:

    df2 = df.copy()

---

# 120. Important Difference: Series vs DataFrame

| Series | DataFrame |
|---|---|
| 1D | 2D |
| One column of data | Multiple columns |
| `pd.Series()` | `pd.DataFrame()` |
| Has index | Has rows, columns, and index |

Example:

    df["Marks"]

returns a Series.

Example:

    df[["Name", "Marks"]]

returns a DataFrame.

---

# 121. Pandas vs NumPy

| NumPy | Pandas |
|---|---|
| Numerical computing | Data analysis |
| ndarray | Series/DataFrame |
| Mainly numerical arrays | Labeled/tabular data |
| Fast numerical operations | Powerful data manipulation |
| Mathematical operations | Cleaning, grouping, merging, EDA |

Simple idea:

    NumPy → Numerical Arrays
    Pandas → Structured Data

---

# 122. SQL vs Pandas

Many SQL operations have Pandas equivalents.

SQL:

    SELECT * FROM students;

Pandas:

    df

SQL:

    SELECT Name, Marks
    FROM students;

Pandas:

    df[["Name", "Marks"]]

SQL:

    SELECT *
    FROM students
    WHERE Marks > 80;

Pandas:

    df[df["Marks"] > 80]

SQL:

    SELECT Course, AVG(Marks)
    FROM students
    GROUP BY Course;

Pandas:

    df.groupby("Course")["Marks"].mean()

SQL JOIN:

    JOIN

Pandas:

    pd.merge()

---

# 123. Pandas Learning Roadmap

Follow this order:

    1. Pandas Introduction
            ↓
    2. Series
            ↓
    3. DataFrame
            ↓
    4. Creating DataFrames
            ↓
    5. Reading CSV
            ↓
    6. Data Inspection
            ↓
    7. Selecting Columns
            ↓
    8. loc / iloc
            ↓
    9. Filtering
            ↓
    10. Sorting
            ↓
    11. Missing Values
            ↓
    12. Duplicates
            ↓
    13. Data Types
            ↓
    14. String Operations
            ↓
    15. apply / map
            ↓
    16. GroupBy
            ↓
    17. Aggregation
            ↓
    18. Merge / Join / Concat
            ↓
    19. Datetime
            ↓
    20. Pivot Tables
            ↓
    21. Data Cleaning
            ↓
    22. EDA
            ↓
    23. Pandas + NumPy
            ↓
    24. Pandas + SQL
            ↓
    25. Pandas + Machine Learning

---

# 124. Practice Dataset

Use this dataset for practice:

    data = {
        "Name": [
            "Tanishk",
            "Rahul",
            "Aman",
            "Rohit",
            "Priya",
            "Neha",
            "Vikas",
            "Ankit"
        ],

        "Age": [
            19,
            20,
            19,
            21,
            20,
            19,
            22,
            20
        ],

        "Course": [
            "AI/ML",
            "CSE",
            "AI/ML",
            "CSE",
            "ECE",
            "AI/ML",
            "CSE",
            "ECE"
        ],

        "Marks": [
            85,
            78,
            92,
            65,
            88,
            95,
            72,
            81
        ]
    }

    df = pd.DataFrame(data)

Practice:

1. Display first 5 rows.
2. Display last 3 rows.
3. Find shape.
4. Find data types.
5. Find average marks.
6. Find highest marks.
7. Find lowest marks.
8. Find students with marks > 80.
9. Find AI/ML students.
10. Sort students by marks.
11. Find average marks by course.
12. Count students by course.
13. Find the student with highest marks.
14. Find students whose age is 20.
15. Add a "Passed" column.
16. Create a "Grade" column.
17. Find unique courses.
18. Count unique courses.
19. Find duplicate rows.
20. Create a summary using groupby().

---

# 125. Mini Project — Student Data Analysis

Create a CSV file containing:

- Student ID
- Name
- Age
- Gender
- Course
- Marks
- Attendance

Then perform:

## Step 1 — Load Data

    df = pd.read_csv("students.csv")

## Step 2 — Understand Data

    df.head()
    df.shape
    df.info()
    df.describe()

## Step 3 — Clean Data

    df.isna().sum()
    df.duplicated().sum()

Handle missing values and duplicates.

## Step 4 — Analyze

Find:

- Average marks
- Highest marks
- Lowest marks
- Course-wise average
- Gender-wise average
- Top 5 students
- Students below passing marks
- Students with low attendance

## Step 5 — Export

    df.to_csv(
        "cleaned_students.csv",
        index=False
    )

---

# 126. EDA Checklist

Whenever you receive a new dataset:

    df.head()
    df.tail()
    df.shape
    df.columns
    df.dtypes
    df.info()
    df.describe()

Then:

    df.isna().sum()
    df.duplicated().sum()
    df.nunique()

Then inspect:

    df["column"].unique()
    df["column"].value_counts()

Then analyze:

    groupby()
    sort_values()
    corr()

Then clean:

    fillna()
    dropna()
    drop_duplicates()
    astype()

---

# 127. Final Goal

After learning Pandas, you should be able to:

- Create Series and DataFrames
- Read CSV/Excel/JSON data
- Inspect datasets
- Select rows and columns
- Filter data
- Sort data
- Handle missing values
- Remove duplicates
- Change data types
- Perform string operations
- Group data
- Perform aggregations
- Merge datasets
- Concatenate datasets
- Work with dates
- Reshape data
- Perform basic EDA
- Prepare datasets for Machine Learning
- Work with SQL databases
- Use Pandas together with NumPy and Scikit-Learn

---

# ⭐ Recommended Next Step

After Pandas:

    NumPy
       ↓
    Pandas
       ↓
    Matplotlib
       ↓
    Seaborn
       ↓
    Data Cleaning
       ↓
    EDA
       ↓
    Feature Engineering
       ↓
    Scikit-Learn
       ↓
    Machine Learning

> NumPy = Numerical Computing
>
> Pandas = Data Manipulation + Analysis
>
> Matplotlib = Data Visualization
>
> Seaborn = Statistical Visualization
>
> Scikit-Learn = Machine Learning