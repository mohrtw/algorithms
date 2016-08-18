from algorithms.dataStructures.UnionFind import NodeByRank, UnionFindByRank

from collections import namedtuple

# Edge represents an edge in a graph
# u and v are nodes
# cost is the cost of the edge

Edge = namedtuple('Edge', 'u v cost')


def KruskalCluster(G, uf, m, k):
    """
    KruskalCluster finds a maximum space k-clustering of a graph G
    and the spacing of that clustering
    
    G is a graph, a list of Edges
    uf is a UnionFind containing all of the Nodes in G
    m is the number of edges in G
    k is the number of clusters
    
    returns T, tot
    T is a list of the edges in the k-clustering
    spacing is the spacing of T
    """

    T = []
    spacing = 0

    # sort Edges by edge cost
    G.sort(key=lambda edge: edge.cost)

    # for each edge, add it to T if doing so would not
    # create a cycle in T
    for i in range(m):
        u, v, w = G[i]

        # check for a cycle by comparing the groups u and v
        # are in in the UnionFind
        if uf.Find(u)!=uf.Find(v):
            # add the edge to T
            # and merge the groups u and v belong to in uf
            T.append(G[i])
            uf.Union(u, v)

        if uf.clusters == k:
            break

    # find the spacing
    for e in G:
        u, v, w = e

        if uf.Find(u)!=uf.Find(v):
            spacing = w
            break
        
            
    return T, spacing    

if __name__ == '__main__':
    n = int(input())

    # create nodes and UnionFind
    ns = [NodeByRank() for _ in range(n)]
    uf = UnionFindByRank(ns)

    # add each edge in input to G
    G = []
    m = 0

    while True:
        try:
            inp = input()
        except EOFError:
            break

        u, v, w = [int(x) for x in inp.split()]

        e = Edge(ns[u-1], ns[v-1], w)
        G.append(e)
        m += 1

    T, spacing = KruskalCluster(G, uf, m, 4)

    print(spacing)


