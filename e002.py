# Even Fibonacci numbers
# Considering terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
from benchmark import timed

@timed
def even_fibs(f=[1,2],x=4000000):
    y = lambda l: l[-1] + l[-2]
    evens=0
    while ( yf:= y(f) ) < x:
        f.append(yf) 
        evens += yf if yf % 2 == 0 else 0
    return evens

result = even_fibs()
print( result )