#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p07.py
@时间    :2020/08/27 17:55:59
@作者    :江伟
@版本    :1.0
@说明    :输出100以内所有的素数。
说明：素数指的是只能被1和自身整除的正整数（不包括1）。
'''
from math import sqrt


for x in range(2, 100):
    is_prime = True
    end = int(sqrt(x))+1
    for y in range(2, end):
        if(x % y == 0):
            is_prime = False
            break
    if(is_prime):
        print(x, end=' ')
