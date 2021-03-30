from benchmark import timed

@timed
def spiral(N):
    SE = SW = NW = NE = 1
    yield 1
    for n in range(0,N//2):
        step=n*8
        SE += 2 + step
        SW += 4 + step
        NW += 6 + step
        NE += 8 + step
        
        yield SE
        yield SW
        yield NW
        yield NE
        #print(SE,SW,NW,NE)

result = sum(spiral(1001))
print(result)
