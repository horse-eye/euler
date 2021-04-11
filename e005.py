# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import numpy as np
from benchmark import timed

@timed
def euler5(n): 
    seq = range(1,n+1)
    y = lambda x: any(x%i > 0 for i in seq)
    x = xf = seq[-1] * seq[-2]
    while(x:=x+xf)>1:
        if not y(x): return x

@timed
def euler5p(n): 
    seq = range(1,n+1)
    y = lambda x: any(x%i > 0 for i in seq)
    x = xf = 19 * 17 * 13 * 11 * 7 * 5 * 3 # use custom factor (not general case)
    while(x:=x+xf)>1:
        if not y(x): return x

@timed
def euler5np(n):
    seq = np.arange(1,21)
    return np.lcm.reduce(seq)

print(euler5(20))
print(euler5p(20))
print(euler5np(20))
