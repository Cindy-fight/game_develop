#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

'''
此文件相关内容有：面向对象

'''

class Employee:

    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total employee %d" % Employee.empCount

    def displayEmployee(self):
        print 'Name:',self.name, " ", 'Salary:', self.salary


e = Employee('Cindy', 3000)
e.displayCount()
e.displayEmployee()


em = Employee('Jack', 6000)
em.displayCount()
em.displayEmployee()

print Employee.empCount

em.age = 16
print 'Age:', em.age

print 'Employee.__doc__:', Employee.__doc__
print 'Employee.__name__:', Employee.__name__
print 'Employee.__module__:', Employee.__module__
print 'Employee.__bases__:', Employee.__bases__
print 'Employee.__dict__:', Employee.__dict__


# 析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, '销毁'

pt = Point()
print pt.__class__.__name__
pt2 = pt
pt3 = pt
print id(pt), id(pt2), id(pt3)

# 疑问：删除与不删除结果一样
del pt
del pt2
del pt3




