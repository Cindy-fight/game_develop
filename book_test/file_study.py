#!/usr/bin/env python
#! -*- coding:UTF-8 -*-

# readlines 和 readline 只能用于读取文本文件
notes = open('notes.txt', 'r')
content = notes.readlines()
print content
notes.close()

my_file = open('new_file.txt', 'a+')
my_file.write("Hello there, neighbor!")
print >> my_file, "\nHello World!"
my_file.close()