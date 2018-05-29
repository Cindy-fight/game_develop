#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

'''
此文件相关内容有：正则表达式

'''

import re

print(re.match('www', 'www.runoob.com').span())

print(re.match('com', 'www.runoob.com'))

'''
re.match与re.search的区别:
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
'''

line = 'Cats are smarter than Dogs'

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print 'matchObj.group():', matchObj.group()
    print 'matchObj.group(1)', matchObj.group(1)
    print 'matchObj.group(2)', matchObj.group(2)
else:
    print 'No match!!'


searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print 'searchObj.group():', searchObj.group()
    print 'searchObj.group(1):', searchObj.group(1)
    print 'searchObj.group(2):', searchObj.group(2)
else:
    print 'Nothing found!!'