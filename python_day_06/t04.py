#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :t04.py
@时间    :2020/08/31 14:41:17
@作者    :江伟
@版本    :1.0
@说明    :练习4：写一个程序判断输入的正整数是不是回文素数。
教案答案：
'''
import p02 as p2
import p03 as p3

if __name__ == "__main__":
    num = int(input("x = "))
    if p2.func(num) and p3.is_palindrome(num):
        print("%d 是回文素数"%num) 

