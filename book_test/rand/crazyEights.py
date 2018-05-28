#!/usr/bin/env python
#! -*- coding:UTF-8 -*-

"""

Crazy Eights 游戏：

条件：两个玩家参与，每个玩家有5张牌，翻开一张牌，开始出牌
目标：在另一个人之前而且在取完一副牌之前出光所有牌

规则：
1、 每一轮，玩家必须做下面的操作之一
 （1）出一张牌，要与翻开的牌花色相同
 （2）出一张牌，要与翻开的牌点数相同
 （3）出一张8
2、如果玩家出了一张'8'，他可以叫'花色'，这说明他可以选择花色，下一个玩家要根据这个花色出牌
3、如果玩家无法出牌，必须从这副牌中选择一张牌，增加到自己手中
4、如果玩家出光了手中所有的牌，他就赢了，根据另一个玩家手中剩余的牌计算得分
 （1）每个8得50分
 （2）每个花牌（J Q K）得10分
 （3）每个 A 得1分
 （4）每个其他的牌按分值得分
5、如果一副牌花光时仍没有人获胜，游戏结束。在这种情况下，每个玩家会根据对方剩余的牌计算得分
6、可以一直玩到达到某个总分，或者直到你累了，得分最高的获胜

"""

import random
from cards import Card

# 初始化
def init_cards():
    global deck, p_hand, c_hand, up_card, active_suit
    deck = []
    # 建立一副牌
    for suit_id in range(1, 5):
        for rank_id in range(1, 14):
            new_card = Card(suit_id, rank_id)
            if new_card.rank == '8':
                new_card.value = 50
            deck.append(new_card)

    # 创建玩家的一手牌 5张
    p_hand = []
    for cards in range(0, 5):
        card = random.choice(deck)
        p_hand.append(card)
        deck.remove(card)

    # 创建计算机的一手牌 5张
    c_hand = []
    for cards in range(0, 5):
        card = random.choice(deck)
        c_hand.append(card)
        deck.remove(card)

    # 随机显示第一张名牌 及当前花色
    card = random.choice(deck)
    deck.remove(card)
    up_card = card
    active_suit = up_card.suit


# 出8时 得到新花色
def get_new_suit():
    global active_suit
    got_suit = False
    while not got_suit:
        suit = raw_input("Pick a suit : ")
        if suit.lower() == 'd':
            active_suit = 'Diamond'
            got_suit = True
        elif suit.lower() == 'h':
            active_suit = 'Hearts'
            got_suit = True
        elif suit.lower() == 'c':
            active_suit = 'Clubs'
            got_suit = True
        elif suit.lower() == 's':
            active_suit = 'Spades'
            got_suit = True
        else:
            print 'Not a valid suit. Try again. ',
    print 'You picked', active_suit


# 玩家选择
def player_turn():
    global deck, p_hand, blocked, up_card, active_suit
    valid_play = False
    is_eight = False
    print "\nYour hand: ",
    for card in p_hand:
        print card.short_name,
    print '\nUp card :', up_card.short_name
    if up_card.rank == '8':
        print 'Suit is ', active_suit
    print 'What would you like to do?',
    response = raw_input("Type a card to play or 'Draw' to take a card: ")

    while not valid_play:
        selected_card = None
        while selected_card == None:
            if response.lower() == 'draw':
                valid_play = True

                if len(deck) > 0:
                    card = random.choice(deck)
                    p_hand.append(card)
                    deck.remove(card)
                    print 'You drew ', card.short_name
                else:
                    print "There are no cards left in the deck."
                    blocked += 1
                return
            else:
                for card in p_hand:
                    if response.upper() == card.short_name:
                        selected_card = card
                if selected_card == None:
                    response = raw_input('You do not have that card. Try again:')

        if selected_card.rank == '8':
            valid_play = True
            is_eight = True
        elif selected_card.suit == active_suit:
            valid_play = True
        elif selected_card.rank == up_card.rank:
            valid_play = True

        if not valid_play:
            response = raw_input('That is not a legal play. Try again:')

    p_hand.remove(selected_card)
    up_card = selected_card
    active_suit = up_card.suit
    print 'You played ', selected_card.short_name
    if is_eight:
        get_new_suit()


# 计算机选择
"""

计算机出牌规则：
1、有8就总是出8，如果出8，挑选新花色，规则是 统计计算机手中每种花色各有多少张牌，并选择牌数最多的花色
2、若没有8，检查所有牌，查看哪些牌可以出，挑选分值最大的牌
3、若无法出牌，则抽牌。抽排规则和人类玩家一样。

"""
def computer_turn():
    global c_hand, deck, up_card, active_suit, blocked
    options = []
    for card in c_hand:
        if card.rank == '8':
            c_hand.remove(card)
            up_card = card
            print 'Computer played ', card.short_name
            #suit_totals = ['Diamond', 'Hearts', 'Clubs', 'Spades']
            suit_totals = [0, 0, 0, 0]
            for suit in range(1, 5):
                for card in c_hand:
                    if card.suit_id == suit:
                        suit_totals[suit-1] += 1   # 与示例代码不一致  请注意, 已想通

            long_suit = 0
            for i in range(4):
                if suit_totals[i] >long_suit:
                    long_suit = i
            if long_suit == 0:
                active_suit = 'Diamond'
            if long_suit == 1:
                active_suit = 'Hearts'
            if long_suit == 2:
                active_suit = 'Clubs'
            if long_suit == 3:
                active_suit = 'Spades'
            print 'Computer changed suit to ', active_suit
            return
        else:
            if card.suit == active_suit:
                options.append(card)
            elif card.rank == up_card.rank:
                options.append(card)

    if len(options) > 0:
        best_play = options[0]
        for card in options:
            if card.value > best_play.value:
                best_play = card

        c_hand.remove(best_play)
        up_card = best_play
        active_suit = up_card.suit
        print 'Computer played ', best_play.short_name
    else:
        if len(deck) > 0:
            next_card = random.choice(deck)
            c_hand.append(next_card)
            deck.remove(next_card)
            print 'Computer drew a card'  # 这里不应该显示给计算机发了什么牌 若显示，有点耍赖 next_card.short_name
        else:
            print 'Computer is blocked '
            blocked += 1
    print "Computer has %i cards left" % len(c_hand)



# 主循环
done = False
p_total = c_total = 0
while not done:
    game_done = False
    blocked = 0
    init_cards()
    while not game_done:
        player_turn()
        if len(p_hand) == 0:
            game_done = True
            print
            print 'You won!'

            # display game score here
            p_points = 0
            for card in c_hand:
                p_points += card.value
            p_total += p_points
            print "You got %i points for computers hand " % p_points

        if not game_done:
            computer_turn()
        if len(c_hand) == 0:
            game_done = True
            print
            print 'Computer won!'

            # display game score here
            c_points = 0
            for card in p_hand:
                c_points += card.value
            c_total += c_points
            print "Computer got %i points for your hand " % c_points

        if blocked >= 2:
            game_done = True
            print 'Both players blocked . GAME OVER.'

            # 双方都无法继续 所以双方都得分
            p_points = 0
            for card in c_hand:
                p_points += card.value
            p_total += p_points

            c_points = 0
            for card in p_hand:
                c_points += card.value
            c_total += c_points

            print 'You got %i points for cards left in computers hand' % p_points
            print 'Computer got %i points for cards left in your hand' % c_points

    play_again = raw_input("Play again (Y/N)? ")
    if play_again.lower().startswith('y'):
        done = False
        print "\nSo far, you have %i points and the computer has %i points.\n" % (p_total, c_total)
    else:
        done = True

print "\nFinal Score:"
print "You : %i     Computer : %i " % (p_total, c_total)
