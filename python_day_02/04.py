#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :04.py
@说明    : 赋值运算符
@时间    :2020/08/24 14:47:47
@作者    :江伟
@版本    :1.0
'''

a = 10
b = 3
a +=b       # 相当于：a = a + b    #a=13 b=3  
a *= a+2    # 相当于：a = a * (a + 2)   #a=13*15=195
print(a)    #195
