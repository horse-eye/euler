from benchmark import timed

@timed
def euler2(f=[1,2],x=4000000):
    y = lambda l: l[-1] + l[-2]
    evens=0
    while ( yf:= y(f) ) < x:
        f.append(yf) 
        evens += yf if yf % 2 == 0 else 0
    return evens

result = euler2()
print( result )