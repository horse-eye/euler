"""A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""

import benchmark as bm
import itertools as it
import functools as ft

def lexicographic_permutation(N,idx):
    num = lambda seq: ft.reduce(lambda total, d: 10 * total + d, seq, 0)    
    x = next(it.islice(it.permutations(range(0,N+1)), idx-1, None), None)   
    return num(x)

x = lexicographic_permutation(9,1000000)
print(x)

bm.time("e24", lambda: lexicographic_permutation(9,1000000))