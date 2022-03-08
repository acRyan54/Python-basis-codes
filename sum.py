from functools import reduce
def funcSum(l):
    return reduce(lambda x, y: x + y, l)
l = list(map(int, input().split()))
print(l)
print(funcSum(l))