import numpy as np
import pandas as pd

# ==========================================
# 1. Creating a DataFrame from a Dictionary
# ==========================================
print("--- 1. Creating DataFrame ---")
"""
EXPLANATION: 
A DataFrame is like a digital spreadsheet or table with rows and columns. 
One of the easiest ways to create one is by using a Python dictionary, 
where the dictionary 'keys' become the column names, and the 'values' (lists) 
become the rows of data under those columns.
"""
data_dict = {"name": ["ali", "sara", "zara"], "marks": [20, 30, 80]}

df = pd.DataFrame(data_dict)
print(df)
print("\n")


# ==========================================
# 2. Exporting to CSV
# ==========================================
"""
EXPLANATION:
Once you have processed your data in Python, you usually want to save it. 
The `.to_csv()` function saves your DataFrame as a standard CSV file on your computer.
Setting `index=False` prevents Pandas from saving an extra, unnamed column for row numbers.
"""
df.to_csv("friend.csv", index=False)
df.to_csv("friend_2.csv", index=False)


# ==========================================
# 3. Viewing Data (Head, Tail, Describe)
# ==========================================
print("--- 3. Head, Tail, and Describe ---")
"""
EXPLANATION:
When dealing with thousands of rows, you can't look at all of them at once:
- `.head(n)` shows you the very first 'n' rows of your data.
- `.tail(n)` shows you the very last 'n' rows.
- `.describe()` automatically calculates statistical summaries like mean, median, min, and max for numeric columns.
"""
print("Top 2 rows:")
print(df.head(2))

print("\nBottom 1 row:")
print(df.tail(1))

print("\nStatistical Description:")
print(df.describe())
print("\n")


# ==========================================
# 4. Reading and Manipulating a CSV
# ==========================================
print("--- 4. Reading from CSV & Indexing ---")
"""
EXPLANATION:
To bring external data into Python, we use `pd.read_csv()`. 
Once loaded, you can extract specific data points using column and row positions (e.g., `df['column'][row]`).
You can also replace the default row numbers (0, 1, 2...) with your own custom labels by changing `df.index`.
"""
# Reading 'nabia.csv'
nabia = pd.read_csv("nabia.csv")
print("Original nabia DataFrame:")
print(nabia)

# Accessing specific column and index row
print("\nSalary at index 1:")
print(nabia["salary"][1])

# Modifying index labels to custom text strings
nabia.index = ["first", "2nd", "3rd", "4th"]
print("\nDataFrame with custom text index:")
print(nabia)
print("\n")


# ==========================================
# 5. Loc and Iloc (Indexing & Slicing)
# ==========================================
print("--- 5. Using loc and iloc ---")
"""
EXPLANATION:
Pandas uses two primary methods to extract or modify specific rows and columns:
- `.loc[]` is **label-based**: You look up data using the actual names of rows and columns (e.g., row 'first', column 'salary').
- `.iloc[]` is **integer-based**: You look up data using numerical positions (0, 1, 2...), completely ignoring text labels.
"""
# Using loc to update values based on string labels
nabia.loc["first", "salary"] = 5000
print("Updated 'first' row salary using .loc:")
print(nabia)

# Using iloc for integer-based slicing (rows 0 to 2, and all columns except the last one)
print("\nSlicing using .iloc[:3, :-1]:")
sliced_nabia = nabia.iloc[:3, :-1]
print(sliced_nabia)
print("\n")


# ==========================================
# 6. Working with Series & Random Numbers
# ==========================================
print("--- 6. Pandas Series & Random DataFrames ---")
"""
EXPLANATION:
- A Pandas **Series** is a single, one-dimensional column of data (like a list with index labels).
- We can combine Pandas with **NumPy** (`np.random.rand`) to auto-generate large datasets filled with 
  random numbers, which is incredibly useful for testing code and algorithms.
"""
# Creating a random Series with 20 items
ser = pd.Series(np.random.rand(20))
print("Random Pandas Series (First 5 items):")
print(ser.head())

# Creating a large 300x5 DataFrame with random floats
newdf = pd.DataFrame(np.random.rand(300, 5), index=np.arange(300))
print("\nLarge DataFrame Shape:", newdf.shape)
print(newdf.head())
print("\n")

# Checking structural attributes
print("Index Range Object:", newdf.index)
print("Columns Range Object:", newdf.columns)

# Converting a DataFrame to a raw Numpy Array (removes headers, leaves pure numbers)
print("\nConverting DataFrame to Numpy Array:")
print(newdf.to_numpy()[:2])  # displaying first two rows
print("\n")


# ==========================================
# 7. Sorting DataFrames
# ==========================================
print("--- 7. Sorting DataFrames ---")
"""
EXPLANATION:
You can rearrange the order of your columns or rows using `.sort_index()`.
Setting `axis=1` tells Pandas to sort the **columns** horizontally. 
Setting `ascending=False` sorts them in reverse order (e.g., column 4 down to column 0).
"""
sorted_df = newdf.sort_index(axis=1, ascending=False)
print("Columns sorted in descending order:")
print(sorted_df.head())
print("\n")


# ==========================================
# 8. Copying vs Views, Modifying Rows/Columns
# ==========================================
print("--- 8. Copying Data and Modifying Headers ---")
"""
EXPLANATION:
- If you write `df2 = df1`, making changes to `df2` might accidentally alter `df1`. Using `.copy()` creates a completely separate duplicate.
- You can overwrite column names instantly by passing a new list (like converting a string into a list of letters).
- `.drop()` removes unwanted columns (`axis=1`) or rows (`axis=0`).
- Whenever you delete rows, your row numbers will have gaps. `.reset_index(drop=True)` cleans up the row numbers back to a normal sequence (0, 1, 2...).
"""
# Explicitly copying to avoid data overriding/warnings
f3 = newdf.copy()

# Updating a specific cell value
newdf.loc[0, 0] = 345

# Renaming columns from integers (0,1,2..) to letters (A,B,C..)
newdf.columns = list("ABCDE")
print("DataFrame with renamed letter columns (A-E):")
print(newdf.head())
print("\n")

# Adding a new column dynamically
newdf.loc[0, "b"] = 1.0

# Dropping columns cleanly (axis=1)
newdf = newdf.drop("b", axis=1)

# Dropping rows cleanly (axis=0)
newdf = newdf.drop(0, axis=0)

# Resetting internal indexes back to sequential order starting from 0
newdf.reset_index(drop=True, inplace=True)
print("DataFrame after dropping and index resetting:")
print(newdf.head())
print("\n")


# ==========================================
# 9. Missing Values (NaN) & Filtering
# ==========================================
print("--- 9. Handling Missing & Null Values ---")
"""
EXPLANATION:
Real-world datasets are often messy and have missing information, represented as `NaN` (Not a Number) or `None`.
- `.isnull()` checks every cell and returns `True` if data is missing.
- `.notnull()` returns `True` if data is present.
- `.drop_duplicates()` cleans your data by wiping out identical repetitive entries.
- `.info()` prints a swift diagnostic summary of column datatypes and non-missing entry counts.
"""
# Checking for null values in a column
print("Is column 'B' null? (First 5 checks):")
print(newdf["B"].isnull().head())

# Dropping duplicate rows based on unique column rules
newdf.drop_duplicates(subset=["A"], keep="first")

# Summary info of the dataframe structure
print("\nDataFrame Structural Information:")
print(newdf.info())

# Counting how many times each unique value appears in a column
print("\nValue counts for column 'A' unique records:")
print(newdf["A"].value_counts(dropna=True).head())

# Checking where values are validly filled
print("\nDataFrame Not-Null check representation:")
print(newdf.notnull().head())
print("\n")


# ==========================================
# 10. Summary Functions & Matrix Statistics
# ==========================================
print("--- 10. Built-in Math & Correlation Functions ---")
"""
EXPLANATION:
Pandas makes calculating mathematical operations on structural tables extremely rapid:
- `.mean()` calculates averages.
- `.std()` evaluates standard deviation (data spread).
- `.corr()` builds a correlation matrix showing how changes in one column relate to changes in another column.
"""
# Mini 3x3 DataFrame with random integers between 1 and 100
matrix_df = pd.DataFrame(
    np.random.randint(1, 101, size=(3, 3)), index=np.arange(3)
)
print("Mini Integer Matrix DataFrame:")
print(matrix_df)

print("\nStatistical Calculations:")
print("Mean per column:\n", matrix_df.mean())
print("Correlation Matrix:\n", matrix_df.corr())
print("Element Counts per column:\n", matrix_df.count())
print("Minimum Values:\n", matrix_df.min())
print("Median Values:\n", matrix_df.median())
print("Standard Deviation:\n", matrix_df.std())
print("\n")


# ==========================================
# 11. Working with Excel files (.xlsx)
# ==========================================
print("--- 11. Excel Read & Write Operations ---")
"""
EXPLANATION:
Similar to CSVs, you can read and write to Microsoft Excel files using `pd.read_excel()` and `df.to_excel()`. 
You can target a specific tab in the workbook by using the `sheet_name` argument.
"""
# Reading explicitly from a specific worksheet
# data = pd.read_excel('data.xlsx', sheet_name='sheet1')

# Writing out the parsed structure back to excel sheets
# data.to_excel('data.xlsx', sheet_name='sheet1')
print("Excel commands successfully set up inside code blocks!")