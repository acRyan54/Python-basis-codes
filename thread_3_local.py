import threading, multiprocessing

# 每个线程对应一个独立的”同名“变量, 避免函数一直传递同一个变量
# global_dict = {}
# global_dict[threading.current_thread()] = std

# ThreadLocal对象是全局变量，属性与线程有关（像实例
'''
>>> type(l)
<class '_thread._local'> 说明这是实例!!
'''


thread_dict = threading.local()

def process_student():
    name = thread_dict.student
    print('Thread_Name:%s >>> Student_Name:%s' % (threading.current_thread().name, name))


def runThread(name):
    thread_dict.student = name
    process_student()
    
if __name__ == '__main__':
    t1 = threading.Thread(target = runThread, args = ('Apple',), name = 'Thread_A')
    t2 = threading.Thread(target = runThread, args = ('Boy',), name = 'Thread_B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()