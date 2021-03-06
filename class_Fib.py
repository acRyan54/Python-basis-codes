class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):#迭代器
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10 ** 7:
            raise StopIteration()
        return self.a
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):#切片参数
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):#方便
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
    