#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p04.py
@时间    :2020/09/04 16:23:12
@作者    :江伟
@版本    :1.0
@说明    :格式化输出字符串。
'''

a, b = 5, 10
# 方式
print('%d * %d =%d' % (a, b, a*b))
# 方式
print('{0} * {1} ={2}'.format(a, b, a*b))
# 方式
print(f'{a} * {b} = {a*b}')
