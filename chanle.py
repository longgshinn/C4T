def chanle(n):
    a=[2]
    for i in range(1,n):
        if i%2==0:
            a.append(a[i-2]-0.5)
        else:
            a.append(-1)
    return a