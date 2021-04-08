# Reciprocal cycles
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def cycle(n):
    rem = 1%n
    remainders = {rem}
    while True:
        d = (rem*10)//n
        rem = (rem * 10) % n
        yield d
        if rem in remainders: break
        remainders.add(rem)

def driver(n):
    result = list(cycle(n))
    return n, len(result)

result = max((driver(n) for n in range(1,1000)), key= lambda t: t[1])
print (result)
