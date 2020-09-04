#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :02.py
@说明    :分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

@时间    :2020/08/24 15:55:01
@作者    :江伟
@版本    :1.0
'''

x = float(input("请输入x的值："))

if(x > 1):
    f = 3 * x - 5
elif (x < -1):
    f = 5 * x +3
else:
    f = x +2

print("f(%.1f) = %.2f"%(x,f))


#嵌套
if(x > 1):
    f = 3 * x - 5
else:
    if(x < -1):
        f = 5 * x + 3
    else:
        f = x + 2    

print("嵌套方式：f(%.1f) = %.2f"%(x,f))

#哪种方式更好？
#Flat is better than nested.
#python之禅:扁平比嵌套好