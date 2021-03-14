import benchmark as bm

def euler1a(y=[3,5], n=1000):
    s=set({})
    r=lambda x:range(x,n,x)
    for i in y:
        s.update(r(i, n))
    return s

def euler1(y=[3,5], n=1000):
    rr=lambda x:range(x,n,x)
    return sum({item for i in y for item in rr(i)})



bm.time("euler1", lambda: euler1() )
