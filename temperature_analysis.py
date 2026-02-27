import numpy as np
import time

#Task 1: Create an Array and Basic Math
temps_celsius = np.array([22, 25, 28, 24, 26])
temps_fahrenheit = temps_celsius * 1.8 + 32
avg_fahrenheit = round(np.mean(temps_fahrenheit), 1)

print(f"Celsius: {temps_celsius}")
print(f"Fahrenheit: {temps_fahrenheit}")
print(f"Average Fahrenheit: {avg_fahrenheit}")
print("\n")


#Task 2: Array Shape and Statistics
scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
highest = np.max(scores)
lowest = np.min(scores)
score_range = highest - lowest

print(f"Shape: {scores.shape}")
print(f"Total elements: {scores.size}")
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")
print(f"Range: {score_range}")
print("\n")


#Task 3: Performance Comparison
num_range = 50001
np_arr = np.arange(1, num_range)
py_list = list(range(1, num_range))

start_np = time.perf_counter()
np_sum = np.sum(np_arr)
end_np = time.perf_counter()
np_time = end_np - start_np

start_py = time.perf_counter()
py_sum = sum(py_list)
end_py = time.perf_counter()
py_time = end_py - start_py
speed_diff = py_time / (np_time if np_time > 0 else 1e-9)

print(f"NumPy sum: {np_sum}")
print(f"Python sum: {py_sum}")
print(f"NumPy time: {np_time:.6f} seconds")
print(f"Python time: {py_time:.6f} seconds")
print(f"NumPy is {speed_diff:.1f}x faster")