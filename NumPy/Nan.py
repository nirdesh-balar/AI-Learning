import numpy as np

# Creating an array with np.nan
arr = np.array([1, 2, np.nan, 4, np.nan])
print(arr)

# Checking for NaN values
is_nan = np.isnan(arr)
print(is_nan)

# Performing operations while ignoring NaN values
sum_without_nan = np.nansum(arr)
print(sum_without_nan)