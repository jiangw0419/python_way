#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :module3.py
@时间    :2020/08/28 18:08:49
@作者    :江伟
@版本    :1.0
@说明    :注意：
如果我们导入的模块除了定义函数之外还中有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码，
事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，
最好是将这些执行代码放入如下所示的条件中，这样的话除非直接运行该模块，
if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是"__main__"。
'''

def foo():
    print("hello world")

def bar():
    print("goodbye world")



# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__

if __name__ == "__main__":
    print("foo()")
    foo()
    print("bar()")
    bar()
  



