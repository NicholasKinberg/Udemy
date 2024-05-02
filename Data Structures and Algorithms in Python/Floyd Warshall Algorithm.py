# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# It is used to find the shortest paths between all pairs of nodes in a weighted graph. 
# This algorithm is highly efficient and can handle graphs with both positive and negative edge weights, making it a versatile tool for solving a wide range of network and connectivity problems.
# floyd warshall computes distance between all vertices whereas dijkstra and bellman ford only do so for one vertex going to all
# floyd warshall never runs loop twice via same vertex, so floyd warshall can never detect negative cycle
INF = 9999 # make-shift infinite value
def printSolution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ") # if distance is a loop that sums to 9999, set to INF
            else:
                print(distance[i][j], end = " ")
        print(" ")

def floydWarshall(nV, G):
    distance = G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j]) # compute minimum distance between all nodes
    printSolution(nV, distance)

G = [
    [0, 8, INF, 1],
    [INF, 0, 1, INF],
    [4, INF, 0, INF],
    [INF, 2, 9, 1]
     ]

floydWarshall(4, G)