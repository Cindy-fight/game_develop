#!/usr/bin/env python
#! -*- coding:UTF-8 -*-

import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("images/beach_ball.png")

x = 50
y = 50
x_speed = 5
y_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width():
        x = -90
    if y > screen.get_height():
        y = -90
    screen.blit(my_ball, [x, y])
    pygame.display.flip()