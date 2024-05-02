# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# topological sort: sorts given actions in such a way that if there is a dependency of one action on another, then the dependent action always comes later than parent action
# topological sort algorithm implemented as stack
# pseudocode:
    # if a vertex depends on currentVertex:
        # go to that vertex and
        # then come back to currentVertex
    # else
        # push currentVertex to stack
from collections import defaultdict
class Graph:
    def __init__(self, numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices
    
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge) # add edge connected to vertex
    
    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v) # append vertices
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack) # initializing stack for visited vertices, recursive
        stack.insert(0, v) # insert unvisited vertices at position 0 because we're using a stack
    
    def topologicalSort(self):
        visited = []
        stack = []
        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack) # topologicalSortUtil provides structure for topologicalSort function to initialize visited and stack lists
        print(stack)