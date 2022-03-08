#Const
from enum import Enum, unique
class Gender(Enum):#常量
    Male = 0
    Female = 1
# Gender.Male 是 Gender.Male, 对应Key
# Gedner.Male.value 是0,对应value
# Gedner.Male.name 是Male,对应name
#<name, value>
class Student(object):
    def __init__(self, name, i):
        self.name = name
        self.gender = Gender(i)
# ::以下4个都相等
# a = Gender.Male
# Gender(a)
# Gender(0)
# Gender['Male']

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')