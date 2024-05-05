# Problem statement: given N number of houses along street with some amount of money, adjacent houses cannot be stolen from, find max amount that can be stolen
# original algorithm (divide and conquer algorithm)
def maxValueHouses(houses, currentHouse):
    if currentHouse > len(houses): # return 0 because there is no house from which to steal
        return 0
    else:
        stealFirstHouse = currentHouse + maxValueHouses(houses, currentHouse+2)
        skipFirstHouse = maxValueHouses(houses, currentHouse+1)
        return max(stealFirstHouse, skipFirstHouse)

# top-down algorithm where we implement dictionary of solved subproblems
def maxValueHousesTD(houses, currentHouse, tempDict):
    if currentHouse > len(houses): # return 0 because there is no house from which to steal
        return 0
    else:
        if currentHouse not in tempDict: # implement dictionary to solve subproblems only once and not multiple times
            stealFirstHouse = currentHouse + maxValueHousesTD(houses, currentHouse+2, tempDict)
            skipFirstHouse = maxValueHousesTD(houses, currentHouse+1, tempDict)
            tempDict[currentHouse] = max(stealFirstHouse, skipFirstHouse) # add solved subproblem to dictionary
        return tempDict[currentHouse] # return subproblems, each solved only once

# bottom-up algorithm where we implement tabulation of solved subproblems
def maxValueHousesBU(houses):
    tempAr = [0]*(len(houses)+2)
    for i in range(len(houses)-1, -1, -1):
        tempAr[i] = max(houses[i]+tempAr[i+2], tempAr[i+1])
    return tempAr[0]