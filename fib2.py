#循环计算
def fib(n):
    l = [0, 1]
    for i in range(2, n+1):
        l.append(l[i-1] + l[i-2])
    return l

n = int(input())
print(fib(n))