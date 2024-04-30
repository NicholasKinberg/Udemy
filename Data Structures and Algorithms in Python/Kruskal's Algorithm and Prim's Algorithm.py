# In Kruskal’s algorithm, sort all edges of the given graph in increasing order. 
# Then it keeps on adding new edges and nodes in the MST if the newly added edge does not form a cycle. 
# It picks the minimum weighted edge at first and the maximum weighted edge at last. 
# Thus we can say that it makes a locally optimal choice in each step in order to find the optimal solution. 
# Hence this is a Greedy Algorithm (locally optimal solution).

# Like Kruskal’s algorithm, Prim’s algorithm is also a Greedy algorithm. 
# This algorithm always starts with a single node and moves through several adjacent nodes, in order to explore all of the connected edges along the way.
# The algorithm starts with an empty spanning tree. 
# The idea is to maintain two sets of vertices. 
# The first set contains the vertices already included in the MST, and the other set contains the vertices not yet included. 
# At every step, it considers all the edges that connect the two sets and picks the minimum weighted edge from these edges. 
# After picking the edge, it moves the other endpoint of the edge to the set containing MST. 