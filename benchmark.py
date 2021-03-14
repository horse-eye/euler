import timeit

def time(label, func):
    t = timeit.Timer( func )
    print ( label + ": %.5f ms" % (t.timeit(1) * 1000)  )
    print()