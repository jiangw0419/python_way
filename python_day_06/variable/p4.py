#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p4.py
@时间    :2020/08/31 15:02:08
@作者    :江伟
@版本    :1.0
@说明    :验证：
如果我们希望函数内部的函数能够修改嵌套作用域中的变量，可以使用nonlocal关键字来指示变量来自于嵌套作用域
'''
def foo():
    b = 200
    print(b)

    def bar():
        nonlocal b
        b = 300
        print(b)
    bar()
    print(b)

if __name__ == "__main__":
    foo()

# 200
# 300
# 300