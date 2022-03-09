from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    
    p = Process(target=run_proc, args=('test',))  # 传入函数和参数(tuple)
    
    print('Child process will start.')
    p.start()
    p.join() # 回到原进程
    print('Child process end.')