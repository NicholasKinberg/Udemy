# In Kruskal’s algorithm, sort all edges of the given graph in increasing order. 
# Then it keeps on adding new edges and nodes in the MST if the newly added edge does not form a cycle. 
# It picks the minimum weighted edge at first and the maximum weighted edge at last. 
# Thus we can say that it makes a locally optimal choice in each step in order to find the optimal solution. 
# Hence this is a Greedy Algorithm (locally optimal solution).

# pseudocode:
    # Kruskal(G):
        # for each vertex:
            # makeSet(v)
        # sort each edge in non decreasing order by weight
        # for each edge (u, v):
            # if findSet(u) != findSet(v):
                # union(u, v)
                # cost = cost + edge(u, v)

import DisjointSet as dst
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []
    
    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])
    
    def addNode(self, value):
        self.nodes.append(value)
    
    def printSolution(self, s, d, w):
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))
    
    def kruskalAlgorithm(self):
        i, e = 0, 0
        ds = dst.DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key = lambda item: item[2])
        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s, d, w])
                ds.union(x, y)
        self.printSolution(s, d, w)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)
g.kruskalAlgorithm()



# Like Kruskal’s algorithm, Prim’s algorithm is also a Greedy algorithm. 
# This algorithm always starts with a single node and moves through several adjacent nodes, in order to explore all of the connected edges along the way.
# The algorithm starts with an empty spanning tree. 
# The idea is to maintain two sets of vertices. 
# The first set contains the vertices already included in the MST, and the other set contains the vertices not yet included. 
# At every step, it considers all the edges that connect the two sets and picks the minimum weighted edge from these edges. 
# After picking the edge, it moves the other endpoint of the edge to the set containing MST. 