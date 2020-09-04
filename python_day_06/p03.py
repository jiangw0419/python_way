#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p03.py
@时间    :2020/08/31 14:02:34
@作者    :江伟
@版本    :1.0
@说明    :练习3：实现判断一个数是不是素数的函数。
质/素数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。
'''
from math import sqrt


def is_palindrome(n):
    end = int(sqrt(n))+1
    for x in range(2, end):
        if(n % x == 0):
            print("%d 不是素数" % n)
            return
    print("%d 是素数" % n)


is_palindrome(8)