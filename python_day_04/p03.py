#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p03.py
@说明    :打印如下所示的三角形图案。

*
**
***
****
*****

@时间    :2020/08/26 18:23:38
@作者    :江伟
@版本    :1.0
'''

lines = int(input("请输入行数："))
for x in range(lines):
    for y in range(x+1):
        print("*",end="")
    print()