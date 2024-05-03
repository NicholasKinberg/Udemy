# Problem statement: given N number of houses along street with some amount of money, adjacent houses cannot be stolen from, find max amount that can be stolen
houseValues = [1,2,3,4,5,6]
# activity selection problem method might be helpful but sorting will be difficult if index of each entry matters
# can't rob two houses that are adjacent, so can't rob house at index[1] if I robbed house at index[0]

# so if I have houseValues = [1,2,3], I can steal a max of 4 because I can't steal from house with value 2 at index position 1
def houseRobber(houseValues):
    evenIndex = []
    oddIndex = []
    if len(houseValues) == 0:
        return 0
    if len(houseValues) == 1:
        return houseValues[0]
    if len(houseValues) == 2:
        if houseValues[0] > houseValues[1]:
            return houseValues[0]
        else:
            return houseValues[1]
    else:
        for i in range(len(houseValues)):
            evenIndex.append(2 * i)
            oddIndex.append((2*i) + 1)
        if sum(evenIndex) > sum(oddIndex):
            return evenIndex
        else:
            return oddIndex
# 2 * i and (2 * i) + 1 for even and odd indices
# I could sort these numbers, but if I do that, original indices will be changed
### OR ###
# maxValueHouses(houses, currentHouse):
    # if currentHouse > length of houses:
        # return 0
    # else:
        # stealFirstHouse = currentHouse + maxValueHouse(houses, currentHouse+2)
        # skipFirstHouse = maxValueHouse(houses, currentHouse+1)
        # return max(stealFirstHouse, skipFirstHouse)

# above pseudocode is advancement of logic from program I wrote
# analyzing else statement:
    # stealFirstHouse refers to sum of first and third index positions
    # skipFirstHouse refers to only second index position
    # return max takes max of either value as recursion goes throughout entire array

def maxValueHouses(houses, currentHouse):
    if currentHouse > len(houses): # return 0 because there is no house from which to steal
        return 0
    else:
        stealFirstHouse = currentHouse + maxValueHouses(houses, currentHouse+2)
        skipFirstHouse = maxValueHouses(houses, currentHouse+1)
        return max(stealFirstHouse, skipFirstHouse)