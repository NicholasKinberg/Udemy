# binary heap can be min or max; if min binary heap, root node must be min of entire binary heap and recursively true across binary heap
# binary heap is a complete tree (all levels completely filled except possibly last level and last level has all keys as left as possible)
# as a result, binary heaps can be stored in arrays
# can use binary heaps to find min or max numbers in logN time
# inserting additional numbers doesn't take more than logN time
# for example, note that for minimum binary heaps, the minimum value will always be at index 1, so one can implement an algorithm to find the minimum number of the binary heap in O(1) time by simply calling index[1]
class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1
# note that in implementing binary heap through array, index[0] is never occupied
def peekOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1] # return beginning (minimum or maximum depending on type) of binary heap by simply calling customList[1]

def sizeOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize # would return 0 because we assign self.heapSize equal to 0 in Heap class?

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i]) # will traverse by level because binary heap is either max and decreasing or min and increasing, so program will traverse list in order

def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2) # turns index into int and divides it by two, assigning it to parentIndex because parentIndex should be at half the index of the given index (parent node, left child, right child)
    if index <= 1: # if index as given by user is 1 or 0, program simply returns
        return
    if heapType == "Min": # but if the binary heap is a minimum binary heap...
        if rootNode.customList[index] < rootNode.customList[parentIndex]: # if the value of the given index is less than rootNode at half the index value of index...
            temp = rootNode.customList[index] #...initialize temp variable and assign it to given index
            rootNode.customList[index] = rootNode.customList[parentIndex] # set given index eqeual to parentIndex, moving index to left subtree
            rootNode.customList[parentIndex] = temp # set parentIndex equal to temp
        heapifyTreeInsert(rootNode, parentIndex, heapType) # recursive, insert node at correct position
        # using recursion in line above to check that entire binary heap is heapified, using parentIndex as index to use recursion on all parentIndex
    elif heapType == "Max": # maximum binary heap
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The binary heap is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue # assign nodeValue to last index in list
    rootNode.heapSize += 1 # extend length of list by 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been successfully inserted"