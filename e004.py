#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import benchmark as bm

def max_pn():
    r = range(999,100,-1)
    ispn = lambda x : x[:3] == x[-3:][::-1]
    return max(a*b for a in r for b in r if ispn(str(a*b)))

print ( max_pn() )
bm.time("e4", max_pn)