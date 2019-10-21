# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def createCounter_b():
    i = 0
    def counter():
        nonlocal i
        i += 1
        return i
    return counter


def createCounter():#个人感觉这个方案在代码上看起来少了一行代码，但是可读性下降了
    i = [0]
    def counter():
        i[0] += 1
        return i[0]
    return counter

'''
网上对int和list是否需要声明全局变量的一个解释：
因为int类型str类型之类的，只有一种修改方法，即x = y， 恰好这种修改方法同时也是创建变量的方法，所以产生了歧义，不知道是要修改还是创建。而dict/list/对象等，可以通过dict['x']=y或list.append()之类的来修改，跟创建变量不冲突，不产生歧义，所以都不用显式global。

原文链接：https://blog.csdn.net/handsomekang/article/details/41392417
'''
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')