#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p08.py
@时间    :2020/09/04 17:29:17
@作者    :江伟
@版本    :1.0
@说明    :生成式和生成器
我们还可以使用列表的生成式语法来创建列表，代码如下所示。
'''
f = [x for x in range(1,10)]
print(f)#[1, 2, 3, 4, 5, 6, 7, 8, 9]

f1 = [x + y for x in 'ABCD' for y in '1234567']
print(f1)#['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7']
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间

f2 = [x ** 2 for x in range(1,1000)]
# print(f2)
# 查看对象占用内存的字节数
import sys
print(sys.getsizeof(f2))#9024
# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f3 = (x ** 2 for x in range(1,1000))
print(sys.getsizeof(f3))#120
for var in f3:
    print(var)

