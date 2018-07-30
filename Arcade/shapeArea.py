'''https://app.codesignal.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ

Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.'''


def shapeArea(n):
    Area=1
    for i in range(1,n+1):
        Area+=(i-1)*4
    return Area
