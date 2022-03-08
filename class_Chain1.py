#简单的链式调用操作
class Chain(object):
    def __init__(self, path = ''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    #实现链式调用
    def __str__(self):
        return self._path
    __repr__ = __str__