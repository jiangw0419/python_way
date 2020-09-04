#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p04.py
@说明    :打印如下所示的三角形图案。
    *
   **
  ***
 ****
*****

@时间    :2020/08/26 18:30:11
@作者    :江伟
@版本    :1.0
'''

lines = int(input("请输入打印行数："))

for x in range(lines):
    for y in range(lines):
        if( y< lines -x-1):
            print(' ',end="")
        else:    
            print("*",end='')
    print()    

