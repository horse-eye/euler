import benchmark as bm

def euler1(y=[3,5], n=1000):
    rr=lambda x:range(x,n,x)
    return sum({item for i in y for item in rr(i)})

print(euler1([3,5],1000))

bm.time("euler1", lambda: euler1() )