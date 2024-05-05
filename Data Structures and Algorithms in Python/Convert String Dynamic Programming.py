# Problem statement: S1 and S2 are given strings
    # Convert S2 to S1 using delete, insert, or replace operations
    # Find the minimum count of edit operations

# divide and conquer algorithm
def findMinOperation(S1, S2, index1, index2):
    # notice for this program that the first 3 if statements apply only when the strings equal in each other in length
    if index1 == len(S1): # checking that index1 equals length of S1
        return len(S2)-index2
    if index2 == len(S2): # checking that index2 equals length of S2
        return len(S1)-index1
    if S1[index1] == S2[index2]: # adding one to index1 and index2 to perform delete, insert, and replace operations to count minimum number of operations
        return findMinOperation(S1, S2, index1+1, index2+1) # recursion
    else:
        deleteOp = 1 + findMinOperation(S1, S2, index1, index2+1) # S2 is one character longer than S1, so delete extra character from S2
        insertOp = 1 + findMinOperation(S1, S2, index1+1, index2) # S2 is one character shorter than S1, so insert extra character into S2
        replaceOp = 1 + findMinOperation(S1, S2, index1+1, index2+1) # S2 and S1 have same length, so replace character from S2 to make it equal to S1
    return min(deleteOp, insertOp, replaceOp)

# top-down algorithm (dictionary)
def findMinOperationTD(S1, S2, index1, index2, tempDict):
    if index1 == len(S1):
        return len(S2)-index2
    if index2 == len(S2):
        return len(S1)-index1
    if S1[index1] == S2[index2]:
        return findMinOperationTD(S1, S2, index1+1, index2+1)
    else:
        dictKey = str(index1) + str(index2)
        if index1 or index2 not in tempDict:
            deleteOp = 1 + findMinOperationTD(S1, S2, index1, index2+1) # S2 is one character longer than S1, so delete extra character from S2
            insertOp = 1 + findMinOperationTD(S1, S2, index1+1, index2) # S2 is one character shorter than S1, so insert extra character into S2
            replaceOp = 1 + findMinOperationTD(S1, S2, index1+1, index2+1) # S2 and S1 have same length, so replace character from S2 to make it equal to S1
            tempDict[dictKey] = min(deleteOp, insertOp, replaceOp)
        return tempDict[dictKey]

# bottom-up algorithm (tabulation)
def findMinOperationBU(s1, s2, tempDict):
    for i1 in range(len(s1)+1):
        dictKey = str(i1)+'0' # assign iteration of s1 to key of tempDict
        tempDict[dictKey] = i1 # assign key to value
    for i2 in range(len(s2)+1):
        dictKey = '0'+str(i2) # assign iteration of s2 to key of tempDict
        tempDict[dictKey] = i2 # assign key to value
    for i1 in range(1,len(s1)+1):
        for i2 in range(1,len(s2)+1):
            if s1[i1-1] == s2[i2-1]: # if strings equal each other
                dictKey = str(i1)+str(i2)
                dictKey1 = str(i1-1)+str(i2-1)
                tempDict[dictKey] = tempDict[dictKey1]
            else:
                dictKey = str(i1)+str(i2)
                dictKeyD = str(i1-1)+str(i2) # delete because i1-1
                dictKeyI = str(i1)+str(i2-1) # insert because i2-1
                dictKeyR = str(i1-1)+str(i2-1) # replace because i1-1 and i2-1
                tempDict[dictKey] = 1 + min(tempDict[dictKeyD], min(tempDict[dictKeyI],tempDict[dictKeyR])) # min and nested min
    dictKey = str(len(s1))+str(len(s2)) # treat lengths as keys
    return tempDict[dictKey]