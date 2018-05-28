#!/usr/bin/env python
#! -*- coding:UTF-8 -*-

import pygame, sys

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([640, 480])
pygame.time.delay(1000)

#先播放一首音乐，声音是最大音量的30%；播放完毕后播放"嘟嘟声"，音量50%
pygame.mixer.music.load("sounds/bg_music.mp3")
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play(3)  # 重复播放三次，若为负数，则会一直循环
sound = pygame.mixer.Sound("sounds/splat.wav")
sound.set_volume(0.50)
sound.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if not pygame.mixer.music.get_busy():  #等待歌曲播放完毕之后再播放 嘟嘟声
        sound.play()
        pygame.time.delay(1000)
        sys.exit()


