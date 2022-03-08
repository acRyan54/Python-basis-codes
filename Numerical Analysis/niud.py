from sympy import *
x = symbols('x')

def cal(f, x0, step):
    g = x - f/diff(f,x)
    return __cal(g, x0, step)

def __cal(g, x0, step):
    ans = [x0]
    for i in range(step):
        ans.append(g.subs(x, ans[i]))
    return ans

if __name__ == '__main__':
    f = sympify(input())
    x0 = float(input())
    step = int(input())
    ans = cal(f, x0, step)
    print(ans)