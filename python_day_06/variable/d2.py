#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :d2.py
@时间    :2020/08/31 14:54:27
@作者    :江伟
@版本    :1.0
@说明    :
再看看下面这段代码，我们希望通过函数调用修改全局变量a的值，但实际上下面的代码是做不到的。

'''

def foo():
    a = 200
    print(a) #200

if __name__ == "__main__":
    a = 100
    foo()
    print(a)    #100 
