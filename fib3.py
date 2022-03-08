#yield定义一个生成器函数
def fib(n):
    i, a, b = 0, 0, 1
    while i < n:
        yield b
        a, b = b, a+b
        i += 1
    return 'done'

n = int(input())
for i in fib(n):
    print(i)
        