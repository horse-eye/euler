
from benchmark import timed

digits = ([ *range(1,21),30,40,50,60,70,80,90]) 
words = ['one','two','three','four','five','six','seven','eight','nine','ten',
'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen',
'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

d = dict(zip(digits , words))

def translate(n):
    
    if n <= 20 or (n<100 and n%10==0):
        return d[n]
    
    if n==1000:
        return 'onethousand'

    if n%100 == 0:
        return d[n//100] + 'hundred'

    if n>20 and n<100:
        return ''.join([d[n//10 * 10],d[n%10]])    

    if n>100 and n<1000:
        h = d[n//100] + 'hundred'
        r = n%100
        t = ''.join([d[r//10 * 10],d[r%10]]) if (r>20 and r%10>0) else d[r]
        return 'and'.join([h,t])

    return '??'

x = sum( len(s) for s in (translate(n) for n in range(1,1001)) )
print(x)