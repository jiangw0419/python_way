#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :d03.py
@时间    :2020/08/28 17:23:47
@作者    :江伟
@版本    :1.0
@说明    : python中函数（构建块）与其他语言的函数一个显著的区别：

对函数入参的处理：函数的参数可以有默认值，也支持使用可变参数，
所以Python并不需要像其他语言一样支持函数的重载，
因为我们在定义一个函数的时候可以让它有多种不同的使用方式

'''

from random import randint


def roll_dice(n=2):
    """摇色子，得到每次相加的总数"""
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total


def add(a=0, b=0, c=0):
    """三个数相加之和"""
    return a+b+c


# 如果没有指定参数那么使用默认值摇两颗色子
print("使用默认值摇两颗色子: ",roll_dice())
# 摇三颗骰子
print("摇三颗骰子: ",roll_dice(3))

print("默认三个数相加：",add())
print("指定a默认bc:",add(10))
print("指定ab默认c:",add(10,20))
print("指定abc:",add(10,20,30))
print("指定其中一个数b=12:",add(b=12))

