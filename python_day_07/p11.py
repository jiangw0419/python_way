#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p11.py
@时间    :2020/09/07 11:16:23
@作者    :江伟
@版本    :1.0
@说明    :集合
参考--p11集合.md文件示意图

1：a.intersection(b)            a与b交集
2: a.sysmmetricDifference(b)    a与b去除交集部分
3: a.union(b)                   a与b并集    
4: a.substracting(b)            a与b,a中不包括b的部分
'''

seta = {1,2,3,4,3,3,3}
#默认去重
print(seta)#{1, 2, 3, 4}
print('Length=',len(seta))#Length= 4

setb = set(range(1,10))
setc = set((1,2,3,4,3,3))
print(setb,setc)#{1, 2, 3, 4, 5, 6, 7, 8, 9} {1, 2, 3, 4}

# 创建集合的推导式语法(推导式也可以用于推导集合)
# set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# print(set4)


"""向集合添加元素和从集合删除元素。"""
seta.add(5)
print(seta)#{1, 2, 3, 4, 5}
setb.update([11,12])
print(setb)#{1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}
#去掉元素11
setb.discard(11)
print(setb)#{1, 2, 3, 4, 5, 6, 7, 8, 9, 12}

if 12 in setb:
        setb.remove(12)

print(setb)#{1, 2, 3, 4, 5, 6, 7, 8, 9}
#移除第一个
print(setb.pop())#1
print(setb)#{2, 3, 4, 5, 6, 7, 8, 9}
