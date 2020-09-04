#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :testpmodule.py
@时间    :2020/08/28 17:59:23
@作者    :江伟
@版本    :1.0
@说明    : 测试不同的module引入相同命名的函数
'''

from module1 import foo
import module2 as m2

foo() #输出结果：hello world!

m2.foo() #输出结果：goodbye world


