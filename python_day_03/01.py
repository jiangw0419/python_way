#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :01.py
@说明    : 分支结构
@时间    :2020/08/24 15:48:19
@作者    :江伟
@版本    :1.0
'''

# if语句的使用

username = input("请输入用户名：")
password = input("请输入密码")

if(username == 'admin' and password =='123456'):
    print("身份验证成功")
else:
    print("身份验证失败")



