#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :t06.py
@时间    :2020/09/08 14:24:52
@作者    :江伟
@版本    :1.0
@说明    :
练习6：打印杨辉三角。教案答案
'''

def main():
    num = int(input('请输入打印的行数:'))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

if __name__ == "__main__":
    main()        
