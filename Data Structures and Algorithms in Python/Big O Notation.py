### example of O(1)
### this is O(1) because I am telling the computer to focus on one int and one int only
def multiply_numbers(n):
    print(n * n)

### example of O(n)
### this is O(n) because computer must go through each item
def print_items(n):
    for i in range(n):
        print(i)


### example of O(2n) which equals O(n)
def print_items_again(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)


### example of O(n^2)
def print_items_squared(n):
    for i in range(n):
        for j in range(n):
            print(i,j)


### example of O(n^3)
def print_items_cubed(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)


### example of O(n^2 + n) which equals O(n^2)
def print_items_squared_plus_n(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
        print(k)

### example of recursive algorithm
### this function calls itself in its own function
def recursive_print(n):
    if n <= 0:
        return 0
    return n + recursive_print(n-1)

### another recursive algorithm example
def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total = total + pair_sum(i, i+1)
    return total
def pair_sum(a,b):
    return a + b


### example of O(a + b)
def print_a_b(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)

### example of O(a * b)
def print_a_times_b(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)

def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]
    for i in range(1, len(sampleArray)):
        if sampleArray[i] > biggestNumber:
            biggestNumber = sampleArray[i]
    print(biggestNumber)

findBiggestNumber(sampleArray=[1, 23, 324, 3245, 23, 252, 35, 2358])