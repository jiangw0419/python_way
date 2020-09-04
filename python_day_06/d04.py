#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :d04.py
@时间    :2020/08/28 17:43:00
@作者    :江伟
@版本    :1.0
@说明    : 函数可变入参：java中有func(String ...str){},
python：*params
'''


def funAdd(*args):
    total = 0
    for n in args:
        total += n
    return total


print("函数可变入参求和：1+2=", funAdd(1, 2))
print("函数可变入参求和：1+2+3=", funAdd(1, 2, 3))
print("函数可变入参求和：1+2+3+4=", funAdd(1, 2, 3, 4))
