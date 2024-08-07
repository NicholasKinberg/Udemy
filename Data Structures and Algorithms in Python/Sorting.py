# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
import math as math

# sorting is arranging data in particular format, either ascending or descending
# types of sorting:
    # space used
        # in place
        # out of place
    # stability
        # stable
        # unstable

# space used
# in place sorting: sorting algorithms which don't require extra space to sort, like bubble sort
# out of place sorting: sorting algorithms which require extra space to sort, like merge sort

# stability
# stable sorting: if a sorting algorithm after sorting the contents does not change the sequence of a similar content in which they appear, this is called stable sorting, like insertion sort
# imagine an array of ascending numbers, some of them the same; those same numbers have different index positions, but unstable sorting will sort these same numbers into different (but ascending or descending) index positions sometimes
# unstable sorting: if a sorting algorithm after sorting the contents does change the sequence of a similar content in which they appear, this is called unstable sorting, like quick sort

# bubble sort: repeatedly compare each pair of adjacent items and swap them if they are in wrong order
def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1): # shorten number of O(n^2) by i instead of having to iterate over customList every time
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j] # use swapping technique such that customList will now show numbers in ascending order
    print(customList)

# selection sort: repeatedly find minimum element and move it to sorted array to make unsorted array sorted
def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)): # decrease list by i+1 to decrease time complexity
            if customList[min_index] > customList[j]:
                min_index = j # if min_index value is greater than j value, assign min_index to j
        customList[i], customList[min_index] = customList[min_index], customList[i] # use swapping technique to assign i to min_index
    print(customList)

# insertion sort: 
    # divide given array into two parts
    # take first element from unsorted array and find correct position in sorted array
    # repeat until unsorted array is empty

def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1 # j is always 1 index position behind i
        while j>=0 and key < customList[j]: # while index j is greater than or equal to 0 and customList[i] < customList[j]:
            customList[j+1] = customList[j] # the following index position value is set to immediate previous index position value
            j -= 1 # subtract one value from original array for each iteration of while loop
        customList[j+1] = key # newly assigned j+1 is assigned to key (customList[i])
    print(customList)

# bucket sort: 
    # create buckets and distribute elements of array into buckets
    # sort buckets individually
    # merge buckets after sorting
    # example:
        # number of buckets = round(sqrt(number of elements))
        # appropriate bucket = cell(value * number of buckets / maxValue)
        # sort all buckets (using any sorting algorithm)

def bucketSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList))) # number of buckets will be the round(sqrt) of length of customList
    maxValue = max(customList) # save maxValue of customList
    arr = [] # initialize empty array
    for i in range(numberOfBuckets): # append an array for each of the buckets you have
        arr.append([]) # append empty list to arr for each bucket
    for j in customList:
        index_b = math.ceil(j*numberOfBuckets/maxValue) # ceil() rounds number up to the next integer that is either bigger than or equal to the value that is being supplied to it
        arr[index_b-1].append(j) # appends number (j) to appropriate bucket in arr
    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i]) # inserting certain numbers from array into certain buckets
    k = 0 # counter variable
    for i in range(numberOfBuckets): # iterate over each bucket in array
        for j in range(len(arr[i])): # iterate over each number in bucket
            customList[k] = arr[i][j] # place number in correct position in original customList
            k += 1 # then increment counter variable k because k is index position in customList
    return customList