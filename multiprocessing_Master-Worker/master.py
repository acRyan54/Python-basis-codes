import queue, random
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager): # 管理器类
    pass

def return_task_queue():
    global task_queue
    return task_queue
def return_result_queue():
    global result_queue
    return result_queue

def main():
    QueueManager.register('get_task_queue', callable = return_task_queue)
    QueueManager.register('get_result_queue', callable = return_result_queue)
    # 把实例的属性作为访问对象
    
    manager = QueueManager(address=('127.0.0.1', 8001), authkey=b'abc')
    manager.start()
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    
    # 添加任务
    for i in range(10):
        n = random.randint(0, 10)
        print("Put task %s ..." % n)
        task.put(n)
        
    print("Try get results...")
    # 取出结果
    for i in range(11):
        try:
            res = result.get(timeout = 6)
            print("Result: %s" % res)
        except queue.Empty:
            print("result queue is empty.")
            
    manager.shutdown()
    print("master exit.")
    
if __name__ == '__main__':
    freeze_support()
    print("Start!")
    main()
    
'''
Start!
Put task 2 ...
Put task 10 ...
Put task 2 ...
Put task 7 ...
Put task 10 ...
Put task 8 ...
Put task 6 ...
Put task 5 ...
Put task 3 ...
Put task 4 ...
Try get results...
Result: 2 * 2 = 4
Result: 10 * 10 = 100
Result: 2 * 2 = 4
Result: 7 * 7 = 49
Result: 10 * 10 = 100
Result: 8 * 8 = 64
Result: 6 * 6 = 36
Result: 5 * 5 = 25
Result: 3 * 3 = 9
Result: 4 * 4 = 16
result queue is empty.
master exit.
'''