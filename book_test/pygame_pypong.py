#!/usr/bin/env python
#! -*- coding:UTF-8 -*-

import pygame, sys

class MyBallClass(pygame.sprite.Sprite):

    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        global points, score_text
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]
            hit_wall.play()

        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            points = points + 1
            score_text = font.render(str(points), 1, (0, 0, 0))
            get_point.play()


class MyPaddleClass(pygame.sprite.Sprite):

    def __init__(self, location = [0, 0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100, 20])
        image_surface.fill([0, 0, 0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
hit = pygame.mixer.Sound("sounds/hit_paddle.wav")  #球拍击打球的声音
hit.set_volume(0.50)
ball_speed = [10, 5]
myBall = MyBallClass("images/wackyball.bmp", ball_speed, [50, 50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270, 400])
points = 0
lives = 3 #玩家只有三条命

#边打游戏边听歌
pygame.mixer.music.load("sounds/bg_music.mp3")
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play(-1)

hit_wall = pygame.mixer.Sound("sounds/hit_wall.wav")
hit_wall.set_volume(0.30)
get_point = pygame.mixer.Sound("sounds/get_point.wav")
get_point.set_volume(0.40)
splat = pygame.mixer.Sound("sounds/splat.wav")
splat.set_volume(0.30)
new_life = pygame.mixer.Sound("sounds/new_life.wav")
new_life.set_volume(0.60)
game_over = pygame.mixer.Sound("sounds/game_over.wav")
game_over.set_volume(0.50)

while True:
    clock.tick(30)
    screen.fill([255, 255, 255])
    font = pygame.font.Font(None, 50)  # 创建字体对象
    score_text = font.render(str(points), 1, (0, 0, 0))  # 渲染文本
    textpos = [10, 10]  # 设置文本位置
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:  #鼠标事件
            paddle.rect.centerx = event.pos[0]
    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        myBall.speed[1] = -myBall.speed[1]
        hit.play()
    if myBall.rect.top >= screen.get_rect().bottom: # 玩家机会设定
        lives = lives - 1
        splat.play()
        pygame.time.delay(2000)
        myBall.rect.topleft = [50, 50]
        new_life.play()
    if lives <= 0:  # 自己思路，机会为0，打印成绩并退出游戏
        pygame.mixer.music.fadeout(2000)   #结束前，音乐淡出
        game_over.play()
        print 'You Score:', str(points)
        print 'Game Over!'
        sys.exit()
    myBall.move()
    screen.blit(score_text, textpos)  # 将文本移到这个位置

    for i in range(lives):  #增加生命计数器
        width = screen.get_rect().width
        screen.blit(myBall.image, [width - 40 * i, 20])

    screen.blit(myBall.image, myBall.rect)
    screen.blit(paddle.image, paddle.rect)
    pygame.display.flip()

