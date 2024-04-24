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