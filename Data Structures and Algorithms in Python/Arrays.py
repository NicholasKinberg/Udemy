# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
import array

### basic array 'i'
my_array = array.array('i')
# print(my_array)

my_array1 = array.array('i', [1,2,3,4])
# print(my_array1)

import numpy as np

np_array = np.array([], dtype=int)
np_array1 = np.array([23,26,235,346,2,3,234])
# print(np_array1)

array1 = array.array('i', [23,234,342,63,434,6,345,3])
array1.insert(3, 67)
# print(array1)

### function to access an element of an array, will return 'not found' if index number is higher than len(array)
def accessIndex(array, index):
    if index > len(array):
        print('the value at this index position does not exist')
    else:
        return array[index]
    
array10 = [234,2345,346,423,643,34,345,7346,345]
# print(accessIndex(array10, 7))

### function to return index position of number for which one searches, equal to n, in array
### can change i variable to n to return actual number instead of index position
def linearSearch(array, n):
    for i in range(len(array)):
        if array[i] == n:
            return i
    return -1

# print(linearSearch([234,234,235,235,24,223,3465,45,4], 234))

from array import *

array11 = array('i', [234,235,236,346,63,475,7,457])
array11.remove(array11[3])
# print(array11)