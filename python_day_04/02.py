#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :02.py
@说明    :循环结构-while
如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环。
while循环通过一个能够产生或转换出bool值的表达式来控制循环，
表达式的值为True则继续循环；表达式的值为False则结束循环。
@时间    :2020/08/26 17:27:06
@作者    :江伟
@版本    :1.0
'''
"""
猜数字游戏的规则是：计算机出一个1到100之间的随机数，
玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），
如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
"""
import random

answer = random.randint(1,100)
couter = 0

while True:
    couter +=1
    number = int(input("请输入："))
    if(number < answer):
        print("大一点")
    elif(number > answer):
        print("小一点")
    else:
        print("猜中了，共猜了：%d 次"%(couter))
        break        
    print("您共猜了：%d 次"%(couter))
    if(couter > 10):
        print("您的智商余额不足..")




