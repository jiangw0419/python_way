#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :d02.py
@时间    :2020/08/28 16:52:56
@作者    :江伟
@版本    :1.0
@说明    :定义函数def，实现d01.py中阶乘功能
'''

def fac(num):
    """求阶乘"""
    result = 1
    for n in range(1,num +1):
        result  *= n
    return result 

m = int(input(" m = "))
n = int(input(" n = "))

print(fac(m) // fac(n) // fac(m-n))