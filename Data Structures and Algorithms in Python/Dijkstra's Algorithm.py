# Dijkstra's Algorithm: Given a weighted graph and a source vertex in the graph, find the shortest paths from the source to all the other vertices in the given graph.
import heapq
class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight # edge is composed of weight, start vertex, and target vertex
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex
    
class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False # False that a given vertex is initially visited
        self.predecessor = None # assume no predecessor until predecessor exists
        self.neighbors = [] # stack for neighbors
        self.min_distance = float("inf") # initially infinite distance between start and target vertices
    
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance # code for finding shortest path

    def addEdge(self, weight, destination_vertex):
        edge = Edge(self, weight, destination_vertex)
        self.neighbors.append(edge) # append edges to neighbors

class Dijkstra:
    def __init__(self):
        self.heap = [] # initialize heap
    
    def calculate(self, start_vertex):
        start_vertex.min_distance = 0 # start_vertex has distance 0
        heapq.heappush(self.heap, start_vertex) # pushes start_vertex onto heap that we initialized earlier
        while self.heap:
            # pop element with lowest distance
            actual_vertex = heapq.heappop(self.heap) # pop smallest item from heap as actual_vertex
            # consider neighbors
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance # Dijkstra's algorithm works by finding shortest path, so shortest path will be smallest distance
                    target.predecessor = start
                    # update the heap
                    heapq.heappush(self.heap, target)
                actual_vertex.visited = True
    
    def getShortestPath(self, vertex):
        print(f"The shortest path to the vertex is: {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end = " ")
            actual_vertex = actual_vertex.predecessor

# test Dijkstra's algorithm
# Step 1: create nodes
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

# Step 2: create edges
nodeA.addEdge(6, nodeB) # parentNode.addEdge(distance, childNode)
nodeA.addEdge(10, nodeC) 
nodeA.addEdge(9, nodeD)

nodeB.addEdge(5, nodeD)
nodeB.addEdge(16, nodeE)
nodeB.addEdge(13, nodeF)

nodeC.addEdge(6, nodeD)
nodeC.addEdge(5, nodeH)
nodeC.addEdge(21, nodeG)

nodeD.addEdge(8, nodeF)
nodeD.addEdge(7, nodeH)

nodeE.addEdge(10, nodeG)

nodeF.addEdge(4, nodeE)
nodeF.addEdge(12, nodeG)

nodeH.addEdge(2, nodeF)
nodeH.addEdge(14, nodeG)

algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.getShortestPath(nodeG)
# NEED TO RESOLVE PROBLEMS IN THIS PROGRAM