from functools import reduce
digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
def char2num(s):
    return digits[s]
def str2float(s):
    ss = s.split('.')
    return reduce(lambda x, y: 10 * x + y, map(char2num, ss[0])) + reduce(lambda x, y: 10 * x + y, map(char2num, ss[1])) * 0.1 ** len(ss[1])

s = input()
print(str2float(s))