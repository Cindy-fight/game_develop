#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

import time
import urllib

print '一周有 ： 7 * 24 * 60 = ' , 7 * 24 * 60 , '分钟'

print 'My name is Wtt Cindy.'
print 'I was born ' , time.localtime(time.time()) , '.'
print 'My favorite color is blue.'


# file = urllib.urlopen('http://web.com/test-ckeditor.html')
# message = file.read()
# print message

'''
一家商场在降价促销。 如果购买金额低于或等于 10元,会给 10%的折扣, 如果购买金额大于 10元,会给 20% 的折扣。
编写一个程序,询问购买价格, 再显示折扣( 10%或 20%) 和最终价格。
'''
price = int(raw_input('请输入你购买的商品金额：'))
discount1 = 0.1
discount2 = 0.2
percent1 = '10%'
percent2 = '20%'
fee1 = price * (1 - discount1)
fee2 = price * (1 - discount2)

if 0 <= price <= 10:
    print '折扣为 ', percent1
    print '优惠后的商品价格为：', fee1
elif price > 10:
    print '折扣为 ', percent2
    print '优惠后的商品价格为：', fee2
else:
    print '输入错误'


'''
一个足球队在寻找年龄在 10到 12岁之间的小女孩加人。 编写一个程序,询问 用户的年龄和性别 (m 表示男性, f表示女性〉。显示一条消息指出这个人是否可以加入球队 。
额外提示 :要合理地建立程序,如果用 户不是女孩就不必询问年龄。
'''

sex = raw_input('请输入你的性别：男性输入m，女性输入f，输入其他表示放弃：')
if sex == 'f':
    age = int(raw_input('请输入你的年龄：'))
    if 10 <= age <= 12:
        print '你符合我们的要求，欢迎你的加入'
    elif age > 12:
        print '你不符合年龄要求'
    else:
        print '你不符合年龄要求'
else:
    print '不好意思，我们是女生足球队'


'''
你在长途旅行,刚到一个加油站,距下一个加油站还有 200 km. 编写 一个程 序确定是不是需要在这里加油,还是可以等到下一个加油站再加油 tank油箱
额外提示:程序中包含一个 5 升的缓冲区,以防油表不准。
'''

tank_size = float(raw_input('你的油箱有多大，单位是升L：'))
tank_percent = float(raw_input('你的油箱有多满，按百分比，半满就是50%：'))
tank_faraway = float(raw_input('你的汽车每升油能走多远，单位km：'))

distance = float(200)
faraway = float((tank_size * (tank_percent / 100) - 5) * tank_faraway)

print 'Size of tank:' , tank_size
print 'percent full:' , tank_percent
print 'km per liter:' , tank_faraway
print 'You can go another', faraway, 'km'
print 'The next gas station is 200 km away'
if distance > faraway:
    print 'You should get gas now.'
else:
    print 'You can wait for the next station.'


'''
建立一个程序,用户必须输入密码才能使用这个程序。你当然知道密码(因 为它会写在你的代码中〉。
不过,你的朋友要得到这个密码就必须问你或者直接猜,也可以学习足够的 python 知识查看代码来找出密码!
对程序没什么要求,可以是你已经编写的程序,也可以是一个非常简单的程 序,只在用户输入正确的口令时显示一条 "You'rein!" 之类的消息。
'''
password = 'ct123456'
count = 0
while count <= 6:
    guess = raw_input('我刚才设定了一个密码，请猜猜是什么：')
    if guess == password:
        print 'Yes, You are Right! bingo'
        break
    count +=1


