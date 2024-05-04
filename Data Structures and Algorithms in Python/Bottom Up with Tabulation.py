# Tabulation is the opposite of top-down approach and avoids recursion
    # solve problem "bottom-up" (by solving all related subproblems first)
    # this is done by filling up a table
    # based on results in table, solution to top/original problem is then computed
# top-down is solving backwards from a given value (like F6 of Fibonacci)
# bottom-up is solving forwards from beginning or given value (like F1 or whatever)
# Problem statement: Fibonacci

def fibTabulation(N):
    tb = [0, 1]
    for i in range(2, N+1):
        tb.append(tb[i - 1] + tb[i - 2])
    return tb[N - 1]
# time complexity: O(n)
# space complexity: O(n)
# is it dynamic programming?
    # does it have optimal substructure property?
    # does it have overlapping subproblems property?
    # if answer to both questions is yes, it is dynamic programming
    # merge sort is NOT dynamic programming because while merge sort does have optimal substructure property, it does NOT have overlapping subproblems property because merge sort problems are independent of each other
