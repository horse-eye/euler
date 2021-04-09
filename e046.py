# Goldbach's other conjecture
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from benchmark import timed
import pyprimesieve as pp
from itertools import takewhile

# Let's define some arbitrary limit
N = 10000

@timed
def find_goldbach():
    primes = pp.primes(N)
    cache = set(primes)
    sq2 = [2*(n*n) for n in range(1,N)]
    i = 9
    while(i<N):
        if not i in cache:
            lt = lambda x : x < i
            result = False
            for a in takewhile(lt, sq2):
                for b in takewhile(lt, primes):
                    if a+b == i:
                        result = True
                        break
                if result:
                    break    
            if not result:
                return i
        i+=2

result = find_goldbach()
print(result)