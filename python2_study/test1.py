#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

'''
此文件相关内容是：基础语法、变量类型、运算符

'''

counter = 100
miles = 10000.00
name = 'Cindy'

print counter
print miles
print name

a = b = c = 1
print a, b, c

a , b, c = [1, 2, 3] , {'name':'bao'}, 'Hello, World!'
print a, b, c

var1 = 123
var2 = name

print var1
print var2

del var1
del var2

# print var1
# print var2

s = 'ILovePython'
print s
print s[1:5]
print s[5]

str = 'Hello World!'

print str
print str[0]
print str[2:5]
print str[2:]
print str * 3
print str + 'WTT TEST'
print str[-6:]

L = list(range(100))
print L
print L[:10]
print L[-10:]
print L[10:20]
print L[:10:2]  # 前十个数 每两个取一个
print L[::5]  # 所有数，每五个取一个
print L[:]   # 原样复制L

# pay attention to:list  tuple
# list是可以修改的  tuple不能修改，相当于只读列表
# 加号 + 是列表连接运算符，星号 * 是重复操作

list = ['Jack', 88, 'Rose', 99.2]
tinyList = [123, 'bao']
print list[1:3]
print list + tinyList

tuple = ('Jack', 88, 'Rose', 99.2)
tinyTuple = (123, 'bao')
print tuple[0:2]
print tuple * 2 + tinyTuple

list[2] = 'Cindy'
print list

# tuple[3] = 59.99
# print tuple

# tuple and list
test_tuple = ('Jack', '88', ['name', 'Cindy', 'score', 98])
print test_tuple
test_tuple[2][3] = 59.9
print test_tuple

# tuple and dict
tuple_dict = ('Jack', '88', {'name':'Cindy', 'age':18, 'sex':'F'})
print tuple_dict
tuple_dict[2]['name'] = 'WangTT'
print tuple_dict

# 列表list 类似于 索引数组， 字典dict 相当于 关联数组

dict = {'name':'Cindy', 'age':18, 'sex':'F', 'hobby':'programming'}
print dict
print dict.keys()
print dict.values()

# complex 创建一个复数 a + bj
comp = complex(1,2)
print comp

# eval() 函数用来执行一个字符串表达式，并返回表达式的值
x = 7; y = 3
print eval('3 * x')
print eval('pow(x, y)')

# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
a = set('tooth')
b = set('google')
print a, b
print a & b   # 交集
print a | b   # 并集
print a - b   # 差集
print b - a

# frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素
f1 = frozenset(range(10))
print f1
f2 = frozenset('programming')
print f2

# chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的ASCII字符（将一个整数转换为一个ASCII字符）
print chr(0x30), chr(0x31), chr(0x61)  # 十六进制
print chr(48), chr(49), chr(97), chr(65)  # 十进制

# unichr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的 unicode 字符 （将一个整数转换为Unicode字符）
print unichr(48), unichr(49), unichr(65), unichr(97), unichr(98)

# ord() 将一个字符转换为它的整数值
print ord('a'), ord('b'), ord('0'), ord('A')

# hex()  将一个整数转换为一个十六进制字符串
print hex(255), hex(18)

# oct() 将一个整数转换为一个八进制字符串
print oct(255), oct(18)

n = 123
print type(n)
print isinstance(n, int)

# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。

number1 = 256
number2 = 256
print number1 is number2    # True
print number1 == number2

number3 = 6789
number4 = 6789
print number3 is number4
print number3 == number4

def judge():
    number5 = 6789
    print number4 is number5
    print number4 == number5

judge()
