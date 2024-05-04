# Problem statement: given N, find the number of ways to express N as a sum of 1, 3, and 4
# original algorithm (divide and conquer algorithm)
def numberFactor(N):
    if N in (0, 1, 2):
        return 1
    if N == 3:
        return 2
    else:
        return numberFactor(N-1) + numberFactor(N-3) + numberFactor(N-4)

# top-down approach where instead of solving the same problem multiple times, we implement a dictionary to store values for key N
def numberFactorTD(N, dp): # variable where dp is dynamic programming dictionary
    if N in (0, 1, 2):
        return 1
    if N == 3:
        return 2
    elif N in dp:
        return dp[N]
    else:
        if N not in dp:
            rec1 = numberFactorTD(N-1)
            rec2 = numberFactorTD(N-3)
            rec3 = numberFactorTD(N-4)
            dp[N] = rec1 + rec2 + rec3
        return dp[N]

# bottom-up approach (tb for tabulation) where we append solved subproblems to tb list
def numberFactorBU(N):
    tb = [1,1,1,2] # first four values for any numberFactor function
    for i in range(4, N+1):
        tb.append(tb[i-1]+tb[i-3]+tb[i-4]) # append numberFactor calculation to tb array
    return tb[N] # return tb value at index N