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

def merge(xs, ys):
    zs = []    

    i, j = 0, 0
    n, m = len(xs), len(ys)

    while i<n or j<m:
        if i>=n:
            zs.append(ys[j])
            j += 1
        elif j>=m:
            zs.append(xs[i])
            i += 1
        else:
            if xs[i]<=ys[j]:
                zs.append(xs[i])
                i += 1
            else:
                zs.append(ys[j])
                j += 1
    
    return(zs)