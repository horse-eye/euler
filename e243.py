# We shall call a fraction that cannot be cancelled down a resilient fraction.
# Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its 
# proper fractions that are resilient; for example, R(12) = 4/11 .
# Find the smallest denominator d, having a resilience R(d) < 15499/94744 
from benchmark import timed
from fractions import Fraction
import numpy as np
import itertools as it

target = 15499/94744  #Fraction(15499,94744)

# FAIL
# Solution not found in ~1hr - will likely take a very long time

def R(d):
    if (d-1)%1000==0: print(d)
    result = 1
    start, step = 2,1
    #if d%2==0: # if both are even, no need to check
    #    start, step = 3,2
    for n in range(start,d,step):
        if np.gcd(n,d) == 1:
            result+=1
            if result/(d-1) >= target:
                return 0
    return d
    #return Fraction(result, d-1)    
    
@timed    
def find():
    iszero = lambda d: d==0
    return next(it.dropwhile(iszero, (R(n) for n in it.count(start=100001, step=2)))) 

result = find()
print(result)