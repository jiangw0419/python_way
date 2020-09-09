#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :d02.py
@时间    :2020/09/09 09:48:01
@作者    :江伟
@版本    :1.0
@说明    :__slots__魔法
'''
"""
我们讲到这里，不知道大家是否已经意识到，Python是一门动态语言。通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，
当然也可以对已经绑定的属性和方法进行解绑定。但是如果我们需要限定自定义类型的对象只能绑定某些属性，
可以通过在类中定义__slots__变量来进行限定。需要注意的是__slots__的限定只对当前类的对象生效，
对子类并不起任何作用。
"""

class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name','_age','_gender')

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

    def toString(self):
        print('姓名：%s 年龄：%d'%(self._name,self._age))        
        # print('姓名：%s 年龄：%d 性别:%s'%(self._name,self._age,self._gender))  #AttributeError: _gender      

def main():
    person = Person('张三',22)
    person.play()#张三 正在玩围棋
    person.toString()#姓名：张三 年龄：22
    person._gender = '男'
    person._name = '李四'
    person.play()
    person.toString()#姓名：李四 年龄：22
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True


if __name__ == "__main__":
    main()                