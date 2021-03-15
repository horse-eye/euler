#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
import itertools as it
import benchmark as bm
from pyprimesieve import primes_nth
from math import sqrt

# Sieve of Eratosthenes
def sieve_nth(nth, limit=200000):
    A = [1 for i in range(2,limit+1)]
    i, sq = 2, int(sqrt(limit))+1
    while (i<sq):
        if A[i-2]:
            j = i**2
            while (j<=limit):
                A[j-2]=0
                j+=i
        i+=1
    seq = (idx+2 for idx, p in enumerate(A) if p==1)
    return next(it.islice(seq, idx-1, None))

# Just for fun
# ~750 times faster than sieve above
def ps_nth_super(nth):
    return primes_nth(nth)

idx = 10001
print (sieve_nth(idx))
print(ps_nth_super(idx))

bm.time("me", lambda: sieve_nth(idx))
bm.time("pyprime", lambda: ps_nth_super(idx))