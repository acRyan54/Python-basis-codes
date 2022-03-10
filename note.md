0. FIXME: Shift+Enter 直接copy到下方用python互动式命令行运行; Ctrl+Alt+N 在下方用cmd运行代码
1. [python3中比较麻烦的import](https://zhuanlan.zhihu.com/p/63143493) 绝对引用和相对引用
2. [递归与循环的改写](https://www.zhihu.com/question/20418254?sort=created)
3. [输入一行数字的处理方法](https://blog.csdn.net/weixin_39613291/article/details/109872736)
   采用map(f, list)函数,来对list(或者tuple, str)中的每个元素进行f(函数)操作,生成一个新的list.. 
   而str.split('',num),则是通过指定分隔符(num个,默认为-1)对str进行拆分.
   [map函数的使用方法](https://www.runoob.com/python/python-func-map.html)
   <strong>l = list(map(int, input().split()))</strong>
4. Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是**惰性**的，只有在需要返回下一个数据时它才会计算
事实上,for循环也是一种迭代过程,以下两种方法等价:

```
for x in [1, 2, 3, 4]:
    pass
```
```
it = iter([1, 2, 3, 4])
while True:
    try:
        x = next(it)
    except StopIteration:
        break
```
5. 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
```
def count1():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

def count2():
    fs = []
    def f(j):
        def g():
            return j * j
        return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs

```
6. 模块的作用域：外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public
7. Python内置的@property装饰器就是负责把一个方法变成属性调用的
8. [元类](https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072#0)暂时理解不了
9. 关于local 和 global变量：函数内部首先搜索local变量，若找不到则跳出函数搜索，如果已经声明该变量为global全局变量，则**可以在不声明的情况下对其赋值**