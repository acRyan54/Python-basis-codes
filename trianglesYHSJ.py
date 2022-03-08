def tri():
    l = [1]
    while True:
        yield l
        x = [0] + l
        y = l + [0]
        l = [x[i]+y[i] for i in range(len(x))]

if __name__ == '__main__':
    n = int(input())
    g = tri()
    for i in range(n):
        print(next(g))