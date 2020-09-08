#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p01.py
@时间    :2020/09/08 17:05:42
@作者    :江伟
@版本    :1.0
@说明    :

面向对象的支柱

面向对象有三大支柱：封装、继承和多态。后面两个概念在下一个章节中进行详细的说明，这里我们先说一下什么是封装。
我自己对封装的理解是"隐藏一切可以隐藏的实现细节，只向外界暴露（提供）简单的编程接口"。
我们在类中定义的方法其实就是把数据和对数据的操作封装起来了，在我们创建了对象之后，
只需要给对象发送一个消息（调用方法）就可以执行方法中的代码，
也就是说我们只需要知道方法的名字和传入的参数（方法的外部视图），
而不需要知道方法内部的实现细节（方法的内部视图）。

'''

"""
练习1：定义一个类描述数字时钟。
"""

from time import sleep

class Clock(object):
    """数字时钟"""

    def __init__(self,hour=0,min=0,second=0):
        self._hour = hour
        self._min = min
        self._second = second

    def show(self):
        """显示时间"""    
        return '%02d:%02d:%02d' % (self._hour,self._min,self._second)

    def run(self):
        """走"""   
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._min += 1
            if self._min == 60:
                self._min = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
         


def main():
    clock = Clock(23,59,57)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == "__main__":
    main()                