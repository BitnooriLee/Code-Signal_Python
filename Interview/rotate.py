def rotateImage(a):
    import copy
    b = copy.deepcopy(a)
    for i in range(len(a)):
        for j in range(len(a)):
            print(i,j)
            b[j][len(a)-1-i] = a[i][j]
    return b
