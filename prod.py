from functools import reduce
def funcProd(l):
    return reduce(lambda x, y: x * y, l)
l = list(map(int, input().split()))
print(l)
print(funcProd(l))