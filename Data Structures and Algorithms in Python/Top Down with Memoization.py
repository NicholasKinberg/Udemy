# Dynamic programming (DP) is an algorithmic technique for solving an optimization problem by breaking it down into simpler subproblems and using the fact that optimal solution to overall problem depends upon optimal solution to its subproblems
# Top down with memoization takes the original problem, solves some of its subproblems and stores the results of those subproblems in memory, and builds the rest of the program with recursion to reduce time complexity
# top-down is solving backwards from a given value (like F6 of Fibonacci)
# bottom-up is solving forwards from beginning or given value (like F1 or whatever)
# Problem statement: solve the problem by recursively finding solution to smaller subproblems
    # whenever we solve a subproblem, we cache its result so we don't solve it repeatedly if it's called multiple times
    # technique of storing results of already solved subproblems is called memoization

# example: 0, 1, 1, 2, 3, 5, 8, ...
    # Fibonacci(N) = Fibonacci(N-1) + Fibonacci(N-2)

def Fibonacci(N):
    if N < 1:
        return ValueError
    if N == 1:
        return 0
    if N == 2:
        return 1
    else:
        return Fibonacci(N-1) + Fibonacci(N-2)
    # time complexity: O(c^n)
    # space complexity: O(n)
    # with recursion, imagine a recursion tree, where for example we print Fibonacci(10)
        # Fibonacci recursion will run until N < 1, at which point the program terminates
        # but the problem is that recursion will solve the same problem multiple times, so we want to optimize that
        # so we rewrite the program as:

def fibMemo(N, memo): # store in memory that F1, F2, F3, ..., FN equal certain numbers to reduce time complexity
    if N == 1:
        return 0
    if N == 2:
        return 1
    if not N in memo:
        memo[N] = fibMemo(N-1, memo) + fibMemo(N-2, memo)
    return memo[N]