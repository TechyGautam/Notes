# NumPy Notes

> NumPy = Numerical Python
>
> NumPy is a Python library used for numerical computing, scientific computing, arrays, matrices, mathematical operations, and efficient data processing.

---

# 1. What is NumPy?

NumPy stands for Numerical Python.

It is one of the most important Python libraries for:

- Numerical computations
- Working with arrays
- Mathematical operations
- Linear algebra
- Statistics
- Random number generation
- Data manipulation
- Scientific computing
- Machine Learning

Import NumPy:

    import numpy as np

`np` is the commonly used alias for NumPy.

---

# 2. Why NumPy?

Python lists are useful, but NumPy arrays are designed for numerical operations and can be much more efficient for large numerical datasets.

Example using Python list:

    numbers = [1, 2, 3, 4, 5]

    result = [x * 2 for x in numbers]

Using NumPy:

    import numpy as np

    numbers = np.array([1, 2, 3, 4, 5])

    result = numbers * 2

Output:

    [ 2  4  6  8 10]

NumPy allows vectorized operations without manually writing a loop.

---

# 3. NumPy Array

The main object in NumPy is the `ndarray`.

`ndarray` means N-dimensional array.

Example:

    import numpy as np

    arr = np.array([1, 2, 3, 4, 5])

    print(arr)

Output:

    [1 2 3 4 5]

---

# 4. Python List vs NumPy Array

Python list:

    numbers = [1, 2, 3, 4]

NumPy array:

    numbers = np.array([1, 2, 3, 4])

Important differences:

| Python List | NumPy Array |
|---|---|
| General-purpose | Numerical computing |
| Can contain different data types | Usually works with a common dtype |
| Slower for large numerical operations | Faster for numerical operations |
| Supports general Python objects | Optimized for numerical data |
| Less mathematical functionality | Many built-in mathematical operations |

---

# 5. Creating NumPy Arrays

## From Python List

    arr = np.array([1, 2, 3, 4])

## From Tuple

    arr = np.array((1, 2, 3, 4))

## 2D Array

    arr = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

## 3D Array

    arr = np.array([
        [
            [1, 2],
            [3, 4]
        ],
        [
            [5, 6],
            [7, 8]
        ]
    ])

---

# 6. Dimensions of an Array

NumPy arrays can have different dimensions.

## 0D Array

A single value:

    arr = np.array(5)

## 1D Array

A single row of values:

    arr = np.array([1, 2, 3, 4])

## 2D Array

Rows and columns:

    arr = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

## 3D Array

Collection of 2D arrays:

    arr = np.array([
        [
            [1, 2],
            [3, 4]
        ],
        [
            [5, 6],
            [7, 8]
        ]
    ])

---

# 7. ndim

`ndim` returns the number of dimensions.

    arr = np.array([1, 2, 3, 4])

    print(arr.ndim)

Output:

    1

Example:

    arr = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    print(arr.ndim)

Output:

    2

---

# 8. shape

`shape` returns the size of each dimension.

    arr = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    print(arr.shape)

Output:

    (2, 3)

Meaning:

    2 rows
    3 columns

For a 1D array:

    arr = np.array([1, 2, 3, 4, 5])

    print(arr.shape)

Output:

    (5,)

---

# 9. size

`size` returns the total number of elements.

    arr = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    print(arr.size)

Output:

    6

---

# 10. dtype

`dtype` tells us the data type of array elements.

    arr = np.array([1, 2, 3])

    print(arr.dtype)

Example output:

    int64

Another example:

    arr = np.array([1.2, 2.5, 3.7])

    print(arr.dtype)

Output may be:

    float64

---

# 11. itemsize

`itemsize` returns the number of bytes used by one element.

    arr = np.array([1, 2, 3])

    print(arr.itemsize)

The exact result depends on the array's dtype.

---

# 12. Creating Arrays with Specific Data Types

    arr = np.array([1, 2, 3], dtype=float)

    print(arr)

Output:

    [1. 2. 3.]

Another example:

    arr = np.array([1.2, 2.8, 3.5], dtype=int)

Output:

    [1 2 3]

Be careful because converting float to int removes the decimal part.

---

# 13. np.zeros()

Creates an array filled with zeros.

    arr = np.zeros(5)

Output:

    [0. 0. 0. 0. 0.]

2D array:

    arr = np.zeros((2, 3))

Output:

    [
        [0. 0. 0.]
        [0. 0. 0.]
    ]

---

# 14. np.ones()

Creates an array filled with ones.

    arr = np.ones(5)

Output:

    [1. 1. 1. 1. 1.]

2D:

    arr = np.ones((2, 3))

---

# 15. np.full()

Creates an array filled with a specific value.

    arr = np.full(5, 7)

Output:

    [7 7 7 7 7]

2D:

    arr = np.full((2, 3), 10)

---

# 16. np.empty()

Creates an array without initializing its values to a specific number.

    arr = np.empty(5)

The values are not guaranteed to be zero.

The contents depend on the existing memory state.

---

# 17. np.arange()

Creates evenly spaced values within a range.

    arr = np.arange(1, 10)

Output:

    [1 2 3 4 5 6 7 8 9]

Syntax:

    np.arange(start, stop, step)

Example:

    arr = np.arange(0, 10, 2)

Output:

    [0 2 4 6 8]

Important:

The `stop` value is generally excluded.

---

# 18. np.linspace()

Creates evenly spaced values between two numbers.

    arr = np.linspace(0, 10, 5)

Output:

    [0.  2.5 5.  7.5 10.]

Syntax:

    np.linspace(start, stop, number_of_values)

Unlike `arange()`, the number of values is specified.

---

# 19. np.eye()

Creates an identity matrix.

    arr = np.eye(3)

Output:

    [
        [1. 0. 0.]
        [0. 1. 0.]
        [0. 0. 1.]
    ]

---

# 20. Random Numbers

NumPy provides random number generation through `np.random`.

Example:

    np.random.rand()

Generates a random floating-point number in the range [0, 1).

---

# 21. np.random.rand()

Generate random values from a uniform distribution between 0 and 1.

    arr = np.random.rand(5)

Example output:

    [0.21 0.75 0.43 0.11 0.89]

2D:

    arr = np.random.rand(2, 3)

---

# 22. np.random.randint()

Generates random integers.

    arr = np.random.randint(1, 10, 5)

Example output:

    [4 8 2 9 1]

Syntax:

    np.random.randint(low, high, size)

The `high` value is excluded.

---

# 23. Random Seed

A seed makes random results reproducible.

    np.random.seed(42)

    print(np.random.randint(1, 10, 5))

Running the same code with the same seed produces the same sequence.

---

# 24. Array Indexing

Indexing starts from 0.

    arr = np.array([10, 20, 30, 40, 50])

    print(arr[0])

Output:

    10

    print(arr[2])

Output:

    30

---

# 25. Negative Indexing

Negative indexes start from the end.

    arr = np.array([10, 20, 30, 40, 50])

    print(arr[-1])

Output:

    50

    print(arr[-2])

Output:

    40

---

# 26. 2D Array Indexing

Example:

    arr = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])

Access row 0, column 1:

    print(arr[0, 1])

Output:

    20

Access row 1, column 2:

    print(arr[1, 2])

Output:

    60

---

# 27. Slicing

Slicing extracts a portion of an array.

    arr = np.array([10, 20, 30, 40, 50])

    print(arr[1:4])

Output:

    [20 30 40]

Syntax:

    arr[start:stop:step]

The stop index is excluded.

---

# 28. Slicing with Step

    arr = np.array([10, 20, 30, 40, 50])

    print(arr[::2])

Output:

    [10 30 50]

Reverse:

    print(arr[::-1])

Output:

    [50 40 30 20 10]

---

# 29. 2D Array Slicing

    arr = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

First two rows:

    arr[:2]

First two columns:

    arr[:, :2]

Rows 1 and 2, columns 1 and 2:

    arr[1:3, 1:3]

---

# 30. Changing Array Elements

    arr = np.array([10, 20, 30, 40])

    arr[1] = 100

Now:

    [10 100 30 40]

2D:

    arr[0, 1] = 500

---

# 31. Array Arithmetic

NumPy supports element-wise arithmetic.

    arr = np.array([1, 2, 3, 4])

Addition:

    arr + 10

Output:

    [11 12 13 14]

Subtraction:

    arr - 10

Output:

    [-9 -8 -7 -6]

Multiplication:

    arr * 2

Output:

    [2 4 6 8]

Division:

    arr / 2

Output:

    [0.5 1.  1.5 2. ]

Power:

    arr ** 2

Output:

    [1 4 9 16]

---

# 32. Operations Between Arrays

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

Addition:

    a + b

Output:

    [5 7 9]

Subtraction:

    a - b

Output:

    [-3 -3 -3]

Multiplication:

    a * b

Output:

    [4 10 18]

Division:

    a / b

Output:

    [0.25 0.4  0.5 ]

These are element-wise operations.

---

# 33. Matrix Multiplication

Element-wise multiplication:

    a * b

Matrix multiplication:

    a @ b

or:

    np.matmul(a, b)

For 2D matrices:

    A = np.array([
        [1, 2],
        [3, 4]
    ])

    B = np.array([
        [5, 6],
        [7, 8]
    ])

    result = A @ B

---

# 34. Comparison Operations

NumPy supports element-wise comparisons.

    arr = np.array([10, 20, 30, 40])

    arr > 20

Output:

    [False False True True]

Other examples:

    arr == 20
    arr != 20
    arr >= 20
    arr < 30

---

# 35. Boolean Indexing

Boolean conditions can be used to filter arrays.

    arr = np.array([10, 20, 30, 40, 50])

    arr[arr > 25]

Output:

    [30 40 50]

Another example:

    arr[arr % 2 == 0]

Returns even numbers.

---

# 36. np.where()

`np.where()` can be used for conditional selection.

    arr = np.array([10, 20, 30, 40])

    result = np.where(arr > 25, 1, 0)

Output:

    [0 0 1 1]

Meaning:

- If condition is True → 1
- If condition is False → 0

---

# 37. np.argmax()

Returns the index of the maximum value.

    arr = np.array([10, 50, 20, 40])

    np.argmax(arr)

Output:

    1

Because 50 is at index 1.

---

# 38. np.argmin()

Returns the index of the minimum value.

    arr = np.array([10, 50, 20, 40])

    np.argmin(arr)

Output:

    0

---

# 39. np.max()

Returns the maximum value.

    arr = np.array([10, 20, 30, 40])

    np.max(arr)

Output:

    40

---

# 40. np.min()

Returns the minimum value.

    np.min(arr)

---

# 41. np.sum()

Returns the sum of elements.

    arr = np.array([1, 2, 3, 4])

    np.sum(arr)

Output:

    10

---

# 42. np.mean()

Returns the arithmetic mean.

    arr = np.array([10, 20, 30, 40])

    np.mean(arr)

Output:

    25.0

Formula:

    Mean = Sum of values / Number of values

---

# 43. np.median()

Returns the median.

    arr = np.array([10, 20, 30, 40, 50])

    np.median(arr)

Output:

    30.0

For an even number of values, NumPy uses the average of the two middle values.

---

# 44. np.std()

Returns standard deviation.

    arr = np.array([10, 20, 30, 40])

    np.std(arr)

Standard deviation measures how spread out values are around the mean.

---

# 45. np.var()

Returns variance.

    arr = np.array([10, 20, 30, 40])

    np.var(arr)

Relationship:

    Variance = Standard Deviation²

---

# 46. np.prod()

Returns the product of all elements.

    arr = np.array([1, 2, 3, 4])

    np.prod(arr)

Output:

    24

---

# 47. np.cumsum()

Returns cumulative sum.

    arr = np.array([1, 2, 3, 4])

    np.cumsum(arr)

Output:

    [1 3 6 10]

---

# 48. np.cumprod()

Returns cumulative product.

    arr = np.array([1, 2, 3, 4])

    np.cumprod(arr)

Output:

    [1 2 6 24]

---

# 49. Axis

Axis is extremely important in NumPy.

For a 2D array:

    arr = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

There are two axes:

    axis=0 → down the rows
    axis=1 → across the columns

Think:

    axis=0 → operate vertically
    axis=1 → operate horizontally

---

# 50. Sum Along Axis

    arr = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

Sum along axis 0:

    np.sum(arr, axis=0)

Output:

    [5 7 9]

Sum along axis 1:

    np.sum(arr, axis=1)

Output:

    [6 15]

---

# 51. Mean Along Axis

    np.mean(arr, axis=0)

Column-wise mean.

    np.mean(arr, axis=1)

Row-wise mean.

---

# 52. Reshape

`reshape()` changes the shape of an array without changing its data.

    arr = np.array([1, 2, 3, 4, 5, 6])

    new_arr = arr.reshape(2, 3)

Result:

    [
        [1 2 3]
        [4 5 6]
    ]

The total number of elements must remain the same.

6 elements:

    2 × 3 = 6

---

# 53. reshape(-1)

NumPy can automatically calculate one dimension.

    arr = np.array([1, 2, 3, 4, 5, 6])

    arr.reshape(2, -1)

Result:

    [
        [1 2 3]
        [4 5 6]
    ]

---

# 54. Flatten

`flatten()` converts an array into a 1D copy.

    arr = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    flat = arr.flatten()

Output:

    [1 2 3 4 5 6]

---

# 55. Ravel

`ravel()` also converts an array into 1D.

    arr.ravel()

Main difference:

- `flatten()` returns a copy
- `ravel()` generally returns a view when possible

---

# 56. Transpose

Transpose swaps rows and columns.

    arr = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    arr.T

Result:

    [
        [1 4]
        [2 5]
        [3 6]
    ]

---

# 57. Resize

`resize()` changes the shape of an array.

    arr = np.array([1, 2, 3, 4, 5, 6])

    arr.resize(2, 3)

Unlike `reshape()`, `resize()` can change the number of elements and modifies the array itself.

---

# 58. Concatenate

Combines arrays.

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    np.concatenate((a, b))

Output:

    [1 2 3 4 5 6]

---

# 59. Stack

Stacks arrays along a new axis.

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    np.stack((a, b))

Output:

    [
        [1 2 3]
        [4 5 6]
    ]

---

# 60. Vertical Stack

`vstack()` stacks arrays vertically.

    np.vstack((a, b))

Output:

    [
        [1 2 3]
        [4 5 6]
    ]

---

# 61. Horizontal Stack

`hstack()` stacks arrays horizontally.

    np.hstack((a, b))

Output:

    [1 2 3 4 5 6]

---

# 62. Split

Splits an array into multiple arrays.

    arr = np.array([1, 2, 3, 4, 5, 6])

    np.split(arr, 3)

Result:

    [array([1, 2]), array([3, 4]), array([5, 6])]

The split must be compatible with the array size.

---

# 63. Sorting

Use `np.sort()`.

    arr = np.array([40, 10, 30, 20])

    np.sort(arr)

Output:

    [10 20 30 40]

Descending:

    np.sort(arr)[::-1]

---

# 64. Searching

`np.where()` can find indexes where a condition is true.

    arr = np.array([10, 20, 30, 20, 40])

    np.where(arr == 20)

This returns the indexes where the condition is true.

---

# 65. Unique Values

Use `np.unique()`.

    arr = np.array([1, 2, 2, 3, 3, 3, 4])

    np.unique(arr)

Output:

    [1 2 3 4]

---

# 66. Counting Unique Values

    values, counts = np.unique(
        arr,
        return_counts=True
    )

This returns:

- Unique values
- Number of occurrences

---

# 67. Copy vs View

This is an important NumPy concept.

## Copy

Creates an independent array.

    arr = np.array([1, 2, 3])

    copy_arr = arr.copy()

Changes to `copy_arr` do not normally affect `arr`.

## View

A view can share the same underlying data.

    view_arr = arr.view()

Changes to the view can affect the original array depending on the operation.

---

# 68. Broadcasting

Broadcasting allows NumPy to perform operations on arrays with compatible shapes.

Example:

    arr = np.array([1, 2, 3])

    arr + 10

Output:

    [11 12 13]

Here, NumPy effectively applies 10 to every element.

2D example:

    arr = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    arr + np.array([10, 20, 30])

Output:

    [
        [11 22 33]
        [14 25 36]
    ]

---

# 69. Broadcasting Rules

Broadcasting generally works when dimensions are compatible.

Starting from the last dimension:

Two dimensions are compatible when:

1. They are equal
2. One of them is 1
3. A missing dimension is treated as 1

Example:

    (2, 3)
    (3,)

These are compatible.

But:

    (2, 3)
    (2,)

are not generally compatible for element-wise broadcasting.

---

# 70. Mathematical Functions

NumPy provides many mathematical functions.

Examples:

    np.sqrt(arr)
    np.square(arr)
    np.abs(arr)
    np.exp(arr)
    np.log(arr)
    np.log10(arr)
    np.sin(arr)
    np.cos(arr)
    np.tan(arr)

Example:

    arr = np.array([1, 4, 9])

    np.sqrt(arr)

Output:

    [1. 2. 3.]

---

# 71. Rounding Functions

## np.round()

    arr = np.array([1.234, 2.567, 3.891])

    np.round(arr, 2)

Example output:

    [1.23 2.57 3.89]

## np.floor()

Rounds down.

    np.floor(3.8)

Output:

    3.

## np.ceil()

Rounds up.

    np.ceil(3.2)

Output:

    4.

---

# 72. Handling NaN

NaN means "Not a Number".

Example:

    arr = np.array([10, np.nan, 30])

Check NaN:

    np.isnan(arr)

Output:

    [False True False]

---

# 73. Handling Infinity

NumPy provides:

    np.inf
    np.nan

Example:

    arr = np.array([1, 2, np.inf])

Check infinity:

    np.isinf(arr)

---

# 74. NaN-Aware Functions

Normal mean:

    np.mean(arr)

If NaN is present, the result may become NaN.

Use:

    np.nanmean(arr)

Similarly:

    np.nansum(arr)
    np.nanmin(arr)
    np.nanmax(arr)
    np.nanstd(arr)

These ignore NaN values where appropriate.

---

# 75. Linear Algebra

NumPy provides linear algebra functionality through `np.linalg`.

Common functions:

    np.linalg.inv()
    np.linalg.det()
    np.linalg.eig()
    np.linalg.solve()
    np.linalg.norm()

Example:

    A = np.array([
        [1, 2],
        [3, 4]
    ])

    np.linalg.det(A)

---

# 76. Dot Product

For vectors:

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    np.dot(a, b)

Calculation:

    1×4 + 2×5 + 3×6
    = 4 + 10 + 18
    = 32

---

# 77. Matrix Inverse

    A = np.array([
        [1, 2],
        [3, 4]
    ])

    inverse = np.linalg.inv(A)

Matrix inverse is important in:

- Linear algebra
- Machine Learning
- Statistics
- Scientific computing

---

# 78. Determinant

    A = np.array([
        [1, 2],
        [3, 4]
    ])

    np.linalg.det(A)

For a 2×2 matrix:

    |a b|
    |c d|

Determinant:

    ad - bc

---

# 79. Saving NumPy Arrays

Save a single NumPy array:

    np.save("data.npy", arr)

Load it:

    arr = np.load("data.npy")

---

# 80. Saving Multiple Arrays

    np.savez(
        "data.npz",
        array1=a,
        array2=b
    )

Load:

    data = np.load("data.npz")

---

# 81. NumPy and CSV

Save array to CSV:

    np.savetxt(
        "data.csv",
        arr,
        delimiter=","
    )

Load CSV:

    arr = np.loadtxt(
        "data.csv",
        delimiter=","
    )

For more complex CSV files, Pandas is often more convenient.

---

# 82. NumPy Performance

NumPy is fast because:

- Arrays use efficient memory layouts
- Operations are implemented in optimized compiled code
- Vectorization reduces Python-level loops
- Broadcasting avoids unnecessary manual loops

Example:

Python loop:

    result = []

    for x in numbers:
        result.append(x * 2)

NumPy:

    result = numbers * 2

The second approach is usually cleaner and often faster for numerical workloads.

---

# 83. Vectorization

Vectorization means performing operations on entire arrays instead of manually looping through individual elements.

Without vectorization:

    result = []

    for x in arr:
        result.append(x * 2)

With NumPy:

    result = arr * 2

Vectorization is one of the most important reasons NumPy is useful.

---

# 84. Useful NumPy Functions — Quick Revision

Array creation:

    np.array()
    np.zeros()
    np.ones()
    np.full()
    np.empty()
    np.arange()
    np.linspace()
    np.eye()

Array information:

    arr.ndim
    arr.shape
    arr.size
    arr.dtype
    arr.itemsize

Math:

    np.sum()
    np.mean()
    np.median()
    np.std()
    np.var()
    np.min()
    np.max()
    np.prod()

Array manipulation:

    reshape()
    flatten()
    ravel()
    transpose()
    concatenate()
    stack()
    vstack()
    hstack()
    split()

Searching:

    np.where()
    np.argmax()
    np.argmin()
    np.unique()

Math functions:

    np.sqrt()
    np.square()
    np.abs()
    np.exp()
    np.log()
    np.sin()
    np.cos()

Random:

    np.random.rand()
    np.random.randint()
    np.random.seed()

Linear algebra:

    np.dot()
    np.matmul()
    np.linalg.inv()
    np.linalg.det()
    np.linalg.solve()

---

# 85. NumPy in Machine Learning

NumPy is extremely important for Machine Learning.

It is used for:

- Numerical data
- Feature arrays
- Mathematical calculations
- Matrix operations
- Vector operations
- Data preprocessing
- Linear algebra
- Statistics
- Model calculations

Machine Learning data often looks like:

    X = np.array([
        [20, 50000],
        [25, 60000],
        [30, 80000]
    ])

Here:

- Rows = Samples
- Columns = Features

Example:

    X.shape

Output:

    (3, 2)

Meaning:

    3 samples
    2 features

---

# 86. NumPy with Pandas

Pandas is built on top of NumPy concepts and works closely with NumPy arrays.

Example:

    import numpy as np
    import pandas as pd

    data = np.array([
        [1, 20],
        [2, 30],
        [3, 40]
    ])

    df = pd.DataFrame(
        data,
        columns=["id", "age"]
    )

NumPy is mainly focused on numerical arrays.

Pandas is mainly focused on labeled tabular data.

---

# 87. NumPy Learning Roadmap

Follow this order:

    1. NumPy Introduction
            ↓
    2. np.array()
            ↓
    3. Dimensions
            ↓
    4. shape / size / ndim / dtype
            ↓
    5. Array Creation
            ↓
    6. Indexing
            ↓
    7. Slicing
            ↓
    8. Array Operations
            ↓
    9. Boolean Indexing
            ↓
    10. Mathematical Functions
            ↓
    11. Aggregation
            ↓
    12. Axis
            ↓
    13. Reshape
            ↓
    14. Stack / Split
            ↓
    15. Broadcasting
            ↓
    16. Copy vs View
            ↓
    17. Random
            ↓
    18. Linear Algebra
            ↓
    19. NumPy + Pandas
            ↓
    20. NumPy + Machine Learning

---

# 88. Practice Tasks

Practice these problems:

1. Create a NumPy array of numbers from 1 to 20.

2. Find the sum of all numbers.

3. Find the mean.

4. Find the maximum and minimum.

5. Find the index of the maximum value.

6. Extract all even numbers.

7. Extract all numbers greater than 10.

8. Reverse an array.

9. Create a 3×3 matrix.

10. Find row-wise sum.

11. Find column-wise sum.

12. Reshape a 1D array into a 2D array.

13. Find unique values.

14. Count unique values.

15. Generate 10 random integers.

16. Create a matrix and calculate its transpose.

17. Perform matrix multiplication.

18. Calculate the determinant of a matrix.

19. Calculate the inverse of a matrix.

20. Create a small dataset using NumPy and calculate basic statistics.

---

# 89. Mini Practice Project — Student Marks Analysis

Create:

    marks = np.array([
        [85, 90, 78],
        [70, 88, 92],
        [95, 91, 89],
        [60, 72, 68]
    ])

Rows represent students.

Columns represent subjects.

Practice:

- Total marks of each student
- Average marks of each student
- Highest marks
- Lowest marks
- Subject-wise average
- Student with highest average
- Students with average > 80

Useful functions:

    np.sum()
    np.mean()
    np.max()
    np.min()
    np.argmax()
    axis=0
    axis=1

---

# 90. Important Concepts to Master

Before moving from NumPy to Pandas, make sure you understand:

- ndarray
- Dimensions
- shape
- size
- ndim
- dtype
- Indexing
- Slicing
- Boolean indexing
- Vectorization
- Broadcasting
- Axis
- Reshape
- Flatten
- Ravel
- Transpose
- Copy vs View
- Aggregation
- Random numbers
- Basic linear algebra

---

# 91. Final Goal

After learning NumPy, you should be able to:

- Create and manipulate arrays
- Work with 1D, 2D and N-dimensional data
- Perform vectorized calculations
- Filter data efficiently
- Perform statistical calculations
- Understand axes
- Reshape datasets
- Perform matrix operations
- Work with random data
- Handle NaN and infinity
- Perform basic linear algebra
- Understand the numerical foundation of Machine Learning
- Work comfortably with NumPy before moving to Pandas

---

# ⭐ Next Step

After NumPy, the recommended learning order is:

    NumPy
       ↓
    Pandas
       ↓
    Matplotlib
       ↓
    Data Cleaning
       ↓
    Exploratory Data Analysis (EDA)
       ↓
    Scikit-Learn
       ↓
    Machine Learning

> NumPy gives you the foundation for numerical computing.
> Pandas builds on this foundation for real-world tabular data.