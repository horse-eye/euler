import math
import benchmark as bm

def d(n):    
    sq, s = int(math.sqrt(n)), 1 
    for x in (n/i for i in range(2,sq+1) if n%i==0):
        s += x
        y = n/x
        if y!=x: s+=y 
    return s

def e021():

    x = { r:d(r) for r in range(2,10000) }
    s=0
    for key in x:
        v = x[key]
        if v in x and v != key and x[v] == key:
            s += key
    return s

print(e021())

bm.time("e21", lambda: e021())