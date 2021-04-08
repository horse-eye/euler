# Considering quadratics of the form: n^2 + an + b, 
# where |a|<1000 and |b| <= 1000
# Find a*b for the expression that produces the maximum number of primes for consecutive values of n starting with 0.
from benchmark import timed
import pyprimesieve as pp


@timed
def maximise_quad():
    max_seq = A = B = 0
    quad = lambda n,a,b : n*n + a*n + b
    cache = set(pp.primes(100000))
    for a in range(-999,1000,1):
        for b in range(-1000,1001,1):
            n=0
            while (x:=quad(n,a,b)) in cache:
                n+=1
            if n>max_seq:
                A,B,max_seq = a,b,n
    
    return (max_seq, A, B, A*B)
    

print(maximise_quad())
