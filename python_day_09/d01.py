#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :d01.py
@时间    :2020/09/09 09:34:03
@作者    :江伟
@版本    :1.0
@说明    :面向对象进阶

在前面的章节我们已经了解了面向对象的入门知识，知道了如何定义类，如何创建对象以及如何给对象发消息。
为了能够更好的使用面向对象编程思想进行程序开发，我们还需要对Python中的面向对象编程进行更为深入的了解。
'''


"""
@property装饰器:
之前我们讨论过Python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，
但是如果直接将属性暴露给外界也是有问题的，比如我们没有办法检查赋给属性的值是否有效。
我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问，
那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。
如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便，
代码如下所示。

"""


class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # setter

    # @name.setter
    # def name(self, name):
    #     self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age < 16:
            print('%s 正在玩飞行棋' % self._name)
        else:
            print('%s 正在玩围棋' % self._name)

def main():
    person = Person('张三',15)
    person.play()#张三 正在玩飞行棋
    person.age = 22
    person.name = '李四'
    #如果注释掉name的setter方法会报以下错误
    #AttributeError: can't set attribute
    person.play()#李四 正在玩围棋
    

if __name__ == "__main__":
    main()