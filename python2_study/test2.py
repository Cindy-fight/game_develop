#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

'''
此文件相关内容是：循环语句，包括：while 、for、 break、 continue、 pass

'''

# print 9*9乘法表  use while、for

# method1 use while

i = 1
while i < 10:
    j = 1
    while j <= i:
        print j , '*', i , '=', i * j,' ',
        j += 1
    print "\n"
    i += 1


# method2 use while

list1 = list(range(1, 10))
list2 = list(range(1, 10))
for x in list1:
    for y in list2:
        if y <= x:
            print y, '*', x, '=', y * x, ' ',
    print "\n"


# 获取100以内的质数

num = []
for a in range(2, 100):
    b = 2
    for b in range(2, a):
        if a % b == 0:
            break
    else:
        num.append(a)
print '100以内的质数有：', num


# the difference between break and continue

# first
for letter in 'Python':
    if letter == 'h':
        break
    print '当前字母：', letter
print "========================="

for letter in 'Python':
    if letter == 'h':
        continue
    print '当前字母：', letter
print "========================="

# second
var = 10
while var > 0:
    print '当期变量值：', var
    var -= 1
    if var == 5:
        break
print 'Good bye!'
print "========================="

var = 10
while var > 0:
    print '当期变量值：', var
    var -= 1
    if var == 5:
        continue
print 'Good bye!'