#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :d06.py
@时间    :2020/09/09 11:17:38
@作者    :江伟
@版本    :1.0
@说明    :继承和多态
刚才我们提到了，可以在已有类的基础上创建新类，这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，
从而减少重复代码的编写。提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍生类。
子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，在实际开发中，
我们经常会用子类对象去替换掉一个父类对象，这是面向对象编程中一个常见的行为，对应的原则称之为里氏替换原则。
下面我们先看一个继承的例子。
'''


class Person(object):
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age < 16:
            print('%s 正在玩飞行棋' % self._name)
        else:
            print('%s 正在下围棋' % self._name)

    def watch_tv(self):
        if self._age >= 18:
            print('%s正在观看动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)


class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))




class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))




def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_tv()

    t = Teacher('骆昊', 38, '砖家')
    t.teach('Python程序设计')
    t.watch_tv()
    


if __name__ == '__main__':
    main()
