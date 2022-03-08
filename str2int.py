#用于代替int()函数
from functools import reduce
digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
def char2num(s):
    return digits[s]
def str2int(s):
    return reduce(lambda x, y: 10 * x + y, map(char2num, s))
s = input()
print(str2int(s))