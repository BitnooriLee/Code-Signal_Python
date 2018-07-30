'''Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!'''

def sortByHeight(a):
    for i in range(len(a)):
        if a[i]!=-1:
            for j in range(len(a)-i):
                if a[i]>a[i+j]:
                    if a[i+j]!=-1:
                        a[i],a[i+j]=a[i+j],a[i]
    return a
