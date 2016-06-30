class Node:
    """
    Node represents a node in a linked list
    
    root is the root of the linked list
    child is the next node in the linked list
    """
    root = None
    child = None
    
    def __init__(self):
        self.root = self

class UnionFind:
    """
    UnionFind represents the UnionFind data structure
    
    nodes is a set of nodes in the UnionFind
    
    functions:
    Find(x) returns the subset to which the node x belongs
    Union(x, y) joins the subsets to which x and y belong
        into a single subset
    """
    
    def __init__(self, nodes):
        self.nodes = nodes

    def Find(self, x):
        """
        Find(x) returns the subset to which the node x belongs
        
        x is a node in self
        """
        if x in self.nodes:
            return x.root
        else:
            raise KeyError(str(x) + " is not in self.nodes.")

    def Union(self, x, y):
        """
        Union(x, y) joins the subsets to which x and y belong
        into a single subset
        
        x is a node in self
        y is a node in self
        """
        xroot = x.root
        xlast = x.root

        while xlast.child != None:
            xlast = xlast.child

        yroot = y.root
        xlast.child = y.root

        curnode = yroot
        while curnode != None:
            curnode.root = xroot
            curnode = curnode.child

