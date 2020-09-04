#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p02.py
@说明    : 将一个正整数反转，12345-->54321
@时间    :2020/08/27 16:15:09
@作者    :江伟
@版本    :1.0
'''

num = int(input("num = "))
resevse_num = 0
while num > 0:
    resevse_num = resevse_num * 10 + num % 10
    num //= 10
print("翻转之后为：%d"%(resevse_num))    

