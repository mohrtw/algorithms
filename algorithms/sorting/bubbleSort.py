def bubbleSort(xs):
    n = len(xs)    

    swapped = True
    
    while swapped:
        swapped = False
        
        for i in range(1,n):
            if xs[i]<xs[i-1]:
                xs[i], xs[i-1] = xs[i-1], xs[i]
                swapped = True
    
    return xs