#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :t01.py
@说明    :tearch教案:输入一个正整数判断它是不是素数
@时间    :2020/08/26 18:01:16
@作者    :江伟
@版本    :1.0
'''

from math import sqrt

num = int(input("请输入一个正整数："))
end = int (sqrt(num))

for x in (1,end+2):
    if(num % x == 0):
        isPrim = True
        break
if( isPrim and num!=1):
    print("%d是素数"%num)
else :
    print("%d不是素数"%num)            
