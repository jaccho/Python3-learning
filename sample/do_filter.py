# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#1
print('#1')
#create a list from 3 to infinity
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#judge if n can be divide by x
#return as a function: lambda function
def _not_divisible(n):
    return lambda x : x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
        
# 打印1000以内的素数:
for n in primes():
    if n < 200:
        print(n)
    else:
        break
    
#2
print('#2')
def is_palindrome_1(n):#自己写的。。。累赘
    nStr = str(n)
    i = len(nStr)-1
    N = 0
    while i > -1:
        N = N * 10 + int(nStr[i])
        i = i - 1
    return n - N == 0

def is_palindrom(n): #最简单的实现了
    return str(n) == str(n)[::-1]
        
      
      
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 1000))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505, 515, 525, 535, 545, 555, 565, 575, 585, 595, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 707, 717, 727, 737, 747, 757, 767, 777, 787, 797, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 909, 919, 929, 939, 949, 959, 969, 979, 989, 999]:
    print('测试成功!')
else:
    print('测试失败!')








      