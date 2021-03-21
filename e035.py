# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

from benchmark import timed
import pyprimesieve as pp

def rotations(n):
    yield n
    if n < 10:
        return
    s = str(n)
    for _ in range(len(s)-1):
        s = s[1:]+s[0]
        yield int(s)     

@timed
def count_circular_primes_below(n):
    #odds_only = lambda x : all( int(digit) in {1,3,5,7,9} for digit in str(x) )   
    #cache = set(filter(odds_only, set(pp.primes(n))))
    cache = set(pp.primes(n))
    is_circular = lambda x : all( int(p) in cache for p in rotations(x) ) 
    return sum(1 for _ in filter(is_circular, cache))

result = count_circular_primes_below(1000000)
print( result )