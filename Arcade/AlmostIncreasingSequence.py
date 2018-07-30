'''Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.'''def almostIncreasingSequence(sequence):
    org=list(sequence)
    check=0
    for j in range(1,len(org)-1):
        if org[j]>=org[j+1]:
            check+=1
        if org[j-1]>=org[j+1]:
            check+=1
    if org[0]>=org[1]:
        check+=1

    if check>2:
        return False
    else:
        return True
