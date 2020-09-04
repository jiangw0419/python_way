#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p05.py
@时间    :2020/09/04 16:30:24
@作者    :江伟
@版本    :1.0
@说明    :使用列表

字符串类型（str）和之前我们讲到的数值类型（int和float）有一些区别
数值类型是标量类型，也就是说这种类型的对象没有可以访问的内部结构；
而字符串类型是一种结构化的、非标量类型，所以才会有一系列的属性和方法。

接下来我们要介绍的列表（list），也是一种结构化的、非标量类型，
它是值的有序序列，每个值都可以通过索引进行标识，定义列表可以将列表的元素放在[]中，
多个元素用,进行分隔，可以使用for循环对列表元素进行遍历，也可以使用[]或[:]运算符取出列表中的一个或多个元素。
'''

"""下面的代码演示了如何定义列表、如何遍历列表以及列表的下标运算。"""

list1 = [1,3,5,7,100]
print(list1)#[1, 3, 5, 7, 100]
# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2)#['hello', 'hello', 'hello']
# 计算列表长度(元素个数)
print(len(list1))#5
# 下标(索引)运算
print(list1[3])#7
print(list1[-1])#100,倒数第一位
# print(list1[100])#IndexError: list index out of range
print(list1[-2])#7倒数第二位

list1[2] = 100#赋值
print(list1)#[1, 3, 100, 7, 100]

# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 1
# 3
# 100
# 7
# 100  

# 通过for循环遍历列表元素
for num in list1:
    print(num)
# 1
# 3
# 100
# 7
# 100    
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index,num in enumerate(list1):
    print(index,num)
# 0 1
# 1 3
# 2 100
# 3 7
# 4 100



