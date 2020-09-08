#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :t02.py
@时间    :2020/09/07 18:21:29
@作者    :江伟
@版本    :1.0
@说明    :
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
'''
import random

def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    tempLen = code_len
    while tempLen>0:
        code += all_chars[random.randint(0,len(all_chars)-1)] 
        tempLen -=1
    return code
print(generate_code())
print(generate_code(6))

if __name__ == "__main__":
    generate_code()       

