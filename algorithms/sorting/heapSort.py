import heapq as hq

def heapSort(xs):    
    hq.heapify(xs)

    ys = []

    while xs:
        ys.append(hq.heappop(xs))
    
    return ys