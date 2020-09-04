#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p04.py
@说明    :输入三条边长，如果能构成三角形就计算周长和面积。海伦公式：S= Math.sqrt(s*(s-a)(s-b)(s-c)) ;    s = (a+b+c)/2
@时间    :2020/08/24 17:55:11
@作者    :江伟
@版本    :1.0
'''
a = float(input("请输入边长a:"))
b = float(input("请输入边长b:"))
c = float(input("请输入边长c:"))

t = (a + b ) > c and (a + c ) > b and (b + c) > a
print("边长分别为%1d ,%2d ,%2d是否能构成三角形？%s"%(a,b,c,t))

if(t):
    l = a + b +c
    p = l / 2
    s = (p * (p-a) * (p-b) * (p-c)) ** 1/2 
    print("三角形的周长:%.1f，面积为:%.2f"%(l,s))

