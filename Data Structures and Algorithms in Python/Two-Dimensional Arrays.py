import numpy as np
# Day 1 - 1,23,523,346,34,74,574
# Day 2 - 1,23,563,672,34,23,567
# Day 3 - 1,23,657,678,23,90,235
# Day 4 - 2,45,436,764,23,45,234
twoDArray = np.array([[1,23,523,346,34,74,574], [1,23,563,672,34,23,567],
                     [1,23,657,678,23,90,235], [2,45,436,764,23,45,234]])
# print(twoDArray)
# newtwoDArray = np.insert(twoDArray, 0, 1)
# print(newtwoDArray)

### need to access rows and columns, so [i]1 and 1[i]
def accessElements(array, rowIndex, columnIndex):
    if rowIndex >= len(array) or columnIndex >= len(array[0]):
        print('incorrect index')
    print(array[rowIndex][columnIndex])

# accessElements(twoDArray, 2, 2)

def traverseElements(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j])

# traverseElements(twoDArray)
            
### build search function that returns position of value
### build nested for loop
def searchArray(array, value):
    for i in range(len(array)):
        for j in range(len(array)):
            if value == array[i][j]:
                print(i, j)
    print('item not found')

searchArray(twoDArray, 652357)