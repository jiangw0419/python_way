#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :t03.py
@时间    :2020/09/07 18:36:13
@作者    :江伟
@版本    :1.0
@说明    :
练习3：设计一个函数返回给定文件名的后缀名。
'''


def get_suffix(fileName, has_dot=False):
    pos = fileName.rfind('.')
    if 0 < pos < len(fileName)-1:
        index = pos if has_dot else pos+1
        return fileName[index:]
    return ''


print(get_suffix('gradle.properties'))
