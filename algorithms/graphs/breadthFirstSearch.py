import queue

from algorithms.dataStructures.graph import graph


def breadthFirstSearch(G, s):

    explore = {}

    q = queue.Queue()
    q.put(s)
    explore[s] = True

    while not q.empty():
        u = q.get()

        for arc in G.get_arcs(u):
            if not explore.get(arc, False):
                explore[arc] = True
                q.put(arc)

    return explore


def shortestDistance(G, s):
    explore = {}
    levels = {}

    q = queue.Queue()
    q.put(s)
    explore[s] = True
    levels[s] = 0

    while not q.empty():
        u = q.get()
        curLvl = levels[u]

        for arc in G.get_arcs(u):
            if not explore.get(arc, False):
                explore[arc] = True
                levels[arc] = curLvl + 1
                q.put(arc)

    return levels
