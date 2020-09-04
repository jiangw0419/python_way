#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p3.py
@说明    :百钱百鸡问题。
说明：百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：
公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
@时间    :2020/08/27 16:20:02
@作者    :江伟
@版本    :1.0
'''

# 穷举法
# 公鸡x x的范围[0,20] 母鸡y y的范围[0,33] ,小鸡z = 100-x-y
for x in range(20):
    for y in range(33):
        z = 100-x-y
        if(5*x + 3*y + z/3 == 100):
            print("百钱白鸡：公鸡:%d,母鸡:%d,小鸡:%d"%(x,y,z))