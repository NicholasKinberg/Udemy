# Problem statement: given N, find the number of ways to express N as a sum of 1, 3, and 4
# Example 1:
    # N = 4
    # Number of ways = 4
    # Explanation: there are 4 ways we can express N: 4, [1,3], [3,1], [1,1,1,1]

def sumsOfOneThreeAndFour(N):
    if N == 0:
        return ValueError
    if N == 1:
        return 1 # can only express N as sum of 1 in 1 way: 1
    if N == 2:
        return 1 # can only express N as sum of 1 in 1 way [1,1]
    if N == 3:
        return 2 # can only express N as sum of 1 in 2 ways: 3, [1,1,1]
    else:
        subP1 = sumsOfOneThreeAndFour(N-1)
        subP2 = sumsOfOneThreeAndFour(N-3)
        subP3 = sumsOfOneThreeAndFour(N-4)
        return subP1+subP2+subP3
    
    # N is int
    # combination program to test different combinations of 1, 3, and 4 to see whether it equals sum
    # if we were to solve this problem, for example f(6), then we would break that down into f(5), f(3), f(2), and so on
    # we can then break those sub-problems down into further sub-problems, like any recursion
    # break problem down by doing the math, for example by understanding that you can add number of solutions from f(5), f(3), and so on
    # you break f(6) down to f(5), f(3), and f(2) because N-1, N-3, and N-4 equal 5, 3, and 2, respectively

    # so in the future, break down problems into their most basic sub-problems while writing pseudocode