#Lagrange
import numpy as np
import sympy as sp
import re

x = sp.symbols('x')


def cal(n, X, Y):
    P = 0
    for i in range(n):
        Li = 1
        for j in range(n):
            if j == i:
                continue
            Li = Li * (x - X[j]) / (X[i] - X[j])
        P = P + Li * Y[i]
    return P
            
    
    
    
if __name__ == '__main__':
    num = int(eval(input()))
    X, Y = [], []
    for i in range(num):
        recv = re.split(r'[\s,]+', input())
        X.append(eval(recv[0]))
        Y.append(eval(recv[1]))
    ans = cal(num, X, Y)
    print(ans)
    print(sp.expand(sp.simplify(ans)))

