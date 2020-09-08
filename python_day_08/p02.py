#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p02.py
@时间    :2020/09/08 17:15:34
@作者    :江伟
@版本    :1.0
@说明    :
练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
'''

from math import sqrt

class Point(object):
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def move_to(self, x, y):
        self._x = x
        self._y = y

    def move_by(self, x, y):
        self._x += x
        self._y += y

    def distance_to(self,other):
        dx = self._x - other._x
        dy = self._y - other._y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self._x), str(self._y))

def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)#(3, 5)
    print(p2)#(0, 0)
    p2.move_by(-1, 2)
    print(p2)#(-1, 2)
    print(p1.distance_to(p2))#5.0


if __name__ == "__main__":
    main()

