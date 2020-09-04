#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p03.py
@说明    : 练习3：输入年份判断是不是闰年。
@时间    :2020/08/24 15:39:54
@作者    :江伟
@版本    :1.0
'''
year = int(input("请输入年份:"))
b = (year % 4 ==0 and year % 100 !=0) or year % 400 == 0
print("%d年闰年:%s"%(year,b))



