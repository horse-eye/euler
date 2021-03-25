# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, 
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import pyprimesieve as pp

def truncations(n):
    yield n
    if n < 10:
        return
    s = str(n)
    for _ in range(len(s)-1):
        s = s[1:]
        yield int(s) 
    s = str(n)
    for _ in range(len(s)-1):
        s = s[:-1]
        yield int(s)     

cache = set(pp.primes(1000000))
result = sum(n for n in cache if (n>7 and all(i in cache for i in truncations(n))))

print(result)
