# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from benchmark import timed
import itertools as it

def pan_prods():
    cache = set(int(''.join(i)) for i in it.permutations(str(123456789)))
    is_pan = lambda a,b,c: int(str(a)+str(b)+str(c)) in cache
    for a in range(1,10):
        for b in range(9876,1234,-1):
            c = a*b
            if is_pan(a,b,c): 
                yield c #(a,b,c)
    for a in range(10,100):
        for b in range(987,123,-1):
            c = a*b
            if is_pan(a,b,c): 
                yield c #(a,b,c)

@timed
def sum_pans():
    return sum({p for p in pan_prods()})

result = sum_pans()
print(result)