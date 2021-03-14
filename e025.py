def euler25(f=[1,1],n=3):
    y = lambda l: l[-1] + l[-2]
    while ( yf:= y(f) ) > 1:
        if len(str(yf)) >= n:
            return len(f)+1;
        else:
            f.append(yf) 


            
i = euler25([1,1],1000)
print(i)

t = timeit.Timer( lambda: euler25() )
pt(t, "Euler25")