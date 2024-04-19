# depth first search algorithm problem
# output is true or false depending on whether one can access treasure 't' without being barred by obstacle 'X' horizontally or vertically
# input to function MUST be dictionary
from collections import defaultdict
class Graph:
    def __init__(self, data, next):
        self.graph = defaultdict(list)
        self.data = data
        self.next = None
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbor in self.graph[v]: # selecting based on key in self.graph, which is a dictionary
            if neighbor not in visited: # if neighbor is not yet in 'visited' list
                self.DFSUtil(neighbor, visited) # recursive, neighbor will be added to 'visited' list
            elif neighbor == 'X':
                print("cannot access treasure")
            elif neighbor == 't':
                print("treasure found")

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)
    
    # need traverse function to find t
    # then implement traverse except when X

# depth first search algorithm (DFS) goes to depth in searching for indices and values in a specific branch of a tree
        # whereas breadth first search algorithm (BFS) searches by level of depth
# treasure map has the following format:
# ..t...
# ..XXX.
# ......
# tX..X.
# .X..Xt
# .XX...
# the DFS algorithm is above but you need to program functionality for a few things:
        # (1) the program needs to find 't'
        # (2) the program needs to identify 'X'
        # (3) the program needs to ignore 't' when the format is the following:
        # .X.
        # XtX
        # .X.
        # such that we cannot access 't' without going through X
        # note that one cannot access 't' diagonally

