#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p05.py
@说明    :打印三角形图案
    *
   ***
  *****
 *******
*********
@时间    :2020/08/26 18:35:10
@作者    :江伟
@版本    :1.0
'''
lines = int(input("请输入要打印的行数："))

"""教案答案"""
# for i in range(lines):
#     for _ in range(lines - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()        