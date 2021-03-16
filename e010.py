#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
from math import sqrt
import benchmark as bm
import pyprimesieve as pp

# Sieve of Eratosthenes
def sieve_sum(limit=2000000):
    A = [1 for i in range(2,limit+1)]
    i, sq = 2, int(sqrt(limit))+1
    while (i<sq):
        if A[i-2]:
            j = i**2
            while (j<=limit):
                A[j-2]=0
                j+=i
        i+=1
    return sum(idx+2 for idx, p in enumerate(A) if p==1)

# Just for fun
# ~900 times faster than sieve above
def ps_sum_super(limit=2000000):
    return pp.primes_sum(limit)


print(sieve_sum())
print(ps_sum_super())

bm.time("me", sieve_sum)
bm.time("pyprime", ps_sum_super)    