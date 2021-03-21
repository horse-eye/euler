# Longest Collatz sequence
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Which starting number, under one million, produces the longest chain?

from benchmark import timed

cache = dict()

def collatz(N):
    i,n = 0, N
    while n>1:
        if n in cache:  # Memoized, avoiding recalculating sub-chain if known already
            cache[N] = i+cache[n]
            return i+cache[n]
        n = n//2 if n%2==0 else n*3+1
        i+=1
    cache[N] = i
    return i    

@timed
def max_collatz():
    return max (( (n, collatz(n)) for n in range(2,1000000) ), key=lambda t: t[1])

print (max_collatz())
