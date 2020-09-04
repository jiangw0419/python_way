#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p01.py
@时间    :2020/08/31 09:36:13
@作者    :江伟
@版本    :1.0
@说明    :练习1：实现计算求最大公约数和最小公倍数的函数。
'''


def func(a, b):
    if(a > b):
        (a, b) = (b, a)
    for n in range(a, 1, -1):
        if(a % n == 0 and b % n == 0):
            return n
    return 1        


def func2(a, b):
    return a * b // func(a, b)


print(func(12, 8))
print(func2(13, 8))
