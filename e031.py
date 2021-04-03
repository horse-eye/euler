from benchmark import timed

coins = [1,2,5,10,20,50,100,200]
solutions=0

class Bag:
    def __init__(self):
        self.stack = []
        self.sum=0

    def push(self, x):
        self.sum += x
        self.stack.append(x)

    def pop(self):
        x = self.stack.pop()
        self.sum -= x
        return x

# CPython: 5,600ms
# PyPy: 400ms
def find(idx, bag, target):
    global solutions
    for i in range(idx, -1, -1):

        coin = coins[i]

        if coin > target:
            continue

        if bag.sum + coin <= target:
            bag.push(coin)

        if bag.sum == target:
            solutions += 1
            bag.pop()
            continue

        find( i-1 if bag.sum + coin > target else i, bag, target)
        bag.pop()   

# Same logic without using a class
# 50% faster on CPython, but slightly slower on PyPy 
def find2(idx, stack, sum, target):
    global solutions
    for i in range(idx, -1, -1):

        coin = coins[i]

        if coin > target:
            continue

        if sum + coin <= target:
            stack.append(coin)
            sum += coin

        if sum == target:
            solutions += 1
            sum -= stack.pop()
            continue

        find2(i-1 if sum + coin > target else i, stack, sum , target)
        sum -= stack.pop()  


@timed
def find_ways_to_make(n):
    global solutions
    solutions = 0
    find2( len(coins)-1, [], 0, n)
    return solutions

print(find_ways_to_make(200))





