#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :02.py
@说明    :
@时间    :2020/08/24 14:16:01
@作者    :江伟
@版本    :1.0
'''

a = 100
b = 12.345
c = 1 + 5j
d = 'hello world'
e = False


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
# console:
# <class 'int'>
# <class 'float'>
# <class 'complex'>
# <class 'str'>
# <class 'bool'>

# ===========================================================
# int()：将一个数值或字符串转换成整数，可以指定进制。

print(int(a)) #100
print(int(b)) #12
# print(int(c)) #TypeError: :can't convert complex to int
# print(int(d)) #ValueError: invalid literal for int() with base 10: 'hello world'
print(int(e)) #0

# float()：将一个字符串转换成浮点数。

print(float(a)) #100.0
print(float(b)) #12.345
# print(float(c)) #TypeError: can't convert complex to float
# print(float(d)) #ValueError: could not convert string to float: 'hello world'
print(float(e)) #0.0

# str()：将指定的对象转换成字符串形式，可以指定编码。

print(str(a)) #100
print(str(b)) #12.345
print(str(c)) #(1+5j)
print(str(d)) #hello world
print(str(e)) #False

# chr()：将整数转换成该编码对应的字符串（一个字符）。

print(chr(a)) #d
# print(chr(b)) #TypeError: integer argument expected, got float
# print(chr(c))#TypeError: can't convert complex to int
# print(chr(d)) #TypeError: an integer is required (got type str)
# print(chr(e)) # 

# ord()：将字符串（一个字符）转换成对应的编码（整数）。

# print(ord(a)) #TypeError: ord() expected string of length 1, but int found
# print(ord(b)) #TypeError: ord() expected string of length 1, but float found
# print(ord(c)) #TypeError: ord() expected string of length 1, but complex found
# print(ord(d)) #TypeError: ord() expected a character, but string of length 11 found
# print(ord(e)) #TypeError: ord() expected string of length 1, but bool found
print(ord('d')) #100
# =================================================================

