#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :p02.py
@说明    :百分制成绩转换为等级制成绩。

要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。

@时间    :2020/08/24 17:48:57
@作者    :江伟
@版本    :1.0
'''

score = float(input('请输入成绩'))

if(score >= 90):
    level = 'A'
elif (score >=80):
    level = 'B'
elif (score >= 70):
    level = 'C'
elif (score >= 60):
    level = 'D'
else:
    level = 'E'   

print('%.1f 分的等级为：%s'%(score,level))


