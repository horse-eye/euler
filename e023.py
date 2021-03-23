import math
from benchmark import timed

#y = [n / i for i in r if n%i==0]
#x = [n/i for i in y]
def sumdivs(n):    
    sq, s = int(math.sqrt(n)), 1 
    for x in (n/i for i in range(2,sq+1) if n%i==0):
        s += x
        y = n/x
        if y!=x: s+=y 
    return s

def ab(n=28112):
    for r in range(12,n):
        if sumdivs(r)>r: yield r

def absums():
    abs = list(ab())
    return {a+b for a in abs for b in abs} 

@timed
def e23():
    sums = absums()
    return sum(r for r in range(1,28123+1) if not r in sums)

print (e23())

