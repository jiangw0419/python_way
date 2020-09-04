#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p01.py
@说明    :输入一个正整数判断是不是素数。
提示：素数指的是只能被1和自身整除的大于1的整数。
@时间    :2020/08/26 17:46:30
@作者    :江伟
@版本    :1.0
'''

number = int(input("请输入一个正整数："))
if(number <= 0):
    print("请输入一个正整数！")
elif (number ==1):
    print("%d不是素数"%number)
temp = number

while True:
    temp +=-1
    print("temp = %d"%temp)
    if( number % temp == 0 and temp >= 0):
        print("%d 可以被 %d整除，所以不是素数"%(number,temp))
        break




