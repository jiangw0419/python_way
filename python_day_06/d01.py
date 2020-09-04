#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :d01.py
@时间    :2020/08/28 15:51:05
@作者    :江伟
@版本    :1.0
@说明    : 函数和模块的使用

在讲解本章节的内容之前，我们先来研究一道数学题，请说出下面的方程有多少组正整数解。
x1 + x2 + x3 + x4 = 8
事实上，上面的问题等同于将8个苹果分成四组每组至少一个苹果有多少种方案。想到这一点问题的答案就呼之欲出了。
'''

"""
python:
输入M和N计算C(M,N)
 n             m!
C     =  {------------
 m          n!(m!-n!)    
"""
m = int(input('M = '))
n = int(input('N = '))

fm = 1
fn = 1
fm_n = 1
for num in range(1, m+1):
    fm *= num
for num in range(1, n+1):
    fn *= num
for num in range(1, m - n + 1):
    fm_n *= num
print(fm // fn // fm_n)

"""思考：上面代码用了三次求阶乘，代码重复，考虑抽出公共部分封装成一个函数，在其他需要使用的地方调用此函数就可以了"""


"""定义函数：python用用def,参考d02.py"""

