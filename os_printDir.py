# 打印目录
import os

def printDir(path):
    os.chdir(path)
    for x in [x for x in os.listdir('.') if os.path.isfile(x)]:
        print(os.path.join(path, x))
    for x in [x for x in os.listdir('.') if os.path.isdir(x)]:
        next_path = os.path.join(path, x)
        printDir(next_path)
        
def main():
    path = input('打印路径:')
    printDir(path)
    
if __name__ == '__main__':
    main()