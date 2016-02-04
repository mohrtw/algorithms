def insertionSort(xs):
    n = len(xs)

    for i in range(1,n):
        j = i
        while j>0 and xs[j-1] > xs[j]:
            xs[j], xs[j-1] = xs[j-1], xs[j]
            j -= 1
    
    return xs