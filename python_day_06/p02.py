#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p02.py
@时间    :2020/08/31 10:00:41
@作者    :江伟
@版本    :1.0
@说明    : 练习2：实现判断一个数是不是回文数的函数

回文数：设n是一任意自然数。若将n的各位数字反向排列所得自然数n1与n相等，则称n为一回文数。
例如，若n=1234321，则称n为一回文数；但若n=1234567，则n不是回文数。
'''


def func(n):
    temp = n
    sum = 0
    while n > 0:
        b = n % 10
        n //= 10
        sum = sum * 10 + b
    if(sum == temp):
        print("%d是回文数！" % temp)
    else:
        print("%d不是回文数！" % temp)


func(1234321)
