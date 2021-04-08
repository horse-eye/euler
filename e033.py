# Digit cancelling fractions

import numpy as np
from math import prod

def get_dcf():
    for n in range (11,99):
        for d in range(n+1,100):
            sn, sd = str(n), str(d)
            if sn[0] == sd[0]:
                if int(sn[1])/int(sd[1]) == n/d:
                    yield (n,d)
            elif sn[0] == sd[1]:
                if int(sn[1])/int(sd[0]) == n/d:
                    yield (n,d) 
            elif sn[1] == sd[0]:
                if sd[1] != '0' and int(sn[0])/int(sd[1]) == n/d:
                    yield (n,d)
            elif sn[1] == sd[1] and not (sn[1]=='0' and sd[1]=='0' ):
                if sd[0] != '0' and int(sn[0])/int(sd[0]) == n/d:
                    yield (n,d)                          

tuples = list(get_dcf())
pn = prod( t[0] for t in tuples)
pd = prod( t[1] for t in tuples)
g = np.gcd(pn, pd)
print(pn, pd, g, pd/g)



'''
16/64
19/95
26/65
49/98
387296 / 38729600
== 1/100
'''