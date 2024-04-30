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

# practical Prim's algorithm:
    # Prim's algorithm is a greedy algorithm
    # it finds minimum spanning tree (MST) for weighted undirected graphs in following ways:
        # 1. take any vertex as source, set its weight to 0, and all other vertices' weights to infinity
        # 2. for every adjacent vertex, if current weight is more than current edge, then we set current weight to current edge
        # 3. then we mark current vertex as visited
        # 4. repeat these steps for all vertices in increasing order of weight
import sys
class Graph:
    def __init__(self, vertexNum, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.vertexNum = vertexNum
        self.MST = []
    
    def printSolution(self):
        print("Edge : Weight")
        for s, d, w in self.MST:
            print("%s -> %s: %s" % (s, d, w))
    
    def primAlgorithm(self):
        visited = [0]*self.vertexNum
        edgeNum = 0
        visited[0] = True
        while edgeNum<self.vertexNum-1:
            min = sys.maxsize
            for i in range(self.vertexNum):
                if visited[i]:
                    for j in range(self.vertexNum):
                        if ((not visited[j]) and self.edges[i][j]):
                            if min > self.edges[i][j]:
                                min = self.edges[i][j]
                                s = i
                                d = j
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True
            edgeNum += 1
        self.printSolution()

edges = [[0, 10, 20, 0, 0],
         [10, 0, 30, 5, 0],
         [20, 30, 0, 15, 6],
         [0, 5, 15, 0, 8],
         [0, 0, 6, 8, 0]]
nodes = ["A", "B", "C", "D", "E"]
g = Graph(5, edges, nodes)
g.primAlgorithm()

# kruskal
    # concentrates on edges
    # finalize edge in each iteration
# prim
    # concentrates on vertices
    # finalize vertex in each iteration