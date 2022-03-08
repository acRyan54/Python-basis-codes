class Student(object):
    def __init__(self, name = 'Michael'):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__
#可以用于打印实例
    def __getattr__(self, attr):#不存在的属性
        if attr == 'score':
            return 1234567890
        return AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
    def __call__(self):#把实例当作函数调用
        print('My name is %s' % self.name)                         