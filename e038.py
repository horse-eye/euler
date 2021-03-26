from benchmark import timed
import itertools as it

def pandigital_multiples():
    cache = set(int(''.join(i)) for i in it.permutations(str(123456789)))
    is_pan = lambda seq: int(''.join(str(i) for i in seq)) in cache
    prods = lambda i,n: [i*n for n in range(1,n+1)]
    for a in range(9999,1,-1):
        for n in range(2,3 if a > 999 else 10):
            seq = prods(a, n)
            if is_pan(seq): 
                yield int(''.join(str(i) for i in seq))
@timed
def res():
    return max(pandigital_multiples())

print(res())


