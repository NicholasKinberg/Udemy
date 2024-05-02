# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# Imagine you have a map with different cities connected by roads, each road having a certain distance. 
# The Bellman–Ford algorithm is like a guide that helps you find the shortest path from one city to all other cities, even if some roads have negative lengths. 
# It’s like a GPS for computers, useful for figuring out the quickest way to get from one point to another in a network.
# pseudocode
    # if distance of destination vertex > distance of source vertex + weight between source and destination vertex:
        # update distance of destination vertex to (distance of source vertex + weight between source and destination vertex)
# pseudocode works to optimize path and weight between source vertex and destination vertex
# number of iterations = number of vertices - 1
    # if any node achieves better distance in previous iteration, then that better distance is used to improve distance of other vertices
    # identify worst case graph that can be given to us
# treat negatives normally, not reversing flows
class Graph:
    def __init__(self, vertices):
        self.V = vertices # variable for vertices
        self.graph = [] # variable to store graph
        self.nodes = [] # variable to store individual nodes

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w]) # append source, destination, weights, all part of edge
    
    def addNode(self, value):
        self.nodes.append(value) # append nodes
    
    def printSolution(self, dist):
        print("Vertex Distance from Source")
        for key, value in dist.items():
            print('  ' + key, ' :   ', value) # print node and distance from node A to node B, eventually reaching destination node
    
    def bellmanFord(self, src):
        dist = {i : float("Inf") for i in self.nodes} # dictionary of floats where "Inf" is replaced with i in self.nodes, i being distance
        dist[src] = 0 # beginning distance is 0 because distance from source node to source node is 0 (src = source)
        for _ in range(self.V-1): # for indefinite number of iterations in range(self.V-1) (number of iterations = number of vertices - 1)...
            for s, d, w in self.graph: #...for source, destination, weight in self.graph...
                if dist[s] != float("Inf") and dist[s] + w < dist[d]: #...if distance from source doesn't equal float and distance from source + weight is less than distance to destination...
                    dist[d] = dist[s] + w #...destination distance is reassigned to distance from source + weight to optimize path
        for s, d, w in self.graph: # for source, destination, weight in self.graph...
            if dist[s] != float("Inf") and dist[s] + w < dist[d]: #...if distance from source doesn't equal float and distance from source + weight is less than distance to destination...
                print("Graph contains negative cycle") #...return graph contains negative cycle
                return # note that this code will run if even after the if statement in line 34 doesn't produce most efficient path, lines 36-38 will run to consider negative paths
        self.printSolution(dist) # then print solution

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "C", 6)
g.addEdge("A", "D", 6)
g.addEdge("B", "A", 3)
g.addEdge("C", "D", 1)
g.addEdge("D", "C", 2)
g.addEdge("D", "B", 1)
g.addEdge("E", "B", 4)
g.addEdge("E", "D", 2)
g.bellmanFord("E")