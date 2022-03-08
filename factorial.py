#python编译器并不提供尾递归优化
import math
def fact(n):
    return factt(n, 1)

def factt(num, prod):
    if num == 1:
        return prod
    return factt(num-1, num*prod)

n = int(input())
print(fact(n))
print(math.factorial(n))