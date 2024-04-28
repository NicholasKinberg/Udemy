# Graph Data Structure is a collection of nodes connected by edges. 
# It’s used to represent relationships between different entities. 
# Graph algorithms are methods used to manipulate and analyze graphs, solving various problems like finding the shortest path or detecting cycles.

# graph consists of finite set of vertices (nodes) and set of edges which connect pairs of nodes
    # terminology:
        # vertices: vertices are nodes of a graph
        # edge: edge is line that connects pairs of vertices
        # unweighted graph: graph which doesn't have weight associated with any edge
        # weighted graph: graph which has weight associated with any edge
        # undirected graph: edges of graph don't have directions associated with them
        # directed graph: edges of graph do have directions associated with them
        # cyclic graph: graph that has at least one loop
        # acyclic graph: graph that has no loop
        # tree: special case of directed acyclic graphs
    # graph types:
        # unweighted - undirected
        # unweighted - directed
        # positive - weighted - undirected
        # positive - weighted - directed
        # negative - weighted - undirected
        # negative - weighted - directed
        # positive means positive values representing edges
        # negative means at least one negative value representing an edge

# graph representation
    # adjacency matrix: square matrix (2D array), elements of array indicate whether pairs of vertices are adjacent in graph
        # use adjacency matrix if graph is complete or almost complete
    # adjacency list: collection of unordered list used to represent graph, each list describes set of neighbors of vertex in graph
        # use adjacency list if there are few edges

# dictionary implementation
    # treat the following dictionary as the keys connecting to the values, so vertex A connects to vertex B and vertex C,
    # vertex B connects to vertices A, D, and E, and so on
    # {A:[B,C], 
    #  B:[A,D,E],
    #  C:[A,E],
    #  D:[B,E,F],
    #  E:[C,D,F],
    #  F:[D,E]}

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge) # appending edge to vertex
    
    def addVertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = [] # initializes new array in which to add values to new key (which is new vertex)
            return True
        return False
    
    def printGraph(self):
        for vertex in self.gdict:
            print(vertex,":",self.gdict[vertex])

customDict =   {'A':['B','C'], 
                'B':['A','D','E'],
                'C':['A','E'],
                'D':['B','E','F'],
                'E':['C','D','F'],
                'F':['D','E']}

# graph = Graph(customDict)
# graph.addEdge('E', 'C')
# print(graph.gdict('E'))