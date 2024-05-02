# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
import array
from array import *
import numpy as np
array = [1,235,236,34,6,46,346]

### Create an array and traverse
def arrayTraverse(array):
    for i in array:
        print(i)

# arrayTraverse(array)

### Access individual elements through indexes
def accessIndex(array, n):
    print(array[n])

# accessIndex(array, 2)
    
### Append any value to the array using append() method

def appendArray(array, n):
    array.append(n)
    print(array)

# appendArray(array, 6)
    
### Insert any value in an array using insert() method
    
def insertArray(array, n, new_number):
    array.insert(n, new_number)
    print(array)

# insertArray(array, 2, 4)
    
### Extend python array using extend() method

def extendArray(array, new_array):
    array.extend(new_array)
    print(array)

# extendArray(array, new_array=[3,2356,236,42,23,5])

### Add items from list into array using fromlist() method
### COME BACK TO THIS
def fromlistArray(array, old_array):
    array.fromlist(old_array)
    print(array)

# fromlistArray(array, old_array=[23,6234,457,478,8,7,456,98,0])
    
### Remove any array element using remove() method
def removeElementArray(array, element):
    array.remove(element)
    print(array)

# removeElementArray(array, 235)

### Remove last array element using pop() method
def popArray(array, n):
    array.pop(n)
    print(array)

# popArray(array, 2)
    
### Fetch any element through its index using the index() method
def indexArray(array, n):
    a = array.index(n)
    print(a)

# indexArray(array, 235)