#!/usr/bin/env python
#! -*- coding:UTF-8 -*-

import random
from cards import Card

list = []

for suit_id in range(1, 5):
    for rank_id in range(1, 14):
        list.append(Card(suit_id, rank_id))

hand = []
for cards in range(0, 5):
    a = random.choice(list)
    print a
    hand.append(a)
    list.remove(a)

print
for card in hand:
    print card.short_name , '=', card.long_name, '   Value:', card.value
