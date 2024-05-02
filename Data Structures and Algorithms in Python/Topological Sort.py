# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# topological sorting is typically acyclic (directed acyclic graph (DAG))
# here too we will use a dictionary to build a topological sort algorithm, notice that algorithms usually use dictionaries
# recursive implementation of topological sort algorithm
import random
from collections import defaultdict
from queue import Queue
class GraphVertex:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v) # v in visited, u in unvisited
    
    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack) # recursive
        stack.insert(0, v) # inserting vertex at position 0, like a queue, if vertex has been visited, FIFO
    
    def topologicalSort(self):
        visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        print(stack)
    
class Graph:
    def __init__(self):
        self.nodes = []
    
    def add_node(self, node):
        self.nodes.append(node)

def generateRandomDict(n):
    keys = [str(i) for i in range(n)]
    values = [random.randint(0, 100) for i in range(n)]
    return dict(zip(keys, values))

vertices = {'A':GraphVertex('A'), 'B':GraphVertex('B'), 'C':GraphVertex('C')}
vertices['A'].addEdge(vertices['D'])
vertices['B'].addEdge(vertices['E'])
vertices['C'].addEdge(vertices['F'])
g = GraphVertex()
# nodes are vertices for the purposes of this program
# need to use dicts, can't be lists
# problem 1: n tasks to be done, some tasks must be done before others, print lexicographically smallest order of tasks

# use this link for another method of topological sort that should answer the question: https://www.youtube.com/watch?v=2mza5BtOefU