import math
def quadratic(a : int, b : int, c : int):
    delta = b * b - 4 * a * c
    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2
    else:
        return -1

a, b, c = int(input()), int(input()), int(input())
print(quadratic(a, b, c))