from sympy import *
x = symbols('x')

def cal(f, a, b, tol):
    x = symbols('x')
    fa = f.subs(x, a)
    fb = f.subs(x, b)
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        fc = f.subs(x, c)
        if fc == 0:
            break
        if fa * fc <= 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a + b) / 2

if __name__ == '__main__':
    f = sympify(input())
    a = float(input())
    b = float(input())
    tol = eval(input())
    print(cal(f, a, b, tol))