#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p01.py
@说明    :练习1：英制单位英寸与公制单位厘米互换。 1英寸=2.54厘米
@时间    :2020/08/24 17:03:58
@作者    :江伟
@版本    :1.0
'''

d = float(input("请输入长度:"))
unit = input("请输入单位：")

if (unit == 'in' or unit == '英寸'):
    print('%.1f 英寸= %.2f厘米' %(d,(d * 2.54)))   
elif (unit == 'cm' or unit == '厘米'):
    print('%.1f厘米 = %.2f英寸' %(d,(d / 2.54)))
else:
    print("输入有误！")


