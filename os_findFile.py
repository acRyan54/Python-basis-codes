'''
import.os

os.path.abspath('.') 查看当前绝对路径
os.getcwd() 同上
os.chdir(path) 切换工作目录

os.mkdir('xxxx')    os.rmdir('xxxx')  对文件夹进行操作

os.path.join('xxx', 'xxx')  对路径的str进行操作
os.path.split('asdf')    os.path.splitext('xsdfsdf')  分成list[0,1]

os.listdir('.')  可以列出文件夹和文件

os.path.isfile('xx')   os.path.isdir('xx')

过滤文件:     [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
'''

# 搜索文件夹
import os

def findFile(s, path):
    os.chdir(path)
    # 搜索目录下文件
    for x in [x for x in os.listdir('.') if os.path.isfile(x)]:
        if x.find(s) != -1:
            print(os.path.join(path, x))
    # 搜索目录下文件夹
    l = [x for x in os.listdir('.') if os.path.isdir(x)]
    if l == []:
        return # 递归的返回条件
    for x in l:
        next_path = os.path.join(path, x)
        findFile(s, next_path)

def main():
    path = input('查找目录:')
    s = input('搜索字符串:')
    findFile(s, path)
    
if __name__ == '__main__':
    main()
    
        