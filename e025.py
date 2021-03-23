# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

from benchmark import timed

@timed
def euler25(f=[1,1],n=3):
    y = lambda l: l[-1] + l[-2]
    while ( yf:= y(f) ) > 1:
        if len(str(yf)) >= n:
            return len(f)+1;
        else:
            f.append(yf) 
            
i = euler25([1,1],1000)
print(i)