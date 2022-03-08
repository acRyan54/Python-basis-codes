from tkinter import N


def notDivisible(n):
    return lambda x: x % n != 0
def primes():
    yield 2
    it = iter(range(3, 10**10000, 2))
    while True:
        n = next(it)
        yield n 
        it = filter(notDivisible(n), it)

n = int(input())
g = primes()
for i in range(n):
    print(next(g))
