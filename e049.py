#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
# (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#What 12-digit number do you form by concatenating the three terms in this sequence?
import benchmark as bm
import pyprimesieve as pp
import itertools as it

step, limit = 3330, 9999
primes = set(pp.primes(limit))

def prime_perms():
    isperm = lambda a,b: str(a) in map(''.join, it.permutations(str(b))) # should check c as well
    for a in range(1000,limit-step*2):
        p = sorted(primes.intersection(range(a, limit+1, step))) 
        if len(p)>2 and isperm(p[0],p[1]): 
            yield ''.join(str(i) for i in p)

result = list(prime_perms())
print( result )

quit()
