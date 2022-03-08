import time, functools

def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start_time = time.time()
        return_value = func(*args, **kw)
        end_time = time.time()
        print('Function: %s\nTime: %s ms. \nReturn Value: %s' % (func.__name__, (end_time - start_time) * 1000, return_value))
        return return_value
    return wrapper

@metric
def ssum(l):
    time.sleep(0.1234)
    ans = 0
    for x in l:
        ans = ans + x
    return ans

l = list(map(int, input().split()))
ssum(l)





        