# SymPy

1. solve(expr, var) 能求解析解, 而nsolve(expr, var)能求精确数值解

## 教程须知

[官方教程](https://docs.sympy.org/latest/tutorial/calculus.html)
[基本教程](https://www.cnblogs.com/zyg123/p/10539650.html)
自主获取帮助：
```
>>>print([w for w in dir(p) if 'coeff' in w])
>>>help(p.all_coeffs)
```

## 基本操作

```[python]
from sympy import *
init_printing(use_latex='mathjax')
x, y = symbols('x y')
x = symbols('x', positive = True, rational = True)
sympify(str)
expand(expr); factor(expr); simplify(expr); apart(expr); together(expr); expand_trig(expr_trig)
latex(expr)
s.eval()
expr.evalf(subs = {var1:value1, var2:value2})
expr.evalf(100)
expr.subs([(var1, value1), (var2, value2)])
数值计算N(expr.subs(xxxxxx))
func = lambdify(x, expr, "numpy") 可以对于'numpy'里的数组进行操作
diff(expr, var1, n1, var2, n2)
integrate(expr, (var1, -oo, oo), (var2, -oo, oo))
limit(expr, x, x_n); limit(expr, x, x_n, '+')
_; N(_); N(expr)
E; I; pi
binomial(n, m)
factorial(n)
expr.series(x, x_0, n).removeO()
solve([f1, f2, f3], [x, y, z])
Eq(Left, Right) <==> Left - Right = 0
linsolve()
nonlinsolve()
f = symbols('f', cls = Function)
dsolve(equation, f(x)); Eq(f(x).diff(x, n), Right)
Matrix([[a11, a12], [a21, a22]])
eye(); ones(); zeros(); diag(a11, a22, a33)
m.shape 属性; m.row(n); m.col(n); m.row_del(n); m.col_del(n); m.row_insert(pos, M); m.col_insert(pos, M);
m.T; m**(-1); m.det(); m.rref()
m.eigenvals(); m.charpoly()  #注:.eigenvals()返回dict{lambda_i: times_i}对应特征值和次数
p.all_coeffs()
P, D = M.diagonalize()
Expr = Sum(expr, (var, n_0, n_t));  Expr = Product(expr, (var, n_0, n_t)); 
Expr = Integral(expr, (var, x_0, x_t))
Expr.doit()


```

### 示例


```
# 打印所有特征值
>>> eig = M.eigenvals()
>>> for eigenval in eig:
...     for i in range(eig[eigenval]):
...             print(eigenval)
# 打印特征多项式
lamda = symbols('lamda')
p = M.charpoly(lamda)
print(p)
print(p.all_coeffs())
factor(p)
```