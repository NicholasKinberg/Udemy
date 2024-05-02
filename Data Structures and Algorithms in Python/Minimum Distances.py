# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# breadth first search algorithm to solve:
# given map with treasures and obstacles, compute distance (count of ticks) from given initial position to nearest accessible treasure
# for this program, initial position can be key in dict, then maybe execute while loop to find nearest treasure
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0) # pop() command takes index position as argument, not value, last in first out (LIFO) for queue
            print(s, end = "")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True