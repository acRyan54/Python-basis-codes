#函数、类可以调用，实例不可调用# callable(xxx)

class Chain(object):
    def __init__(self, path = ''):
        self._path = path
    def __str__(self):
        return self._path
    __repr__ =  __str__
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    #print 这个地方用return， 因为有__repr__可以直接调用path
    def __call__(self, name):#调用+属性
        return Chain('%s/%s' % (self._path, name))

#Chain().users('Michael').repos 输出 /users/Michael/repos
###################分解动作
# Chain()
# Chain().users
# Chain().users('Michael')
# Chain().users('Michael').repos
