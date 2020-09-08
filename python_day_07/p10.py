#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p10.py
@时间    :2020/09/04 17:55:29
@作者    :江伟
@版本    :1.0
@说明    :元组:元组元素不能修改

Python中的元组与列表类似也是一种容器数据类型，可以用一个变量（对象）来存储多个数据，
不同之处在于元组的元素不能修改，在前面的代码中我们已经不止一次使用过元组了。
顾名思义，我们把多个元素组合到一起就形成了一个元组，所以它和列表一样可以保存多条数据。
下面的代码演示了如何定义和使用元组。
'''
#定义元组
t = ('江伟',18,True,'安徽池州')

print(t)
# 获取元组中的元素
print(len(t))#4
print(t[0])#江伟
print(t[-1])#安徽池州
print(t[len(t)-1])#安徽池州

#遍历打印 t中元素
for num in t:
    print(num)


# 变量t重新引用了新的元组原来的元组将被垃圾回收
# t[0] = 19
# print(t[0])#TypeError: 'tuple' object does not support item assignment
t = ('王大锤',19,False,'陕西西安')
print(t)#('王大锤', 19, False, '陕西西安')
# 将元组转换成列表
person = list(t)
print(person)#['王大锤', 19, False, '陕西西安']
#列表是可以修改它的元素的
person[0]=20
print(person[0])
# 将列表转换成元组
tt = tuple(person)
print(tt)#(20, 19, False, '陕西西安')


