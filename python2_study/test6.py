#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

'''
此文件相关内容有：面向对象

'''

class Animal:

    __privateCount = 0
    publicCount = 0

    def run(self):
        print 'Animal is running...'

    def count(self):
        self.__privateCount += 1
        Animal.publicCount += 1
        print '私有属性的值为：', self.__privateCount

    def hello(self):
        print 'Hello, ', self.__class__.__name__


class Dog(Animal):
    def run(self):
        print 'Dog is running...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

animal = Animal()
animal.count()
animal.count()

dog = Dog()
dog.run()
dog.hello()
dog.count()

cat = Cat()
cat.run()
cat.hello()
cat.count()

print '公共属性的值为：', Animal.publicCount
print '私有属性的值为：', animal._Animal__privateCount  # 访问私有属性的方法

a = Animal()
d = Dog()
c = Cat()

print isinstance(a, Animal)
print isinstance(d, Dog)
print isinstance(c, Cat)
print isinstance(d, Animal)
print isinstance(c, Animal)
