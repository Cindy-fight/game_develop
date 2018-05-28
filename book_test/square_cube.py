#!/usr/bin/env python
#! -*- coding:UTF-8 -*-

print "Number\tSquare\tCube"
for i in range(1,11):
    print i, '\t', i**2, '\t', i**3

age = 18
print 'I am %i years old' % age

number1 = 18.88
number2 = - 19.98

print '% .2f' % number1
print '% .2f' % number2

print '%.2E' % number1
print '%.2e' % number1

name_string = "Sam,Brad,Alex,Cameron,Toby,Gwen,Jenn,Connor"
names = name_string.split(',')
print names

word_list = ['My' , 'name' , 'is' , 'Cindy']
string = ' ha ha ' . join(word_list)
print string

print string.startswith('My')

print string.startswith('My na')

print string.endswith('y')

print string.endswith('Cindy')

s = 'Hello World!'
if 'l' in s:
    position = s.index('l')
    print "Found 'l' at index ", position

# strip 相当于php的trim
name_1 = name_string.strip('norS')
print name_1

up = s.upper()
lo = s.lower()
print up
print lo

for i in range(1, 9):
    print i, '/ 8 = % .3f' % float(i * 1000 / 8 / 1000)


