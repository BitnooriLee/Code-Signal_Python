'''https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.'''

def adjacentElementsProduct(inputArray):
    a=[]
    for i in range(0,len(inputArray)-1):
        a.append(inputArray[i]*inputArray[i+1])
    return max(a)
