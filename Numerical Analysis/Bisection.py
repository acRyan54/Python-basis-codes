#Bisection
from sympy import *
x = symbols('x')

def func(f, var):
    return f.evalf(subs = {x: var})

def cal(f, a, b, tol):
    fa = func(f, a)
    fb = func(f, b)
    while (b - a) / 2 > tol:
        c = (b + a) / 2
        fc = func(f, c)
        if fc == 0:
            return c
        if fa * fc < 0:
            b = c
        else:
            a = c
    return (b + a) / 2
        
        

if __name__ == '__main__':
    f = sympify(input())
    a = eval(input())
    b = eval(input())
    tol = eval(input())
    print(cal(f, a, b, tol))