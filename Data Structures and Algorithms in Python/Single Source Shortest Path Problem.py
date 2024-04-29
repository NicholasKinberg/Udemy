# single source shortest path (SSSP) problem: find path between a given vertex (called source) to all other vertices in graph such that total distance between them (source and destination) is minimum
    # BFS
        # enqueue any starting vertex
        # while queue is not empty
            # p = dequeue()
            # if p is unvisited
                # mark it visited
                # enqueue all adjacent unvisited vertices of p
                # update parent of adjacent vertices to curVertex
    # Dijkstra's Algorithm
    # Bellman Ford