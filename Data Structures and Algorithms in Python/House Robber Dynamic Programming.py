# Problem statement: given N number of houses along street with some amount of money, adjacent houses cannot be stolen from, find max amount that can be stolen
# original algorithm (divide and conquer algorithm)
def maxValueHouses(houses, currentHouse):
    if currentHouse > len(houses): # return 0 because there is no house from which to steal
        return 0
    else:
        stealFirstHouse = currentHouse + maxValueHouses(houses, currentHouse+2)
        skipFirstHouse = maxValueHouses(houses, currentHouse+1)
        return max(stealFirstHouse, skipFirstHouse)

