# Newton
from sympy import *
x = symbols('x')

def cal(f, x0, step, m = 1):
    def _cal(g, x0, step):
        ans = [x0]
        for i in range(step):
            ans.append(g.subs(x, ans[i]))
        return ans
    g = x - (m * f) / diff(f,x)
    return _cal(g, x0, step)


if __name__ == '__main__':
    f = sympify(input())
    x0 = eval(input())
    step = int(eval(input()))
    # m = int(eval(input()))
    ans = cal(f, x0, step, 1)
    print(ans[-1])