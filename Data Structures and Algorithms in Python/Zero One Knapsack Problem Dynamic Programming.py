# Problem statement: given weights and profits of N items, find max profit within given capacity C, items can't be broken
# example 1:
    # mango, apple, orange, banana, each with different weight and profit, can fit into a knapsack with capacity (C) 7
    # mango[weight: 3, profit: 31], index 1
    # apple[weight: 1, profit: 26], index 2
    # orange[weight: 2, profit: 17], index 3
    # banana[weight: 5, profit: 72], index 4

    # orange + banana = weight: 7, profit: 89, f(3, 4), numbers within function refer to index positions as stated above, name this operation subProblem1
    # orange * 3 + apple = weight: 7, profit: 77, f(2, 3), subProblem2
    # mango * 2 + apple = weight: 7, profit: 88, f(1, 3), subProblem3
    # banana + apple * 2 = weight: 7, profit: 150, f(2, 4), subProblem4

    # result should be max(subProblem1, subProblem2) and so on

# divide and conquer algorithm
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def knapsack(items, capacity, currentIndex):
    if capacity <= 0 or currentIndex < 0 or currentIndex > len(items):
        return 0 # if-else are mutually exclusive, if-elif-else are not mutually exclusive
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit * knapsack(items, capacity-items[currentIndex].weight, currentIndex+1)
        profit2 = knapsack(items, capacity-items[currentIndex].weight, currentIndex+1)
        return max(profit1, profit2)
    else:
        return 0 # assuming that first column is titled "weight" and second column is titled "profit"

# top-down (dictionary)
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
 
def knapsackTD(items, capacity, currentIndex, tempDict):
    dictKey = str(currentIndex) + str(capacity) # add strings of index and capacity as dictKey
    if capacity <=0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    elif dictKey in tempDict:
        return tempDict[currentIndex] # if dictKey is already in tempDict, just return key currentIndex value in tempDict
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + knapsackTD(items, capacity-items[currentIndex].weight, currentIndex+1, tempDict)
        profit2 = knapsackTD(items, capacity, currentIndex+1, tempDict)
        tempDict[dictKey] = max(profit1, profit2)
        return tempDict[dictKey]
    else:
        return 0

# bottom-up (tabulation)
def knapsackBU(profits, weights, capacity):
    if capacity <= 0 or len(profits) == 0 or len(weights) != len(profits):
        return 0
    numberOfRows = len(profits) + 1
    dp = [[None for i in range(capacity+2)] for j in range(numberOfRows)]
    for i in range(numberOfRows):
        dp[i][0] = 0
    for i in range(capacity+1):
        dp[numberOfRows-1][i] = 0
    for row in range(numberOfRows-2, -1, -1):
        for column in range(1,capacity+1):
            profit1 = 0
            profit2 = 0
            if weights[row] <= column:
                profit1 = profits[row] + dp[row + 1][column - weights[row]]
            profit2 = dp[row + 1][column]
            dp[row][column] = max(profit1, profit2)
    return dp[0][capacity]