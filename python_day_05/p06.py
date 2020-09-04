#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p06.py
@时间    :2020/08/27 17:32:23
@作者    :江伟
@版本    :1.0
@说明    :找出10000以内的完美数。

说明：完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。

'''

num = int(input('num = '))

sum = 0
str = ''
for n in range(1,num):
    if(num % n == 0):
        if(n == 1):
            str = n
        else:
            str = '%s+%d'%(str,n)
        sum += n

if(sum == num):
    print("%d是完美数 :%s" %( num,str))
else:
    print('%d不是完美数'%num)