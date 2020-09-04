#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p02.py
@时间    :2020/08/31 15:19:43
@作者    :江伟
@版本    :1.0
@说明    :Python为字符串类型提供了非常丰富的运算符，我们可以使用+运算符来实现字符串的拼接，
可以使用*运算符来重复一个字符串的内容，可以使用in和not in来判断一个字符串是否包含另外一个字符串（成员运算），
我们也可以用[]和[:]运算符从字符串取出某个字符或某些字符（切片运算），代码如下所示。
'''
s1 = 'hello' + ' ' + 'world'
s2 = 'hello' * 3 

print(s1) # hello world
print(s2) # hellohellohello

print('ll' in s1) #True
print ('ol' not in s1)#True

s3 = "abc123456"
# 从字符串中取出指定位置的字符(下标运算)
print(s3[3])#1
# print(s3[11])#  IndexError: string index out of range
# 字符串切片(从指定的开始索引到指定的结束索引)
print(s3[2:5])#c12
print(s3[:5])#abc12
print(s3[5:])#3456
print(s3[2::2])#c246 从下标为2开始步长为2循环取字符串
print(s3[::-1])#654321cba 从最后一个开始取
print(s3[-3:-1])#45 取倒数
