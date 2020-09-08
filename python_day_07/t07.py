#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :t07.py
@时间    :2020/09/08 14:33:46
@作者    :江伟
@版本    :1.0
@说明    :
练习6：打印杨辉三角。
'''

def main():
    rows  = int(input('请输入要打印杨辉三角的行数：'))

    N = [1]
    for i in range(rows):
        print(N)
        #杨辉三角的关键在于每次打印之后要在列表最后一位加上0这个元素
        N.append(0)
        N = [N[k] + N[k-1] for k in range(i+2)]



if __name__ == "__main__":
    main()