#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :d01.py
@时间    :2020/09/08 16:40:51
@作者    :江伟
@版本    :1.0
@说明    :

面向对象编程基础:

把一组数据结构和处理它们的方法组成对象（object），把相同行为的对象归纳为类（class），
通过类的封装（encapsulation）隐藏内部细节，通过继承（inheritance）实现类的特化（specialization）
和泛化（generalization），通过多态（polymorphism）实现基于对象类型的动态分派。
'''


"""
定义类:
在Python中可以使用class关键字定义类，然后在类中通过之前学习过的函数来定义方法，
这样就可以将对象的动态特征描述出来，代码如下所示。
"""

class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print('%s 正在学习%s'%(self.name,course_name))  

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)    
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.'%self.name)
        else:
            print('%s正在观看动作电影.'%self.name)



#  说明： 写在类中的函数，我们通常称之为（对象的）方法，这些方法就是对象可以接收的消息。               

def main():
     # 创建学生对象并指定姓名和年龄
    stu1 = Student('张三', 18)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()

    
    stu2 = Student('王大锤', 25)
    stu2.study('思想品德')
    stu2.watch_movie()


if __name__ == "__main__":
    main()    