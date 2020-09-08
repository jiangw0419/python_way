#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :t05.py
@时间    :2020/09/08 14:08:51
@作者    :江伟
@版本    :1.0
@说明    :
练习5：计算指定的年月日是这一年的第几天。
'''


def is_leap_year(year):
    """是否是闰年"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def whitch_day(year,month,day):
    day_of_month_isleap = [31,29,31,30,31,30,31,31,30,31,30,31]
    day_of_month_notleap= [31,28,31,30,31,30,31,31,30,31,30,31]
    total = 0
    if is_leap_year(year):
        day_of_month = day_of_month_isleap
    else:
        day_of_month = day_of_month_notleap
    for m in range(month - 1):
          total +=day_of_month[m]  
    return total +day    

def main():
    print(whitch_day(1990,8,28))
    print(whitch_day(2020,9,8))
    print(whitch_day(1991,4,19))

if __name__ == "__main__":
    main()

