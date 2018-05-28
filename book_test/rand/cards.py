#!/usr/bin/env python
#! -*- coding:UTF-8 -*-

# 纸牌游戏

'''
suit_id 表示花色，是一个从1到4的数，其中1=方块(Diamond)， 2=红桃♥️ (Hearts)， 3=梅花♣️ (Clubs)， 4=黑桃 ♠️ (Spades）
rank_id 是从1到13的数， 分别表示 A 2 3 4 5 6 7 8 9 10 J Q K
rank  名称
value 数值
'''

class Card():

    def __init__(self, suit_id, rank_id):
        self.suit_id = suit_id
        self.rank_id = rank_id
        if self.rank_id == 1:
            self.rank = 'Ace'
            self.value = 1
        elif self.rank_id == 11:
            self.rank = 'Jack'
            self.value = 10
        elif self.rank_id == 12:
            self.rank = 'Queen'
            self.value = 10
        elif self.rank_id == 13:
            self.rank = 'King'
            self.value = 10
        elif 2 <= self.rank_id <= 10:
            self.rank = str(self.rank_id)
            self.value = self.rank_id
        else:
            self.rank = 'RankError'
            self.value = -1

        if self.suit_id == 1:
            self.suit = 'Diamond'
        elif self.suit_id == 2:
            self.suit = 'Hearts'
        elif self.suit_id == 3:
            self.suit = 'Clubs'
        elif self.suit_id == 4:
            self.suit = 'Spades'
        else:
            self.suit = 'SuitError'

        self.short_name = self.rank[0] + self.suit[0]
        if self.rank == '10':
            self.short_name = self.rank + self.suit[0]
        self.long_name = self.rank + ' of ' + self.suit


