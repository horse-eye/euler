import timeit
from time import process_time

def time(label, func):
    t = timeit.Timer( func )
    print ( label + ": %.5f ms" % (t.timeit(1) * 1000)  )
    print()

def timed(func):
    ''' Prints the execution time of a function in milliseconds, using timeit default timer'''   
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        end = timeit.default_timer()
        exec_time = (end - start)*1000
        print(func.__name__ + ": %.5f ms (decor)" % exec_time)
        return result
    return wrapper    