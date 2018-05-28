#!/usr/bin/env python
#! -*- coding:UTF-8 -*-

import pygame, sys
from random import *

class MyBallClass(pygame.sprite.Sprite):

    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

def animate(group):
    screen.fill([255, 255, 255])
    for ball in group:
        ball.move()
    for ball in group:
        group.remove(ball)  #从组删除精灵
        if pygame.sprite.spritecollide(ball, group, False): #检查精灵与组之间的碰撞
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
        group.add(ball)  #将球再添加回原来的组中
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    # pygame.time.delay(50)


size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
image_file = "images/beach_ball.png"
clock = pygame.time.Clock()  # 创建一个clock对象
group = pygame.sprite.Group()
for row in range(0, 3):
    for column in range(0, 3):
        location = [column * 180 + 10, row * 180 + 10]
        speed = [choice([-5, 5]), choice([-5, 5])]
        ball = MyBallClass(image_file, location, speed)
        group.add(ball)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            frame_rate = clock.get_fps()  #实际帧速率
            print 'frame_rate:', frame_rate
            sys.exit()
    animate(group)
    clock.tick(30) #设置期望帧速率

