# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# Problem Statement: Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.
# using breadth first search to ascertain whether there is a route between two nodes in a directed acyclic graph
# pseudocode:
    # create function with two parameters start and end ndoes
    # create queue and enqueue start node to it (FIFO for directed acyclic grpah (DAG))
    # find all neighbors of enqueued node and then enqueue them into queue
    # repeat this process until end of elements in graph
    # if during the above process at some point we encounter destination node, return True
    # mark visited nodes as visited

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        visited = [startNode] # first node to visit
        queue = [startNode] # enqueue startNode
        path = False
        while queue:
            deVertex = queue.pop(0)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited: # lines 24 to 27 are from BFS
                    if adjacentVertex == endNode: # if while loop reaches endNode, break and return path as True
                        path = True
                        break # if adjacentVertex != endNode, break
                    else:
                        visited.append(adjacentVertex) # continue appending adjacentVertex until adjacentVertex == endNode
                        queue.append(adjacentVertex)
        return path

### OR ###
from collections import defaultdict
class Graph2:
    def __init__(self, vertices):
        self.V = vertices # implement vertices individually
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def isReachable(self, start, end):
        visited = [False]*(self.V) # set all vertices equal to False for whether they have been visited initially
        queue = [] # initialize queue, queue is integral to BFS, just as stack is integral to DFS
        queue.append(start) # append starting node
        visited[start] = True # thus we set whether starting node has been visited to True
        while queue: # while loop again
            n = queue.pop(0) # popping each element of DAG, setting to n
            if n == end: # if n ever equals ending node, return True
                return True
            for i in self.graph[n]: # else, continue running while loop where for i in DAG, if a node i hasn't been visited, append that node to the queue and set whether that node has been visited to True
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return False # if n never equals end, return False