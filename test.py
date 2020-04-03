import numpy as np

value_list = [10, 5, 8, 3, 6, 7, 4]
value_length = len(value_list) +1
target_sum = 24

# combination have [10, 3, 7, 4], [10, 5, 8, 6], [8, 3, 7, 6]
dp = np.zeros((value_length+1, target_sum))
print("{0}".format(dp))
