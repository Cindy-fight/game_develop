#!/usr/bin/env python
#！-*- coding:UTF-8 -*-
import os

'''
此文件相关内容有：文件I/O

'''

# input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回

str1 = raw_input("请输入：")
print "你输入的内容是：", str1

str2 = input("请输入：")
print "你输入的内容是：", str2

fp = open('foo.txt', 'a+')

print fp.name
print fp.mode

fp.write('Hello, Python!\nHello, World!\n')

fp.close()


fo = open('foo.txt', 'r+')
content = fo.read()
print '文件中的内容是：', content

position = fo.tell()
print '当前文件位置：', position

# 把指针再次重新定位到文件开头
# position_init = fo.seek(0, 0)

fo.close()

os.rename('foo.txt', 'foo.log')

ft = open('test.txt', 'a+')
ft.write('wtt test\n')
ft.close()

os.remove('test.txt')

