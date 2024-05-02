# Problem statement: you are given coins of different denominations and total amount of money; find minimum number of coins that you need to make up a given amount

# treat problem as taking an array of coins
# minimize number of numbers needed to produce sum
def minimumNumberOfCoins(array, totalSum):
    pass
    # two parameters: array and sum
    # sum = 0
    # for i in range(len(array)):
        # sum = sum + i
        # if totalSum == sum
            # return totalSum
        # else
            # return "no combination of numbers will produce totalSum"
    ### OR ###
    # could sort array by ascending or descending, but could also use SSSP algorithms
    # how would we adapt SSSP algorithms to this optimization problem?