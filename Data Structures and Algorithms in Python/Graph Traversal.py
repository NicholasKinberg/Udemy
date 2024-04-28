# breadth first search (BFS), searching laterally
# depth first search (DFS), searching vertically (to the end of each subtree and then moving to the next one)
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False
    
    def addVertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = [] # initializes new array in which to add values to new key (which is new vertex)
            return True
        return False
    
    def printGraph(self):
        for vertex in self.gdict:
            print(vertex,":",self.gdict[vertex])

    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            try:
                self.gdict[vertex1].remove(vertex2)
                self.gdict[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    def removeVertex(self, vertex):
        if vertex in self.gdict.keys():
            for other_vertex in self.gdict[vertex]:
                self.gdict[other_vertex].remove(vertex)
            del self.gdict[vertex]
            return True
        return False

    def bfs(self, vertex): # uses queue, FIFO
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex)
            for adjacent_vertex in self.gdict[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)
    
    def dfs(self, vertex): # uses stack, LIFO
        visited = set()
        stack = [vertex]
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
            for adjacent_vertex in self.gdict[current_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)





customDict =   {'A':['B','C'], 
                'B':['A','D','E'],
                'C':['A','E'],
                'D':['B','E','F'],
                'E':['C','D','F'],
                'F':['D','E']}