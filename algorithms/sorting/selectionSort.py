def selectionSort(xs):
    n = len(xs)

    for i in range(n):
        curMin = xs[i]
        curMinIndex = i
        
        for j in range(i+1,n):
            if xs[j]<curMin:
                curMin = xs[j]
                curMinIndex = j
                
        xs[i], xs[curMinIndex] = xs[curMinIndex], xs[i]
        
    return xs