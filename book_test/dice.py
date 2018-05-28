#!/usr/bin/env python
#! -*- coding:UTF-8 -*-

import random


# 掷骰子游戏
totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(1000):
    # dice_total = random.randint(2, 12)
    # totals[dice_total] += 1

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    totals[dice_1+dice_2] += 1

for i in range(2, 13):
    print 'total', i, 'came up', totals[i], 'times.'


# 掷硬币游戏

heads_in_row = 0
ten_heads_in_row = 0
for i in range(1000000):
    coin = random.randint(0, 1)  # 0表示正面 1表示反面
    if(coin == 0):
        heads_in_row += 1
    else:
        heads_in_row = 0

    # 连续正面朝上10次 +1
    if heads_in_row == 10:
        ten_heads_in_row += 1
        heads_in_row = 0

print '连续10次面朝上的次数：', ten_heads_in_row
