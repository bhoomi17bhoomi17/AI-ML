import numpy as np
import pandas as pd
from scipy import stats

# Sample data
data = [12, 15, 14, 10, 18, 20, 15, 16, 14, 19]

# Mean
mean = np.mean(data)
print("Mean:", mean)

# Median
median = np.median(data)
print("Median:", median)

# Mode
mode = stats.mode(data, keepdims=True)
print("Mode:", mode.mode[0])

# Variance
variance = np.var(data, ddof=1)
print("Variance:", variance)

# Standard deviation
std_dev = np.std(data, ddof=1)
print("Standard Deviation:", std_dev)

# Covariance & Correlation
x = np.array([2, 4, 6, 8, 10])
y = np.array([3, 7, 5, 11, 14])

cov_matrix = np.cov(x, y)
print("Covariance matrix:\n", cov_matrix)

corr = np.corrcoef(x, y)
print("Correlation matrix:\n", corr)

# Simple Linear Regression (y = m*x + b)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print(f"Regression line: y = {slope:.2f}x + {intercept:.2f}")