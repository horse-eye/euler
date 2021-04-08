# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from benchmark import timed
from math import sqrt

def get_primefactors(n):
    while n%2 == 0:
        yield 2
        n//=2
    for i in range(3, int(sqrt(n)+1),2):
        while n%i == 0:
            yield i
            n//=i
    if n>2: yield n 

@timed
def get_max_pf(n):
    return max(get_primefactors(n)) 


print ( get_max_pf(600851475143) )