# Permuted multiples
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
from benchmark import timed
from itertools import count

def f(n):
    s = sorted(str(n))
    for i in range(2,7):
        if not s == sorted(str(i*n)):
            return False
    return True        

# For some reason, this is much slower (by almost 100%)
#return False if any( sorted(str(i*n)) != s for i in range(2,7) ) else True

@timed
def find():
    return next(filter(f,count(start=125875)))

result = find()
print(result)
