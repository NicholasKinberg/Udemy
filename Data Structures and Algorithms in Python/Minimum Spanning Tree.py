# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# minimum spanning tree (MST) is subset of edges of connected, weighted, and undirected graph which:
    # connects all vertices together
    # no cycle
    # minimum total edge

# real life example of needing to connect 5 islands but wanting to minimize cost of building bridges between all 5 islands

# disjoint set is data structure that keeps track of set of elements which are partitioned into number of disjoint and non-overlapping sets and each set has representative which identifies that set
    # make set
        # makeSet(N): used to create initial set
    # union
        # union(x,y): merge 2 given sets
    # find set
        # findSet(x): returns set name in which this element is there

class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0) # fromkeys(keys, value)
    
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot # assign xroot to greater yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot # assign yroot to greater xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1 # else increase xroot by 1 if xroot == yroot

vertices = ["A", "B", "C", "D", "E"]
ds = DisjointSet(vertices)
ds.union("A", "B")
ds.union("A", "C")
print(ds.find("A"))