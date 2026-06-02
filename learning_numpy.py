# =====================================================================
# Learning NumPy: Core Concepts, Operations, and Memory Efficiency
# =====================================================================

import sys
import numpy as np

# ---------------------------------------------------------------------
# 1. Array Creation and Basic Attributes
# ---------------------------------------------------------------------
print("--- 1. Array Creation & Attributes ---")

# Creating a basic 1D array
arr = np.array([1, 2, 3, 4])
print(f"Basic Array: {arr}")

# Creating an array filled with zeros of shape (rows, columns)
# np.zeros() defaults to float64 data type
zeros = np.zeros((2, 4))
print(f"\nZeros Array:\n{zeros}")
print(f"Shape of zeros: {zeros.shape}")  # Returns (rows, columns) -> (2, 4)
print(f"Size of zeros: {zeros.size}")  # Total number of elements -> 8
print(f"Data type of zeros: {zeros.dtype}")  # float64

# Creating a range of numbers from 0 up to (but excluding) 15
r = np.arange(15)
print(f"\nRange Array (np.arange): {r}")

# np.linspace(start, stop, number_of_elements)
# Creates evenly spaced numbers over a specified interval
l = np.linspace(1, 5, 4)
print(f"Linspace Array: {l}")

# np.empty() allocates memory without initializing values (contains random garbage data)
e = np.empty((4, 6))
print(f"\nEmpty Array (Garbage Values):\n{e}")

# np.empty_like() creates an uninitialized array with the same shape and type as a given array
empl = np.empty_like(l)
print(f"Empty Like Array shape: {empl.shape}")


# ---------------------------------------------------------------------
# 2. Reshaping and Flattening Arrays
# ---------------------------------------------------------------------
print("\n--- 2. Reshaping & Flattening ---")

r20 = np.arange(20)
# Reshaping a 1D array into a 2D array (5 rows, 4 columns)
# Note: Total elements must remain identical (5 * 4 = 20)
reshaped_arr = r20.reshape(5, 4)
print(f"Reshaped Array (5x4):\n{reshaped_arr}")

# .ravel() flattens a multi-dimensional array back into a 1D array
flattened = reshaped_arr.ravel()
print(f"Flattened back with ravel(): {flattened}")


# ---------------------------------------------------------------------
# 3. Axis Operations and Matrix Transformations
# ---------------------------------------------------------------------
print("\n--- 3. Axis Operations & Transformations ---")

# Creating a 2D array (3x3 matrix)
x = [[1, 2, 3], [3, 5, 7], [0, 1, 2]]
arr2 = np.array(x)
print(f"Matrix arr2:\n{arr2}")

# Axis 0 = Columns (Vertical operation downwards)
# Axis 1 = Rows (Horizontal operation across)
print(f"Sum along Axis 0 (Column-wise sum): {arr2.sum(axis=0)}")
print(f"Sum along Axis 1 (Row-wise sum): {arr2.sum(axis=1)}")

# .T transposes the matrix (swaps rows and columns)
print(f"Transposed Matrix (arr2.T):\n{arr2.T}")

# Using .flat to iterate through every single element of a matrix
print("Iterating using arr2.flat:")
for element in arr2.flat:
    print(element, end=" ")
print()

print(f"Number of dimensions (ndim): {arr2.ndim}")
print(f"Total bytes consumed by elements (nbytes): {arr2.nbytes} bytes")


# ---------------------------------------------------------------------
# 4. Searching and Sorting (Argmin, Argmax, Argsort)
# ---------------------------------------------------------------------
print("\n--- 4. Min/Max Indices & Sorting ---")

arr3 = np.array([1, 2, 45, 56, 0])
print(f"Array arr3: {arr3}")

# argmax() and argmin() return the *index* of the maximum and minimum values
print(f"Index of max value in arr3: {arr3.argmax()}")  # 56 is at index 3
print(f"Index of min value in arr3: {arr3.argmin()}")  # 0 is at index 4

# argsort() returns the indices that would sort the array in ascending order
print(f"Indices that would sort arr3: {arr3.argsort()}")

# Axis-based argmin/argmax on 2D arrays
print(f"\nMatrix arr2 again:\n{arr2}")
print(
    f"Index of min value along rows (axis=1): {arr2.argmin(axis=1)}"
)  # Min index for each row
print(
    f"Index of max value along columns (axis=0): {arr2.argmax(axis=0)}"
)  # Max index for each col


# ---------------------------------------------------------------------
# 5. Arithmetic Operations and Element-wise Functions
# ---------------------------------------------------------------------
print("\n--- 5. Matrix Math ---")

arr4 = np.array([[2, 4, 7], [24, 67, 1], [2, 0, 1]])

# Element-wise addition
print(f"arr2 + arr4:\n{arr2 + arr4}")

# Element-wise square root
print(f"Square root of arr2 elements:\n{np.sqrt(arr2)}")


# ---------------------------------------------------------------------
# 6. Filtering and Conditional Finding (np.where, non-zero)
# ---------------------------------------------------------------------
print("\n--- 6. Conditional Operations & Finding Elements ---")

# np.where(condition) returns a tuple of arrays representing coordinate indices where condition is True
gt_five = np.where(arr2 > 5)
print(f"Indices where arr2 > 5: {gt_five}")

# np.count_nonzero() returns how many elements do not equal 0
print(f"Count of non-zero elements in arr2: {np.count_nonzero(arr2)}")

# np.nonzero() returns the row and column coordinates of all non-zero elements
print(f"Indices of non-zero elements in arr2:\n{np.nonzero(arr2)}")


# ---------------------------------------------------------------------
# 7. Memory Efficiency: Python List vs NumPy Array
# ---------------------------------------------------------------------
print("\n--- 7. Memory Efficiency Comparison ---")

py_list = [1, 3, 7]
num_py = np.array(py_list)

# Python lists store references to objects, costing significantly more memory
list_memory = sys.getsizeof(1) * len(py_list)
print(f"Memory allocated by raw elements in Python list: {list_memory} bytes")

# NumPy stores uniform data types in contiguous blocks of memory
numpy_memory = num_py.itemsize * num_py.size
print(f"Memory allocated by NumPy array: {numpy_memory} bytes")
print(f"NumPy used {list_memory - numpy_memory} fewer bytes for the same data!")