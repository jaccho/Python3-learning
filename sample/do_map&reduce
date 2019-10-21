# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from functools import reduce
from math import sqrt

#1
print('#1')
def normalize(name):
        Name = (name[0].upper())
        return Name + reduce(lambda x,y:x.lower()+y.lower(),name[1:])

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


#2
print('#2')
def prod(L):
    return reduce(lambda x,y:x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
    
#3
print('#3')
def str2float(s):
    def str2int(s):
        return reduce(lambda x,y:x*10+y,map(lambda x:int(x),s))
    i = s.find('.')
    if i == -1:
        return str2int(s)
    else:
        l = len(s)
        s = s[0:i]+s[i+1:]
        return str2int(s)/(10**(l-i-1))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))
"""
输出结果
str2float('123.456') = 123.456
测试成功!
0
123.456
123.456
0.1234
0.1234
120.0034
"""
