def bmua(b):
    a=[]
    c=[]
    for i in range(1025):
        a.append(i)
    for i in range(len(a)):
        if b**a[i]<1025:
            c.append(b**a[i])
        else:
            break
    return c