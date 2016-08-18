from algorithms.dataStructures.UnionFind import Node, UnionFind

# Edge represents an edge in a graph
# u and v are nodes
# cost is the cost of the edge

Edge = namedtuple('Edge', 'u v cost')


def KruskalMST(G, uf, m):
    """
    KruskalMST finds a minimum spanning tree of a graph G
    and the total cost of that tree
    
    G is a graph, a list of Edges
    uf is a UnionFind containing all of the Nodes in G
    m is the number of edges in G
    
    returns T, tot
    T is a list of the edges in the MST
    tot is the toal cost of T
    """

    T = []
    tot = 0

    # sort Edges by edge cost
    G.sort(key=lambda edge: edge.cost)

    # for each edge, add it to T if doing so would not
    # create a cycle in T
    for i in range(m):
        u, v, w = G[i]

        # check for a cycle by comparing the groups u and v
        # are in in the UnionFind
        if uf.Find(u)!=uf.Find(v):
            # add the edge to T, add its cost to tot
            # and merge the groups u and v belong to in uf
            T.append(G[i])
            tot += w
            uf.Union(u, v)

    return T, tot    
