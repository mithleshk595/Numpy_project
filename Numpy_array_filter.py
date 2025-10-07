import numpy as np

arr = np.array([1, 2,  3, 4, 5, 6, 7])

# create an empty list
filter_arr = []

# go throgh each elemnt in arr
for element in arr:
    # if the element is completely divisible by 2, set the value is true, otherwise false
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(arr)

