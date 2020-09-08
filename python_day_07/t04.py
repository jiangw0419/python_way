#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :t04.py
@时间    :2020/09/07 18:44:08
@作者    :江伟
@版本    :1.0
@说明    :
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
'''

def max2(x):
    m1,m2 = (x[0],x[1]) if x[0] > x[1] else (x[1],x[0])
    for index in range(2,len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index]>m2:
            m2 = x[index]
    return m1,m2   

print(max2((1,2,3123,2,3,4,5,6,9,7,6)))         