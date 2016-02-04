def quickSort(xs):
    n = len(xs)

    # basecase
    if n<2:
        return xs

    if n==2:
        if xs[1]<xs[0]:
            xs[0], xs[1] = xs[1], xs[0]
    
        return xs
        
    pivot = xs[0]

    # partition
    leftPartition = []
    rightPartition = []

    for i in range(1,n):
        if xs[i] < pivot:
            leftPartition.append(xs[i])
        else:
            rightPartition.append(xs[i])
            
    # sort partitions
    leftPartition = quickSort(leftPartition)
    rightPartition = quickSort(rightPartition)
    
    xs = leftPartition
    xs.append(pivot)
    xs.extend(rightPartition)
    
    return xs
