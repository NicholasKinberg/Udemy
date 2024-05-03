# Problem statement: given N, find the number of ways to express N as a sum of 1, 3, and 4
# Example 1:
    # N = 4
    # Number of ways = 4
    # Explanation: there are 4 ways we can express N: 4, [1,3], [3,1], [1,1,1,1]

def sumsOfOneThreeAndFour1(N):
    array = [1, 3, 4]
    if N == 0:
        return ValueError
    if N == 1:
        return 1 # can only express N as sum of 1 in 1 way: 1
    if N == 2:
        return 1 # can only express N as sum of 1 in 1 way [1,1]
    if N == 3:
        return 2 # can only express N as sum of 1 in 2 ways: 3, [1,1,1]
    if N == 4:
        return 4 # can only express N as sum of of 1 and 3 in 4 ways: 4, [1,3], [3,1], [1,1,1,1]
    # N is int
    # combination program to test different combinations of 1, 3, and 4 to see whether it equals sum
    array.sort()
    index = len(array)-1
    while True:
        value = array[index]
        if N >= value:
            print(value)
            N = N - value
        if N < value:
            index -= 1
        if N == 0:
            break