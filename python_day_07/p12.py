#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p12.py
@时间    :2020/09/07 15:51:50
@作者    :江伟
@版本    :1.0
@说明    :
'''

set1 = {1, 2, 3, 4, 1, 2, 3, 4, 5, 4, 3, 2, 2, 2}
print(set1)#{1, 2, 3, 4, 5}
set2 = set(range(1, 10))
print(set2)#{1, 2, 3, 4, 5, 6, 7, 8, 9}
set3 = set((1,2,3))
print(set3)#{1, 2, 3}


print(set1 & set2)#{1, 2, 3, 4, 5}
# print(set1 .intersection(set2))#{1, 2, 3, 4, 5}
print(set1 | set2)#{1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(set1 .union (set2))#{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set1 - set2)#set()
# print(set1.difference(set2))##set()
print(set2 - set1)#{8, 9, 6, 7}
# print(set2.difference(set1))#{8, 9, 6, 7}
print(set1 ^ set2)#{6, 7, 8, 9}
# print(set1.symmetric_difference(set2))#{6, 7, 8, 9}


#判断子集和超集
print(set1 >= set2)#False
# print(set1.issuperset(set2))
print(set2 <= set3)#False
# print(set1.issubset(set2))


