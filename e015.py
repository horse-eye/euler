
from benchmark import timed

cache = {}
def count_paths(x,y):
    
    if (x,y) in cache:
        return cache[(x,y)]
    
    if x==0 or y == 0:
        return 1    
    
    xx = count_paths(x-1, y)
    cache[(x-1,y)] = xx

    yy = count_paths(x, y-1) 
    cache[(x,y-1)] = yy

    return xx+yy

@timed
def driver(n):
    return count_paths(n,n)

print (driver(20))
