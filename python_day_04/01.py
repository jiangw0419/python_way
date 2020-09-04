#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :01.py
@说明    : 循环结构-for in 和 while
@时间    :2020/08/26 16:50:34
@作者    :江伟
@版本    :1.0
'''

'''计算1..100求和的结果'''

sum = 0

# 0-100
# for x in range(101):#0-100范围的整数取不到101
# for x in range(1,101):#前闭后开 [1,101)
# for x in range(1,101,2): # 前闭后开步长为2  1,3,5...奇数之和
# for x in range(100,0,-2):#前闭后开步长为-2  100，98...0偶数之和
for x in range(0,101,2):#偶数之和
    sum +=x

print("for x in range(101) = %d"%(sum))   




