def merge(xs, ys):

    zs = []

    i, j = 0, 0
    n, m = len(xs), len(ys)

    while i < n or j < m:
        if i >= n:
            zs.append(ys[j])
            j += 1
        elif j >= m:
            zs.append(xs[i])
            i += 1
        else:
            if xs[i] <= ys[j]:
                zs.append(xs[i])
                i += 1
            else:
                zs.append(ys[j])
                j += 1

    return(zs)


def mergeSort(xs):

    n = len(xs)

    # basecase
    if n < 2:
        return xs

    if n == 2:
        if xs[1] < xs[0]:
            xs[0], xs[1] = xs[1], xs[0]

        return xs

    # sort partitions
    i = int(n/2)
    xs[:i] = mergeSort(xs[:i])
    xs[i:] = mergeSort(xs[i:])

    # merge partitions
    xs = merge(xs[:i], xs[i:])

    return xs
