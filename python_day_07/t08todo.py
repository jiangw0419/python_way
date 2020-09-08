#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :t08.py
@时间    :2020/09/08 15:00:05
@作者    :江伟
@版本    :1.0
@说明    :
综合案例：
案例1：双色球选号。
'''
from random import sample,randint,randrange


def random_select():
    """
    随机选取一组号码
    """
    red_balls = [x for x in range(1,34)]
    selected_balls = []
    selected_balls = sample(red_balls,6)
    selected_balls.sort()
    selected_balls.append(randint(1,16))
    return selected_balls

def display(balls):
    """
    输出双色球号码
    """
    for index,ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|' ,end=' ')
        print('%02d' %ball,end=' ')    
    print()

def main():
    n = int(input('机选几组: '))
    # print(random_select())  
    for _ in range(n):
         display(random_select())

if __name__ == "__main__":
    main()

# 机选几组: 10
# 03 05 07 16 25 28 | 07
# 05 06 12 14 15 22 | 16
# 03 06 09 15 17 22 | 04
# 09 12 19 22 26 31 | 11
# 04 06 17 21 27 33 | 10
# 01 09 10 13 16 19 | 08
# 01 13 16 19 23 26 | 06
# 10 17 21 25 28 30 | 07
# 06 14 19 21 25 28 | 01
# 02 07 09 10 25 30 | 11




