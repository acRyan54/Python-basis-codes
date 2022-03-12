#ModifiedNewton
from sympy import *
x = symbols('x')

def cal(f, x0, step):
    def _cal(g, x0, step):
        ans = [x0]
        for i in range(step):
            ans.append(g.subs(x, ans[i]))
        return ans
    
    g = x - (f * diff(f, x)) / (diff(f, x) ** 2 - f * diff(f, x, 2))
    return _cal(g, x0, step)


if __name__ == '__main__':
    f = sympify(input())
    x0 = eval(input())
    step = int(eval(input()))
    ans = cal(f, x0, step)
    print(ans[-1])