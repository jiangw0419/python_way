#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :d3.py
@时间    :2020/08/31 14:55:56
@作者    :江伟
@版本    :1.0
@说明    : 修改全局变量的值
'''

def foo():
    #1.我们可以使用global关键字来指示foo函数中的变量a来自于全局作用域，
    #2.如果全局作用域中没有a，那么下面一行的代码就会定义变量a并将其置于全局作用域。
    #同理，如果我们希望函数内部的函数能够修改嵌套作用域中的变量，可以使用nonlocal关键字来指示变量来自于嵌套作用域,--->d4
    global a
    a = 200
    print(a) #200

if __name__ == "__main__":
    a = 200
    foo()
    print(a) #200