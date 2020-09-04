#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p04.py
@说明    :CRAPS赌博游戏。
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。
@时间    :2020/08/27 16:42:02
@作者    :江伟
@版本    :1.0
'''
from random import randint
counter = 0
while True:
    counter +=1
    num = randint(1,12)
    if(counter == 1):
        if(num == 7 or num == 11):
            print("第%d次摇出骰子点数为：%d玩家赢！"%(counter,num))
            break
        elif(num == 2 or num == 3 or num == 12):
            print("第%d次摇出骰子点数为：%d庄家赢！"%(counter,num))
            break
        else:
            firstNum = num
            print("第%d次摇出骰子点数为：%d继续游戏！"%(counter,num))
    else:
        if(num == 7):
            print("第%d次摇出骰子点数为：%d庄家赢！"%(counter,num))
            break
        elif(num == firstNum):
            print("第%d次摇出骰子点数为：%d玩家赢！"%(counter,num))
            break
        else:
            print("第%d次摇出骰子点数为：%d继续游戏！"%(counter,num))
            
    