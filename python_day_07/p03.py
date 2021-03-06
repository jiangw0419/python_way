#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p03.py
@时间    :2020/08/31 18:25:33
@作者    :江伟
@版本    :1.0
@说明    :
我们还可以通过一系列的方法来完成对字符串的处理，代码如下所示。
'''

str1 = "hello , world!"
# 通过内置函数len计算字符串的长度
print(len(str1))#14
# 获得字符串首字母大写的拷贝
print(str1.capitalize())#Hello , world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title())#Hello , World!
# 获得字符串变大写后的拷贝
print(str1.upper())#HELLO , WORLD!
# 从字符串中查找子串所在位置
print(str1.find('w'))#8
print(str1.find("o"))#4第一个位置
print(str1.find("str"))#-1表示没有找到
# 与find类似但找不到子串时会引发异常
print(str1.index("o"))#4
# print(str1.index("str"))#ValueError: substring not found
# 检查字符串是否以指定的字符串开头
print(str1.startswith("w"))#False
print(str1.startswith("h"))#True
print(str1.startswith("H"))#False
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!'))#true
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50,'*'))#******************hello , world!******************
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50,'*'))#************************************hello , world!
# 将字符串以指定的宽度靠左放置右侧填充指定的字符
print(str1.ljust(50,'*'))#hello , world!************************************

strNum = 'abc123456'
# 检查字符串是否由数字构成
print(strNum.isdigit())#False
# 检查字符串是否以字母构成
print(strNum.isalpha())#False
# 检查字符串是否以数字和字母构成
print(strNum.isalnum())#True

str3 = '    jiangwei@keepcode.cn '
print(str3)#    jiangwei@keepcode.cn
# 获得字符串修剪左右两侧空格之后的拷贝,java中的str.trim()方法
print(str3.strip())#jiangwei@keepcode.cn



