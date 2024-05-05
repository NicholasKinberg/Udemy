# Divide and conquer algorithms are about solving sub-problems of the major problem to yield solution to major problem
# Problem statement: S1 and S2 are given strings
    # Convert S2 to S1 using delete, insert, or replace operations
    # Find the minimum count of edit operations

# probably need to use while loops
# probably need to use recursion
# implement counter to count how many times either method is used (probably can only use one method)
# inputs: S1 and S2
# outputs: S1 and number of edit operations

# examples:
    # convert a simple word to another simple word using only delete
    # convert a simple word to another simple word using only insert
    # convert a simple word to another simple word using only replace

# pseudocode
    # implement delete function
    # implement insert function
    # implement replace function
    # implement counter to count how many times the program runs w/which edit operations

# example 1
    # S1 = "catch"
    # S2 = "carch"
    # output = 1 because only one operation needed
    # explanation: replace "r" with "t"

# example 2
    # S1 = "table"
    # S2 = "tbres"
    # output = 3 because need to insert "a" in second position, replace "r" and "l" and delete "s"

def findMinOperation(S1, S2, index1, index2):
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