#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

'''
此文件相关内容有：数字、字符串、列表、元组、字典、 日期和时间

'''

from math import ceil
from math import exp
from math import fabs
from math import floor, log, e, log10, modf, sqrt
from random import choice, randrange, random, seed, shuffle, uniform
import time
import calendar

x = -10
y = 18

print abs(x)

print ceil(4.1)

# 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
print cmp(3, 5)

# 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
print exp(1)
print exp(2)

print fabs(x)

# 注意：abs 与 fabs 的区别， abs(-10) 返回10；fabs(-10)返回10.0

print floor(4.9)  # 4.0

print floor(-4.9)  # -5.0

print log(e)  # 1.0

print log(1000, 10)  # 3.0

print log10(100)

print max(range(1, 100))

print min(range(1, 100))

print modf(100.12)

print pow(3, 2)

print round(3.1415926, 3)

print sqrt(3)

# 从序列的元素中随机挑选一个元素
print choice(range(100))

# 从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1   randrange ([start,] stop [,step])
print randrange(0, 88, 3)

# 	随机生成下一个实数，它在[0,1)范围内
print random()

# 改变随机数生成器的种子seed
seed(10)
print 'Random number with seed 10: ', random()

# shuffle  将序列的所有元素随机排序
list = [18, 6, 99, 303]
shuffle(list)
print list

# uniform 随机生成下一个实数，它在[x,y]范围内
print uniform(1, 100)

L1 = [188,'cindy', 991, 'age', 'student']

L2 = [977,'lucy', 990, 'sex', 'student']

print cmp(L1, L2)

print len(L1)

print max(L1)

print min(L1)

L1.append('cindy')
print L1

print L1.count('cindy')

L1.extend(L2)    # 追加元素（列表）
print L1

print L1.index('cindy')  # 找出匹配的第一个索引位置

L1.insert(1, 'test')  # 在位置1 插入'test'元素
print L1

L1.pop()  # 删除最后一个元素
print L1

L1.remove('cindy')  # 移除某个值的第一个匹配项
print L1

L1.reverse()  # 反向列表中的元素
print L1

L1.sort()  # 正序
print L1

L1.sort(reverse=True)  # 倒序
print L1

# 删除字典元素
dict = {'name':'Cindy', 'age':'18', 'class': 'four', 'hobby':'programming'}
print dict
del dict['hobby']  # 删除某个值
print dict
dict.clear()   # 清空字典所有条目
print dict
del dict     # 删除字典

'''
字典键的特性
1、不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个会被记住
2、键必须不可变。可以用数字、字符串或者元祖充当，但是列表不行

'''

d = {'name':'Cindy', 'age':'18', 'hobby':'programming'}
d2 = {'address':'zhangJiang'}
print d

print d.copy()

print d.fromkeys(range(3), d.values())

print d.get('name')

print d.has_key('hobby')

print d.items()

print d.keys()

print d.values()

# print d.setdefault('sex', default='none')  # 未看到效果 ，不理解

d.update(d2)
print d

d.pop('age')
print d

print d.popitem()

print d

# 时间和日期

print '当前时间戳为：', time.time()

localtime = time.localtime(time.time())

print '本地时间是：', localtime

print '格式化后的时间为：', time.asctime(localtime)

print time.strftime("%Y-%m-%d %H:%M:%s", time.localtime())

print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

str = "Fri Dec 01 17:04:25 2017"
print time.mktime(time.strptime(str, "%a %b %d %H:%M:%S %Y"))

cal = calendar.month(2017, 12)
print "以下输出2017年12月份的日历："
print cal

print time.timezone

print time.tzname

print calendar.calendar(2017, w=2, l=1, c=6)  # 效果等同于calendar.calendar(2017)

# print calendar.calendar(2017)

print calendar.calendar(2017, w=5, l= 2, c =8)

print calendar.firstweekday()

print '2016是否是闰年', calendar.isleap(2016)

print '2000到2020之间的闰年有', calendar.leapdays(2000, 2020), '个'

print calendar.month(2017, 12, w = 4, l = 3)

print calendar.monthcalendar(2017, 12)

print calendar.monthrange(2017, 12)

calendar.prcal(2017)  # 等价于 print calendar.calendar(2017, w=2, l=1, c=6)

calendar.prmonth(2017, 12)  # 等价于 print calendar.month(2017, 12, w = 2, l = 1)

# calendar.setfirstweekday(0)

# calendar.timegm()

# 返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）
print '\n2017.12.1的日期码是', calendar.weekday(2017, 12, 1)

