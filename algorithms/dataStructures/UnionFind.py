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


class NodeByRank:
    """
    NodeByRank represents a node in a UnionFind
    
    root is the root of the linked list
    rank is the next rank of the node in the tree
    """
    root = None
    child = None
    
    def __init__(self):
        self.root = self
        self.rank = 0


class UnionFindByRank:
    """
    UnionFindByRank represents the UnionFind data structure
    using rank
    
    nodes is a set of nodes in the UnionFindByRank
    clusters is the number of clusters
    
    functions:
    Find(x) returns the subset to which the node x belongs
    Union(x, y) joins the subsets to which x and y belong
        into a single subset
    """
    
    def __init__(self, nodes):
        self.nodes = nodes
        self.clusters = len(nodes)

    def Find(self, x):
        """
        Find(x) returns the subset to which the node x belongs
        
        x is a node in self
        """
        if x in self.nodes:
            if x is not x.root:
                x.root = self.Find(x.root)
        else:
            raise KeyError(str(x) + " is not in self.nodes.")

        return x.root

    def Union(self, x, y):
        """
        Union(x, y) joins the subsets to which x and y belong
        into a single subset
        
        x is a node in self
        y is a node in self
        """
        xroot = self.Find(x)
        yroot = self.Find(y)

        if xroot is yroot:
            return

        if xroot.rank < yroot.rank:
            xroot.root = yroot
        elif xroot.rank > yroot.rank:
            yroot.root = xroot
        else:
            yroot.root = xroot
            xroot.rank += 1

        self.clusters -= 1

