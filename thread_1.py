import time, threading

# t = threading.Thread(target=x, name=x)
# threading.current_thread().name

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(0.1)
    print('thread %s ended.' % threading.current_thread().name)

if __name__ == '__main__':
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name = 'Sub-Thread') #否则为Thread-1
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)
    
'''
thread MainThread is running...  # 主线程默认为MainThread
thread LoopThread is running...
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread ended.
thread MainThread ended.
'''