# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
import numpy as np
def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = np.array([23,4234,543,6234,57,3,64,5321,43,456743,73,56,2,56,7895,432])
print(search(arr, 6234))