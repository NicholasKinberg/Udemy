# Problem statement: you are given coins of different denominations and total amount of money; find minimum number of coins that you need to make up a given amount

# treat problem as taking an array of coins
# minimize number of numbers needed to produce sum
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

def coinChange(totalNumber, coins):
    N = totalNumber # given by user
    coins.sort() # sort numbers in ascending order
    index = len(coins)-1 # index equals one less than length of coins array
    while True: # while loop
        coinValue = coins[index] # while coinValue is assigned to second-to-last position of coins array, which should be second-to-largest number in array...
        if N >= coinValue: # if N is greater than or equal to coinValue (which should be second-to-largest number in coins array)
            print(coinValue) # print coinValue
            N = N - coinValue # then subtract coinValue from N
        if N < coinValue: # if N is less than coinValue (again, the penultimate number in the coins array)
            index -= 1 # subtract one from index, making the array smaller such that coinValue will eventually be lesser than or equal to N
        if N == 0: # if N equals 0, stop while loop, returning nothing
            break
# note that if I set x = y in one line and then set y = 0 in the next, x does NOT take on value of 0, x takes on value of y at time of assignment