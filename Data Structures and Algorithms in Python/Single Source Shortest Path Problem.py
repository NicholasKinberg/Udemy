# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# single source shortest path (SSSP) problem: find path between a given vertex (called source) to all other vertices in graph such that total distance between them (source and destination) is minimum
    # BFS
        # enqueue any starting vertex
        # while queue is not empty
            # p = dequeue()
            # if p is unvisited
                # mark it visited
                # enqueue all adjacent unvisited vertices of p
                # update parent of adjacent vertices to curVertex

        # BFS doesn't work with weighted graph, DFS doesn't work for SSSP
            # BFS doesn't consider edge weights, so as a result, BFS can't produce SSSP with weighted edges
            # DFS, can only tweak order in which children are investigated, normal DFS proceeds in arbitrary order, i.e. the order in which children are stored
    # Dijkstra's Algorithm
    # Bellman Ford
class Graph:
    def __init__(self, gdict=None): # initializing graph class with dictionary
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def bfs(self, start, end):
        queue = [] # initializing queue variable
        queue.append([start]) # append starting index position
        while queue: # while loop
            path = queue.pop(0) # path of queue pops first index position on each iteration of while loop
            node = path[-1] # node is the last node of the path list
            if node == end: # if node equals end of BFS as provided by user, program will return path
                return path
            for adjacent in self.gdict.get(node, []): # for adjacent nodes (last index position as provided by path[-1]), retrieve last node key and value (first argument in get() is key, second is value, which is empty in this case)
                new_path = list(path) # new_path is assigned to list of path
                new_path.append(adjacent) # append adjacent nodes to produce queue of visited nodes for BFS
                queue.append(new_path) # then append those nodes stored in new_path list

customDict =   {'A':['B','C'], 
                'B':['A','D','E'],
                'C':['A','E'],
                'D':['B','E','F'],
                'E':['C','D','F'],
                'F':['D','E']}