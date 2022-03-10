# 正则表达式 \d \w \s    * + ? {}
''' 匹配 re.match(r'xx', 'xxx')
>>> import re
>>> re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
<_sre.SRE_Match object; span=(0, 9), match='010-12345'>
>>> re.match(r'^\d{3}\-\d{3,8}$', '010 12345')

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
'''





''' 拆分str: re.split(r'xxx', 'xxx')
>>> s = 'a,  b,c, d,e  , f'
>>> re.split(r'[\s\,\;]+', s)
['a', 'b', 'c', 'd', 'e', 'f']
'''





''' 分组 m=re.match(r'(xx)-(xxx)', str);   m.group(0~1~2)
>>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
注意：此处只考虑到了前^后$的串
>>> m
<_sre.SRE_Match object; span=(0, 9), match='010-12345'>
>>> m.group(0)
'010-12345'
>>> m.group(1)
'010'
>>> m.group(2)
'12345'
'''



''' 例子-识别时间: re.match(r'()()()', str).groups()
>>> t = '19:05:30'
>>> m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
>>> m.groups()
('19', '05', '30')
'''




''' 加上?可以改为非贪婪匹配
>>> re.match(r'^(\d+?)(0*)$', '102300').groups()
('1023', '00')
'''



''' 预编译 re.compile()
>>> import re
# 编译:
>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
>>> re_telephone.match('010-12345').groups()
('010', '12345')
>>> re_telephone.match('010-8086').groups()
('010', '8086')
'''