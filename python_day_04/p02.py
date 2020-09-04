#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p02.py
@说明    :输入两个正整数，计算它们的最大公约数和最小公倍数。
提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。
@时间    :2020/08/26 18:06:20
@作者    :江伟
@版本    :1.0
'''
from math import sqrt

num1 = int(input("请输入数字1："))
num2 = int(input("请输入数字2："))

if (num1 > num2):
    num1,num2 = num2,num1 #num1>num3就交换位置
for x in range(num1,0,-1):
    if( num1 % x  == 0 and num2 % x == 0):
        print("%d和%d的最小公倍数为：%d"%(num1,num2,(num2*num2 // x)))
        print("%d和%d的最大公约数为:%d"%(num1,num2,x))            
        break





