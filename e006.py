#The sum of the squares of the first ten natural numbers is, 385
#The square of the sum of the first ten natural numbers is, 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
from benchmark import timed

@timed
def e6(N=100):
    nums = range(1,N+1)
    sq = lambda n: n*n
    return sq(sum(n for n in nums)) - sum(sq(n) for n in nums)

x = e6(100)
print(x)