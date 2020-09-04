#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p07.py
@时间    :2020/09/04 17:11:26
@作者    :江伟
@版本    :1.0
@说明    :
和字符串一样，列表也可以做切片操作，通过切片操作我们可以实现对列表的复制或者将列表中的一部分取出来创建出新的列表，
代码如下所示。

'''

fruits = ['grape','apple','strawberry','waxberry']
fruits += ['pitaya','pear','mango']

# 列表切片
fruits2 = fruits[1:4]
print(fruits2)#['apple', 'strawberry', 'waxberry']
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3)#['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
#
fruits4=fruits[-4:-1]
print(fruits4)#['waxberry', 'pitaya', 'pear']
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5)#['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']


"""下面的代码实现了对列表的排序操作。"""
list = ['orange','apple','zoo','internationalization','blueberry']
list2 = sorted(list)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
print(list2)#['apple', 'blueberry', 'internationalization', 'orange', 'zoo']

list3 = sorted(list,reverse=True)
print(list3)#['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list,key=len)
print(list4)#['zoo', 'apple', 'orange', 'blueberry', 'internationalization']

# 给列表对象发出排序消息直接在列表对象上进行排序
list.sort(reverse=True)
print(list)#['zoo', 'orange', 'internationalization', 'blueberry', 'apple']






