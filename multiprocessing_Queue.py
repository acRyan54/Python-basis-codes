from multiprocessing import Process, Queue
import os
import time
import random
# TODO:对阻塞的理解有欠缺
# 写数据进程执行的代码:

# q = Queue(), q.put(), q.get()

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get()   #(Block == True) 如果此时队列为空，则wait等待生产者线程添加数据
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    child_w = Process(target=write, args=(q,))  # 记得把queue传到子进程里
    child_r = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    child_w.start()
    # 启动子进程pr，读取:
    child_r.start()
    # 等待pw结束:
    child_w.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    child_r.terminate()
