#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :t01.py
@时间    :2020/09/07 18:12:04
@作者    :江伟
@版本    :1.0
@说明    :
练习1：在屏幕上显示跑马灯文字。
'''

import os
import time

def main():
    content = '北京欢迎你,为你开天辟地....'
    t = 0.0
    while t<=2:
        # 清理屏幕上的输出
        os.system('clear')
        print(content)
        t += 0.2
        time.sleep(t)
        content = content[1:]+content[0]

if __name__ == "__main__":
    main()

