#!/usr/bin/env python
#! -*- coding:UTF-8 -*-

import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("images/beach_ball.png")
screen.blit(my_ball, [50, 50])
pygame.display.flip()

# 隔两秒移动一次沙滩球
pygame.time.delay(2000)
screen.blit(my_ball, [150, 50])
pygame.draw.rect(screen, [255, 255, 255], [50, 50, 90, 90], 0)   # 擦掉第一个球
pygame.display.flip()

# 写个循环玩玩
for i in range(250, 640, 100):
    pygame.time.delay(2000)
    screen.blit(my_ball, [i, 50])
    pygame.draw.rect(screen, [255, 255, 255], [i-100, 50, 90, 90], 0)
    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()