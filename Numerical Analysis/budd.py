from sympy import *
x = symbols('x')

def cal(g, x0, step):
    ans = [x0]
    for i in range(step):
        ans.append(g.subs(x, ans[i]))
    return ans

if __name__ == '__main__':
    g = sympify(input())
    x0 = float(input())
    step = int(input())
    ans = cal(g, x0, step)
    print(ans)