#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :d1.py
@时间    :2020/08/31 14:49:02
@作者    :江伟
@版本    :1.0
@说明    : 变量的作用域
'''
def foo():
    b = 'hello' #局部变量（local variable），属于局部作用域

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()

if __name__ == "__main__":
    a = 100 #全局变量（global variable）属于全局作用域
    # print(b)  NameError: name 'b' is not defined
    foo()    