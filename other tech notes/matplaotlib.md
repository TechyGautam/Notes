# Matplotlib Notes

> Matplotlib is a Python library used for data visualization.
>
> It helps us convert data into graphs and charts so that patterns, trends, comparisons, and distributions become easier to understand.

---

# 1. What is Matplotlib?

Matplotlib is one of the most popular Python visualization libraries.

It can be used to create:

- Line charts
- Bar charts
- Histograms
- Scatter plots
- Pie charts
- Box plots
- Area charts
- Subplots
- Custom visualizations

Import Matplotlib:

    import matplotlib.pyplot as plt

`plt` is the commonly used alias for `matplotlib.pyplot`.

---

# 2. Why Matplotlib?

Numbers in a dataset can sometimes be difficult to understand.

Example:

    months = ["Jan", "Feb", "Mar", "Apr"]
    sales = [100, 150, 120, 200]

A graph can immediately show:

- Which month had the highest sales
- Which month had the lowest sales
- Whether sales are increasing or decreasing
- Overall trends

Visualization makes data easier to understand.

---

# 3. Basic Matplotlib Workflow

The basic workflow is:

    Import Matplotlib
          ↓
    Prepare data
          ↓
    Create plot
          ↓
    Add labels/title
          ↓
    Customize plot
          ↓
    Show plot

Example:

    import matplotlib.pyplot as plt

    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 30, 25]

    plt.plot(x, y)

    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("My First Plot")

    plt.show()

---

# 4. First Line Plot

    import matplotlib.pyplot as plt

    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 30, 25]

    plt.plot(x, y)

    plt.show()

`plot()` is mainly used for line plots.

---

# 5. xlabel()

Adds a label to the X-axis.

    plt.xlabel("Time")

Example:

    plt.plot(x, y)

    plt.xlabel("Days")

---

# 6. ylabel()

Adds a label to the Y-axis.

    plt.ylabel("Sales")

---

# 7. title()

Adds a title to the graph.

    plt.title("Monthly Sales")

---

# 8. show()

Displays the plot.

    plt.show()

In scripts, `plt.show()` is generally used at the end of the plotting commands.

---

# 9. Line Plot

Line plots are useful for:

- Trends
- Time series
- Continuous data
- Changes over time

Example:

    days = [1, 2, 3, 4, 5]
    temperature = [25, 27, 26, 30, 29]

    plt.plot(days, temperature)

    plt.xlabel("Day")
    plt.ylabel("Temperature")
    plt.title("Temperature Trend")

    plt.show()

---

# 10. Line Styles

You can customize the line style.

Common styles:

    "-"
    "--"
    ":"
    "-."

Example:

    plt.plot(
        x,
        y,
        linestyle="--"
    )

---

# 11. Markers

Markers show individual data points.

Common markers:

    "o"   → circle
    "s"   → square
    "^"   → triangle
    "*"   → star
    "x"   → x
    "+"   → plus

Example:

    plt.plot(
        x,
        y,
        marker="o"
    )

---

# 12. Line Width

Change line thickness:

    plt.plot(
        x,
        y,
        linewidth=3
    )

---

# 13. Multiple Lines

You can plot multiple datasets.

    months = ["Jan", "Feb", "Mar", "Apr"]

    sales_2025 = [100, 150, 120, 180]
    sales_2026 = [120, 170, 160, 210]

    plt.plot(
        months,
        sales_2025,
        label="2025"
    )

    plt.plot(
        months,
        sales_2026,
        label="2026"
    )

    plt.legend()

    plt.show()

---

# 14. legend()

A legend explains different lines or datasets.

    plt.legend()

You usually provide labels while plotting:

    plt.plot(
        x,
        y,
        label="Sales"
    )

Then:

    plt.legend()

---

# 15. Grid

Add grid lines:

    plt.grid()

You can also customize it:

    plt.grid(
        linestyle="--",
        alpha=0.5
    )

Grid lines can make values easier to read.

---

# 16. Figure Size

Set figure size:

    plt.figure(
        figsize=(10, 6)
    )

`figsize` is:

    (width, height)

Example:

    plt.figure(figsize=(12, 5))

---

# 17. Bar Chart

Bar charts are useful for comparing categories.

Example:

    subjects = [
        "Math",
        "Science",
        "English",
        "Python"
    ]

    marks = [
        85,
        90,
        78,
        95
    ]

    plt.bar(
        subjects,
        marks
    )

    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Student Marks")

    plt.show()

---

# 18. Horizontal Bar Chart

Use `barh()`.

    plt.barh(
        subjects,
        marks
    )

This is useful when category names are long.

---

# 19. Bar Width

    plt.bar(
        subjects,
        marks,
        width=0.6
    )

---

# 20. Grouped Bar Chart

Useful for comparing two or more values for each category.

Example:

    import numpy as np
    import matplotlib.pyplot as plt

    subjects = [
        "Math",
        "Science",
        "Python"
    ]

    student1 = [80, 85, 90]
    student2 = [75, 90, 95]

    x = np.arange(len(subjects))

    width = 0.35

    plt.bar(
        x - width/2,
        student1,
        width,
        label="Student 1"
    )

    plt.bar(
        x + width/2,
        student2,
        width,
        label="Student 2"
    )

    plt.xticks(
        x,
        subjects
    )

    plt.legend()

    plt.show()

---

# 21. Histogram

Histogram is used to understand the distribution of numerical data.

Example:

    marks = [
        45, 50, 55, 60,
        62, 65, 68, 70,
        72, 75, 78, 80,
        85, 88, 90, 95
    ]

    plt.hist(marks)

    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.title("Marks Distribution")

    plt.show()

---

# 22. Bins in Histogram

Bins determine how values are grouped.

    plt.hist(
        marks,
        bins=5
    )

More bins:

    plt.hist(
        marks,
        bins=10
    )

Choosing bins appropriately can make the distribution easier to interpret.

---

# 23. Scatter Plot

Scatter plots show relationships between two numerical variables.

Example:

    hours = [
        1, 2, 3, 4, 5, 6
    ]

    marks = [
        40, 45, 55, 65, 75, 85
    ]

    plt.scatter(
        hours,
        marks
    )

    plt.xlabel("Study Hours")
    plt.ylabel("Marks")
    plt.title("Study Hours vs Marks")

    plt.show()

---

# 24. Scatter Plot Uses

Scatter plots are useful for:

- Finding relationships
- Identifying trends
- Detecting clusters
- Detecting possible outliers
- Understanding correlation

Example:

    Study Hours ↑
          |
          |       *
          |     *
          |   *
          | *
          +----------------→ Marks

---

# 25. Pie Chart

Pie charts show proportions.

Example:

    labels = [
        "Python",
        "Java",
        "C++",
        "JavaScript"
    ]

    values = [
        40,
        25,
        20,
        15
    ]

    plt.pie(
        values,
        labels=labels
    )

    plt.title("Programming Languages")

    plt.show()

Pie charts work best with a small number of categories.

---

# 26. autopct

Display percentages:

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

Example output format:

    40.0%
    25.0%
    20.0%
    15.0%

---

# 27. Explode in Pie Chart

You can separate a slice:

    explode = [
        0.1,
        0,
        0,
        0
    ]

    plt.pie(
        values,
        labels=labels,
        explode=explode,
        autopct="%1.1f%%"
    )

---

# 28. Box Plot

Box plots are useful for understanding:

- Distribution
- Median
- Quartiles
- Spread
- Potential outliers

Example:

    marks = [
        45, 50, 55, 60,
        62, 65, 68, 70,
        72, 75, 78, 80,
        85, 88, 90, 95
    ]

    plt.boxplot(marks)

    plt.ylabel("Marks")
    plt.title("Marks Distribution")

    plt.show()

---

# 29. Box Plot Components

A box plot generally represents:

    Minimum
       |
    Q1
       |
    Median
       |
    Q3
       |
    Maximum

Important:

    IQR = Q3 - Q1

Points far from the main distribution may be identified as potential outliers.

---

# 30. Area Plot

An area plot can show the magnitude of values over an ordered axis.

Example:

    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 30, 25]

    plt.fill_between(
        x,
        y
    )

    plt.plot(
        x,
        y
    )

    plt.show()

---

# 31. xticks()

Customize X-axis labels.

    plt.xticks(
        [0, 1, 2],
        ["A", "B", "C"]
    )

You can also rotate labels:

    plt.xticks(
        rotation=45
    )

---

# 32. yticks()

Customize Y-axis ticks.

    plt.yticks(
        [0, 20, 40, 60, 80, 100]
    )

---

# 33. xlim()

Set X-axis limits.

    plt.xlim(
        0,
        10
    )

---

# 34. ylim()

Set Y-axis limits.

    plt.ylim(
        0,
        100
    )

---

# 35. Text on Plot

Add text:

    plt.text(
        2,
        80,
        "Important Point"
    )

Syntax:

    plt.text(
        x_position,
        y_position,
        "text"
    )

---

# 36. annotate()

Used to add an annotation to a specific point.

    plt.annotate(
        "Highest",
        xy=(5, 95),
        xytext=(4, 80),
        arrowprops={
            "arrowstyle": "->"
        }
    )

---

# 37. Color

Matplotlib allows customization of plot colors.

Example:

    plt.plot(
        x,
        y,
        color="green"
    )

You can also use shorthand color codes:

    "r" → red
    "g" → green
    "b" → blue
    "k" → black
    "m" → magenta
    "c" → cyan
    "y" → yellow

---

# 38. Alpha

`alpha` controls transparency.

Example:

    plt.scatter(
        x,
        y,
        alpha=0.5
    )

Values generally range from:

    0 → transparent
    1 → fully opaque

---

# 39. Subplots

Subplots allow multiple plots in one figure.

Example:

    fig, axes = plt.subplots(
        2,
        2
    )

This creates:

    2 rows
    2 columns

Total:

    4 plots

---

# 40. Basic Subplot Example

    fig, axes = plt.subplots(
        2,
        1
    )

    axes[0].plot(
        x,
        y
    )

    axes[1].bar(
        x,
        y
    )

    plt.show()

---

# 41. One Row Multiple Plots

    fig, axes = plt.subplots(
        1,
        2
    )

    axes[0].plot(
        x,
        y
    )

    axes[1].bar(
        x,
        y
    )

    plt.show()

---

# 42. Figure and Axes

Modern Matplotlib commonly uses the object-oriented style:

    fig, ax = plt.subplots()

    ax.plot(
        x,
        y
    )

    ax.set_title(
        "Sales"
    )

    ax.set_xlabel(
        "Month"
    )

    ax.set_ylabel(
        "Sales"
    )

    plt.show()

Here:

    fig → entire figure
    ax  → plotting area / axes

---

# 43. pyplot vs Object-Oriented Style

Simple pyplot style:

    plt.plot(x, y)
    plt.title("Graph")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

Object-oriented style:

    fig, ax = plt.subplots()

    ax.plot(x, y)
    ax.set_title("Graph")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    plt.show()

For simple plots, both are fine.

For complex visualizations and multiple subplots, the object-oriented style is often easier to manage.

---

# 44. Multiple Axes

Example:

    fig, ax = plt.subplots()

    ax.plot(
        x,
        y,
        label="Sales"
    )

    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")
    ax.set_title("Monthly Sales")

    ax.legend()

    plt.show()

---

# 45. tight_layout()

Automatically adjusts spacing.

    plt.tight_layout()

Useful when:

- Labels overlap
- Titles overlap
- Multiple subplots are present

Example:

    fig, axes = plt.subplots(
        2,
        2
    )

    plt.tight_layout()

---

# 46. Saving a Plot

Use:

    plt.savefig(
        "plot.png"
    )

Example:

    plt.plot(
        x,
        y
    )

    plt.title(
        "Sales"
    )

    plt.savefig(
        "sales.png"
    )

    plt.show()

---

# 47. Saving as PDF

    plt.savefig(
        "plot.pdf"
    )

Matplotlib supports several output formats depending on the environment and backend.

---

# 48. DPI

DPI means:

    Dots Per Inch

Higher DPI generally produces a higher-resolution raster image.

Example:

    plt.savefig(
        "plot.png",
        dpi=300
    )

---

# 49. Figure Object

Create a figure manually:

    fig = plt.figure(
        figsize=(10, 6)
    )

Then add plotting axes as needed.

For most everyday plots:

    fig, ax = plt.subplots()

is more convenient.

---

# 50. Clear Plot

Clear the current axes:

    plt.cla()

Clear the current figure:

    plt.clf()

Close a figure:

    plt.close()

---

# 51. Multiple Figures

You can create multiple figures.

    plt.figure()

    plt.plot(
        x,
        y
    )

    plt.figure()

    plt.bar(
        x,
        y
    )

    plt.show()

---

# 52. Log Scale

Sometimes data contains very large ranges.

Use logarithmic scale:

    plt.yscale("log")

Or:

    plt.xscale("log")

Useful for:

- Exponential growth
- Large numerical ranges
- Scientific data
- Certain ML/data analysis visualizations

---

# 53. Horizontal Reference Line

Use `axhline()`:

    plt.axhline(
        y=50
    )

Example:

    plt.axhline(
        y=50,
        linestyle="--"
    )

Useful for showing:

- Average
- Target
- Threshold
- Passing marks

---

# 54. Vertical Reference Line

Use `axvline()`:

    plt.axvline(
        x=5
    )

Useful for marking a specific X value.

---

# 55. Fill Between

Highlight the area between two curves:

    plt.fill_between(
        x,
        y1,
        y2
    )

Example:

    x = [1, 2, 3, 4, 5]

    y1 = [10, 20, 15, 25, 30]
    y2 = [5, 10, 8, 15, 20]

    plt.plot(x, y1)
    plt.plot(x, y2)

    plt.fill_between(
        x,
        y1,
        y2,
        alpha=0.3
    )

    plt.show()

---

# 56. Error Bars

Error bars show uncertainty or variation.

Example:

    x = [1, 2, 3, 4]
    y = [10, 20, 15, 25]
    error = [1, 2, 1, 3]

    plt.errorbar(
        x,
        y,
        yerr=error,
        fmt="o-"
    )

    plt.show()

---

# 57. Hist2D

For two-dimensional distributions:

    plt.hist2d(
        x,
        y,
        bins=20
    )

Useful for understanding the density of two numerical variables.

---

# 58. Colorbars

Some plots use a color scale to represent an additional variable.

Example:

    plt.scatter(
        x,
        y,
        c=values
    )

    plt.colorbar()

---

# 59. Labels and Titles

A good graph should normally have:

- Clear title
- X-axis label
- Y-axis label
- Legend when multiple datasets exist
- Appropriate scale
- Readable tick labels

Example:

    plt.plot(
        months,
        sales,
        label="Sales"
    )

    plt.title(
        "Monthly Sales"
    )

    plt.xlabel(
        "Month"
    )

    plt.ylabel(
        "Sales"
    )

    plt.legend()

    plt.grid()

    plt.show()

---

# 60. Choosing the Right Plot

| Data/Goal | Recommended Plot |
|---|---|
| Trend over time | Line plot |
| Compare categories | Bar chart |
| Distribution of numerical data | Histogram |
| Relationship between two variables | Scatter plot |
| Proportion of categories | Pie chart |
| Distribution + outliers | Box plot |
| Two or more plots together | Subplots |
| Density of two numerical variables | Hist2D |

---

# 61. Matplotlib with NumPy

NumPy is commonly used to generate numerical data.

Example:

    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(
        0,
        10,
        100
    )

    y = x ** 2

    plt.plot(
        x,
        y
    )

    plt.xlabel("X")
    plt.ylabel("X²")
    plt.title("Square Function")

    plt.show()

---

# 62. Matplotlib with Pandas

Pandas DataFrames can also be plotted.

Example:

    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.DataFrame({
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr"
        ],
        "Sales": [
            100,
            150,
            130,
            180
        ]
    })

    plt.plot(
        df["Month"],
        df["Sales"]
    )

    plt.show()

---

# 63. Pandas Plotting

Pandas also provides a plotting interface.

Example:

    df.plot(
        x="Month",
        y="Sales"
    )

    plt.show()

But understanding Matplotlib directly is important because it provides much more control over visualization.

---

# 64. Matplotlib with Machine Learning

Matplotlib is heavily used in Machine Learning for:

- Data exploration
- Understanding distributions
- Feature analysis
- Model evaluation
- Training curves
- Comparing predictions
- Error analysis
- Visualizing datasets

Example:

    plt.scatter(
        actual,
        predicted
    )

This can help visualize model performance.

---

# 65. Plotting Model Training

For models that track training history:

    plt.plot(
        history["loss"],
        label="Training Loss"
    )

    plt.plot(
        history["val_loss"],
        label="Validation Loss"
    )

    plt.xlabel("Epoch")
    plt.ylabel("Loss")

    plt.legend()

    plt.show()

This is especially common in Deep Learning.

---

# 66. Common Matplotlib Mistakes

## Mistake 1

Forgetting:

    plt.show()

In many scripts, this is needed to display the figure.

---

## Mistake 2

Forgetting labels.

Bad:

    plt.plot(x, y)

Better:

    plt.plot(x, y)
    plt.xlabel("Time")
    plt.ylabel("Sales")
    plt.title("Sales Trend")

---

## Mistake 3

Using the wrong chart.

For example:

- Trend → Line
- Categories → Bar
- Distribution → Histogram
- Relationship → Scatter

---

## Mistake 4

Overloading the graph.

Too many:

- Colors
- Labels
- Lines
- Text
- Categories

can make a graph difficult to understand.

---

## Mistake 5

Forgetting legend when multiple datasets are plotted.

Use:

    plt.legend()

---

# 67. Basic Visualization Template

    import matplotlib.pyplot as plt

    # Data
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 30, 25]

    # Figure
    plt.figure(
        figsize=(8, 5)
    )

    # Plot
    plt.plot(
        x,
        y,
        marker="o",
        label="Data"
    )

    # Labels
    plt.xlabel("X")
    plt.ylabel("Y")

    # Title
    plt.title("Example Plot")

    # Grid
    plt.grid()

    # Legend
    plt.legend()

    # Layout
    plt.tight_layout()

    # Display
    plt.show()

---

# 68. Basic EDA Visualization Workflow

After loading data with Pandas:

    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv(
        "data.csv"
    )

First understand the dataset:

    print(df.head())
    print(df.shape)
    print(df.info())
    print(df.describe())

Then visualize:

    df["Age"].plot(
        kind="hist"
    )

    plt.show()

---

# 69. Example — Student Marks

    students = [
        "Aman",
        "Rahul",
        "Tanishk",
        "Rohit"
    ]

    marks = [
        75,
        82,
        95,
        68
    ]

    plt.bar(
        students,
        marks
    )

    plt.xlabel(
        "Students"
    )

    plt.ylabel(
        "Marks"
    )

    plt.title(
        "Student Performance"
    )

    plt.show()

---

# 70. Example — Study Hours vs Marks

    study_hours = [
        1,
        2,
        3,
        4,
        5,
        6
    ]

    marks = [
        40,
        45,
        55,
        65,
        75,
        88
    ]

    plt.scatter(
        study_hours,
        marks
    )

    plt.xlabel(
        "Study Hours"
    )

    plt.ylabel(
        "Marks"
    )

    plt.title(
        "Study Hours vs Marks"
    )

    plt.show()

---

# 71. Practice Tasks

Practice these:

1. Create a line plot of daily temperatures.

2. Create a bar chart of marks in five subjects.

3. Create a horizontal bar chart of programming languages.

4. Create a histogram of 100 random marks.

5. Create a scatter plot of study hours vs marks.

6. Create a pie chart showing time spent on different activities.

7. Create a box plot of student marks.

8. Plot two lines on the same graph.

9. Add title, X-label, Y-label, and legend.

10. Add grid lines.

11. Change line style.

12. Add markers.

13. Change figure size.

14. Create 2×2 subplots.

15. Save a graph as PNG.

16. Create a graph using Pandas DataFrame.

17. Create a graph using NumPy arrays.

18. Visualize a dataset from a CSV file.

19. Find and visualize an outlier.

20. Create an EDA report using Pandas + Matplotlib.

---

# 72. Mini Project — Student Performance Visualization

Create a dataset:

    students = [
        "Aman",
        "Rahul",
        "Tanishk",
        "Rohit",
        "Priya"
    ]

    marks = [
        75,
        82,
        95,
        68,
        88
    ]

Create:

## Plot 1 — Bar Chart

Compare student marks.

## Plot 2 — Histogram

Show marks distribution.

## Plot 3 — Sorted Bar Chart

Show students from highest to lowest marks.

## Plot 4 — Average Line

Add a horizontal line showing average marks.

Example:

    average = sum(marks) / len(marks)

    plt.axhline(
        y=average,
        linestyle="--",
        label="Average"
    )

---

# 73. Mini EDA Project

Use a real CSV dataset.

Workflow:

    Load Dataset
         ↓
    Pandas
         ↓
    Understand Data
         ↓
    Clean Data
         ↓
    Select Numerical Columns
         ↓
    Create Histograms
         ↓
    Create Box Plots
         ↓
    Create Scatter Plots
         ↓
    Analyze Relationships
         ↓
    Write Conclusions

---

# 74. Matplotlib + NumPy + Pandas

These three libraries work together very well.

    NumPy
       ↓
    Numerical Operations
       ↓
    Pandas
       ↓
    Data Cleaning + Analysis
       ↓
    Matplotlib
       ↓
    Visualization

Example:

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    data = {
        "Hours": [1, 2, 3, 4, 5],
        "Marks": [40, 50, 60, 75, 90]
    }

    df = pd.DataFrame(data)

    plt.scatter(
        df["Hours"],
        df["Marks"]
    )

    plt.xlabel(
        "Study Hours"
    )

    plt.ylabel(
        "Marks"
    )

    plt.title(
        "Study Hours vs Marks"
    )

    plt.show()

---

# 75. Important Functions — Quick Revision

## Basic

    plt.plot()
    plt.show()
    plt.figure()

## Labels

    plt.xlabel()
    plt.ylabel()
    plt.title()
    plt.legend()

## Grid

    plt.grid()

## Line

    plt.plot()

## Bar

    plt.bar()
    plt.barh()

## Distribution

    plt.hist()
    plt.boxplot()

## Relationship

    plt.scatter()

## Proportion

    plt.pie()

## Subplots

    plt.subplots()

## Axis

    plt.xlim()
    plt.ylim()
    plt.xticks()
    plt.yticks()

## Annotation

    plt.text()
    plt.annotate()

## Reference Lines

    plt.axhline()
    plt.axvline()

## Saving

    plt.savefig()

## Layout

    plt.tight_layout()

---

# 76. Important Concepts to Master

Before moving forward, understand:

- Figure
- Axes
- Axis
- Line plot
- Bar chart
- Histogram
- Scatter plot
- Pie chart
- Box plot
- Subplots
- Labels
- Titles
- Legends
- Grid
- Markers
- Line styles
- Figure size
- Axis limits
- Annotations
- Saving figures
- Object-oriented plotting

---

# 77. Matplotlib Learning Roadmap

Follow this order:

    1. Matplotlib Introduction
            ↓
    2. pyplot
            ↓
    3. Line Plot
            ↓
    4. Labels + Title
            ↓
    5. Markers + Line Styles
            ↓
    6. Multiple Lines
            ↓
    7. Bar Chart
            ↓
    8. Histogram
            ↓
    9. Scatter Plot
            ↓
    10. Pie Chart
            ↓
    11. Box Plot
            ↓
    12. Figure Size
            ↓
    13. Grid + Legend
            ↓
    14. Subplots
            ↓
    15. Figure + Axes
            ↓
    16. Customization
            ↓
    17. Saving Figures
            ↓
    18. Matplotlib + NumPy
            ↓
    19. Matplotlib + Pandas
            ↓
    20. EDA Visualization
            ↓
    21. ML Visualization

---

# 78. Final Goal

After learning Matplotlib, you should be able to:

- Create different types of charts
- Choose the correct visualization for a problem
- Customize plots
- Compare multiple datasets
- Visualize distributions
- Visualize relationships
- Identify possible outliers
- Create subplots
- Save visualizations
- Use NumPy with Matplotlib
- Use Pandas with Matplotlib
- Perform visualization during EDA
- Visualize Machine Learning results

---

# ⭐ Recommended Next Step

After Matplotlib:

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

> NumPy → Numerical Computing
>
> Pandas → Data Manipulation + Analysis
>
> Matplotlib → Visualization
>
> Seaborn → Statistical Visualization
>
> Scikit-Learn → Machine Learning