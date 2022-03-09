import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue') # 只需属性名称一致
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print("Connet to server %s..." % server_addr)
manager = QueueManager(address=(server_addr, 8001), authkey=b'abc')
manager.connect()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    try:
        n = task.get(timeout=1)
        print("run task %d * %d..." % (n, n))
        res = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(res)
    except queue.Empty:
        print("task queue is empty.")

print("worker exit.")

'''
Connet to server 127.0.0.1...
run task 2 * 2...
run task 10 * 10...
run task 2 * 2...
run task 7 * 7...
run task 10 * 10...
run task 8 * 8...
run task 6 * 6...
run task 5 * 5...
run task 3 * 3...
run task 4 * 4...
worker exit.
'''