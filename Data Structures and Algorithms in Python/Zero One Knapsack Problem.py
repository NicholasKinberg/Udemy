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

# pseudocode:
    # knapsack(items, capacity, currentIndex):
        # for-loop to sum profits from items, should be in index[2] for each item
        # for-loop to sum weights from items, should be in index[1] for each item
        # name of each item is in index[0] for each item
        # if capacity <= 0 or currentIndex < 0 or currentIndex > len(profits)
            # return 0
        # elif currentItemWeight <= capacity
            # profit1 = currentItemProfit * knapsack(items, capacity - currentItemWeight, nextItem)
            # profit2 = knapsack(items, capacity - currentItemWeight, nextItem)
            # return max(profit1, profit2)
        # else
            # return 0
def knapsack(items, capacity, currentIndex):
    if capacity <= 0 or currentIndex < 0 or currentIndex > len(items):
        return 0 # if-else are mutually exclusive, if-elif-else are not mutually exclusive
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit * knapsack(items, capacity-items[currentIndex].weight, currentIndex+1)
        profit2 = knapsack(items, capacity-items[currentIndex].weight, currentIndex+1)
        return max(profit1, profit2)
    else:
        return 0 # assuming that first column is titled "weight" and second column is titled "profit"