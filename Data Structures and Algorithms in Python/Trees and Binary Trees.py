# tree is nonlinear data structure with hierarchical relationships between its elements without having any cycle, basically reversed from real-life tree
# tree is like a menu: you want coffee -> size -> flavor -> etc.
# properties:
    # represents hierarchical data
    # each node has 2 components: data and link to its subcategory
    # base category and subcategories under it
class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children # initialize TreeNode class by adding functionality to add children as tree nodes
    
    def __str__(self, level=0):
        ret = "   " * level + str(self.data) + "\n" # inserts line break so it goes to next level below; notice no space at level 0 so tree parent is lonely
        # treat the above line of code as adding an indent for your tree
        for child in self.children: # adds child rows for however many rows of children
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode) # appends TreeNode to children

# tree = TreeNode('Drinks', [])
# cold = TreeNode('Cold', [])
# hot = TreeNode('Hot', [])
# tree.addChild(cold)
# tree.addChild(hot)
# coffee = TreeNode('Coffee', [])
# hotChocolate = TreeNode('Hot Chocolate', [])
# soda = TreeNode('Soda', [])
# sangria = TreeNode('Sangria', [])
# hot.addChild(coffee)
# hot.addChild(hotChocolate)
# cold.addChild(soda)
# cold.addChild(sangria)
# print(tree)

# binary trees are trees that have at most two children per node