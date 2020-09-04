#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p04.py
@时间    :2020/08/31 14:07:38
@作者    :江伟
@版本    :1.0
@说明    :练习4：写一个程序判断输入的正整数是不是回文素数。
'''


def func(n):
    is_hw = True
    is_prime = True
    temp = n
    total = 0
    while temp > 0:
        a = temp % 10
        temp //= 10
        total = total * 10 + a
    if(total == n):
        is_hw = True
    else:
        is_hw = False

    for x in range(2, int(n ** 0.5) + 1):
        if(n % x == 0):
            is_prime = False
        break

    if(is_hw and is_prime):
        print("%d是回文素数" % n)
    elif(is_hw):
        print("%d是回文数，但不是素数" % n)
    elif(is_prime):
        print("%d是素数，但不是回文数" % n)
    else:
        print("%d既不是回文数，也不是素数" % n)


x = int(input('x = '))
func(x)
