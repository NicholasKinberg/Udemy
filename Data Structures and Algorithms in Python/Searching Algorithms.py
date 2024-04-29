import math as math
# These algorithms are designed to efficiently navigate through data structures to find the desired information, ...
# ...making them fundamental in various applications such as databases, web search engines, and more.

# linear search:
    # also known as sequential search, searching for element, element by element
    # can improve time efficiency of linear search several ways, one way is by sorting array
    # pseudocode:
        # create function with two parameters: array and value for which we are searching
        # loop through array and check if each array element is equal to value for which we are searching
        # if value is in array, return index position that that value occupies
        # if the value is never found, return -1 (or False, whatever you prefer)

def linearSearch(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1 # remove return command from for-loop, otherwise return command will iterate and just return -1

# binary search:
    # binary search is faster than linear search
    # half of remaining elements can be eliminated at a time, instead of eliminating one by one
    # binary search only works for sorted arrays
    # pseudocode:
        # create function with two parameters: sorted array and value for which we are searching
        # create two pointers: left pointer at start of array and right pointer at end of array
        # based on left and right pointers, calculate middle pointer
        # while middle is not equal to value and start is less than or equal to end of loop:
            # if middle is greater than value, move right pointer down
            # if middle is lesser than value, move left pointer up
        # if value is never found, return -1

def binarySearch(arr, value):
    start, end = 0, len(arr)-1
    middle = math.floor((start+end)/2)
    print(start, middle, end)
    while not(arr[middle]==value): # while middle doesn't equal value
        if value < arr[middle]:
            end = middle - 1 # count-down from middle
        else:
            start = middle + 1 # count-up from middle
        middle = math.floor((start+end)/2)
        print(start, middle, end)
    if arr[middle] == value:
        return middle
    else:
        return -1
