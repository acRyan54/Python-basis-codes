import time, threading

# l = threading.Lock(), l.acquire(), l.release()
# 保证关键代码只由单线程执行

balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance # 提前声明才能对全局变量进行赋值
    balance = balance + n
    balance = balance - n

# def run_thread(n):
#     for i in range(2000000):
#         change_it(n)

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()  
        try:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
# 注意：try结束后的return/break会挂起，先执行finally中的内容 ==> 即finally中的内容一定会执行

if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    # t1 = threading.Thread(target=run_thread(5))
    # t2 = threading.Thread(target=run_thread(8))
    # 这样得到的target就是一个固定参数的新函数，生成这个函数时change_it()相当于被锁上了
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)