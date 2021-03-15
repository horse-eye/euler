import itertools as it
from math import sqrt

# Sieve of Eratosthenes
def prime_sieve(n=200000):
    A = [1 for i in range(2,n+1)]
    i, sq = 2, int(sqrt(n))+1
    while (i<sq):
        if A[i-2]:
            j = i**2
            while (j<=n):
                A[j-2]=0
                j+=i
        i+=1
    return [idx+2 for idx, p in enumerate(A) if p==1]

idx = 10001
x = next(it.islice(prime_sieve(), idx-1, None))
print (x)
