#!/usr/bin/env python
#! -*- coding:UTF-8 -*-

import pygame, sys
import random, time

WINDOW_H = 768
WINDOW_W = 512
pygame.init()
screen = pygame.display.set_mode([WINDOW_W, WINDOW_H])



# class Item(): # 地图元素类
#     def __init__(self, img_path, x, y):
#         self.img = pygame.image.load(img_path)
#         self.x = x
#         self.y = y





class Map():  # 地图类
    def __init__(self, img_path, x, y):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y

        self.img2 = pygame.image.load(img_path)
        self.x2 = x
        self.y2 = y - WINDOW_H


    def move(self):
        self.y += 3
        self.y2 += 3





class Bullet():
    def __init__(self, img_path, x, y):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y


    def move(self):
        self.y -= 8


    def is_hit_enemy(self, enemy):
        return pygame.Rect.colliderect(pygame.Rect(self.x, self.y, 20, 31), pygame.Rect(enemy.x, enemy.y, 100, 68))





class EnemyPlane():
    def __init__(self, img_path, x, y):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y

        self.is_hited = False
        self.anim_index = 0 # 记录动画索引

    hit_sound= pygame.mixer.Sound("res/baozha.ogg")


    def move(self):
        if not self.is_hited:
            self.y += 10


    def reset(self):  # 数据重置
        self.__init__("images/img-plane_%d.png" % random.randint(1, 7), random.randint(0, WINDOW_W-120), random.randint(-700, -70))


    def plane_down(self): # 敌机爆炸
        if self.anim_index >= 21:
            self.reset()
            return
        elif self.anim_index == 0:
            self.hit_sound.play()
        self.img = pygame.image.load("images/bomb-%d.png" % (self.anim_index // 3 + 1))
        self.anim_index += 1





class HeroPlane():
    def __init__(self, img_path, x, y):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y

        self.bullet_list = []
        self.is_hited = False
        self.anim_index = 0  # 记录动画索引


    def move_left(self):
        self.x -= 5


    def move_right(self):
        self.x += 5


    def move_up(self):
        self.y -= 5


    def move_down(self):
        self.y += 5


    def fire(self):
        bullet = Bullet("images/bullet_9.png", self.x + 50, self.y - 30)
        self.bullet_list.append(bullet)


    def is_hit_enemy(self, enemy):
        return pygame.Rect.colliderect(pygame.Rect(self.x, self.y, 120, 78), pygame.Rect(enemy.x, enemy.y, 100, 68))


    def plane_down(self):
        if self.anim_index >= 21:
            self.is_hited = True
            return True
        self.img = pygame.image.load("images/bomb-%d.png" % (self.anim_index // 3 + 1))
        self.anim_index += 1





# class GameText():
#     def __init__(self, content, font_size, x, y):
#         self.font_size = font_size
#         self.content = content
#         self.x = x
#         self.y = y





class Game():
    def __init__(self):

        pygame.display.set_caption("Plane War v1.24")   # 设置标题
        game_ico = pygame.image.load("res/app.ico")   # 设置图标
        pygame.mixer.music.load("res/bg2.ogg")   # 加载背景音乐
        self.gameover_sound = pygame.mixer.Sound("sounds/gameover.wav")  # 游戏结束时的音效 （超级玛丽）
        pygame.mixer.music.play(-1)   # 循环播放背景音乐

        self.window = screen
        self.map = Map("images/img_bg_level_%d.jpg" % random.randint(1, 5), 0, 0)
        self.hero_plane = HeroPlane("images/hero2.png", 300, 500)
        self.enemy_planes = []
        for _ in range(5):
            enemy_plane = EnemyPlane("images/img-plane_%d.png" % random.randint(1,7), random.randint(0, WINDOW_W-120), random.randint(-700, -70))
            self.enemy_planes.append(enemy_plane)

        self.score = 0
        self.is_over = False


    def draw_map(self):
        # 背景图
        if self.map.y >= WINDOW_H:
            self.map.y = 0
            self.map.y2 = -WINDOW_H
        self.window.blit(self.map.img, (self.map.x, self.map.y))
        self.window.blit(self.map.img2, (self.map.x2, self.map.y2))



    def draw_hero_plane(self):
        # 飞机图
        for enemy_plane in self.enemy_planes:
            if self.hero_plane.is_hited:
                self.is_over = self.hero_plane.plane_down()
            elif not enemy_plane.is_hited:
                if self.hero_plane.is_hit_enemy(enemy_plane):
                    enemy_plane.is_hited = True
                    self.hero_plane.is_hited = True
                    self.is_over = self.hero_plane.plane_down()

        self.window.blit(self.hero_plane.img, (self.hero_plane.x, self.hero_plane.y))



    def draw_bullet(self):
        # 子弹图
        out_window_bullets = []
        for bullet in self.hero_plane.bullet_list:
            if bullet.y >= -30:  # 在边界内

                for enemy_plane in self.enemy_planes:  # 和每架敌机碰撞检测
                    if not enemy_plane.is_hited:  # 只和没有被击中的敌机进行检测

                        if bullet.is_hit_enemy(enemy_plane):
                            out_window_bullets.append(bullet)
                            enemy_plane.is_hited = True
                            self.score += 10
                            break
                self.window.blit(bullet.img, (bullet.x, bullet.y))

            else:
                out_window_bullets.append(bullet)

        for out_window_bullet in out_window_bullets:
            self.hero_plane.bullet_list.remove(out_window_bullet)



    def draw_enemy_plane(self):
        # 敌机图
        for enemy_plane in self.enemy_planes:
            if enemy_plane.y >= WINDOW_H:
                enemy_plane.reset()
            elif enemy_plane.is_hited:
                enemy_plane.plane_down()

            self.window.blit(enemy_plane.img, (enemy_plane.x, enemy_plane.y))



    def draw_game_text(self,content, font_size, x, y):
        # 贴得分
        # 设置文本 返回文本对象   render(文本内容， 抗锯齿， 颜色)
        # 加载自定义字体，返回字体对象
        # 设置文本的位置和尺寸
        # font = pygame.font.SysFont('SimHei', font_size)
        font = pygame.font.Font("res/SIMHEI.TTF", font_size)
        text_obj = font.render(content, 1, (255, 255, 255))
        text_rect = text_obj.get_rect(x=x, y=y)
        self.window.blit(text_obj, text_rect)



    def draw(self):
        self.draw_map()
        self.draw_hero_plane()
        self.draw_bullet()
        self.draw_enemy_plane()
        self.draw_game_text("SCORE:%d" % self.score, 35, 30, 30)



    def update(self):
        pygame.display.update()


    def event(self): #事件检测
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.hero_plane.fire()

        presses_keys = pygame.key.get_pressed()

        # 个人觉得战机不应该上下移动，也不应该超出左右地图的边界
        # if presses_keys[pygame.K_UP]:
        #     self.hero_plane.move_up()

        # if presses_keys[pygame.K_DOWN]:
        #     self.hero_plane.move_down()


        if presses_keys[pygame.K_LEFT]:
            if self.hero_plane.x > -16 and self.hero_plane.x < 411:
                self.hero_plane.move_left()

        if presses_keys[pygame.K_RIGHT]:
            if self.hero_plane.x > -16 and self.hero_plane.x < 411:
                self.hero_plane.move_right()

        print self.hero_plane.x


    def action(self): #主动动作
        # 子弹移动
        for bullet in self.hero_plane.bullet_list:
            bullet.move()

        # 敌机移动
        for enemy_plane in self.enemy_planes:
            enemy_plane.move()

        # 地图移动
        self.map.move()



    def is_hited(self, rect1, rect2):
        # 判断两个矩形是否相交，相交返回True，否则返回False
        return pygame.Rect.colliderect(rect1, rect2)



    def wait_game_input(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif event.key == pygame.K_RETURN:
                        if self.is_over:
                            self.gameover_sound.stop()    # 停止游戏结束音效，重新开始游戏
                            self.__init__()
                        return



    def game_start(self):
        self.draw_map()
        self.draw_game_text("PLANE WAR", 40, WINDOW_W / 2 - 100, WINDOW_H / 3)
        self.draw_game_text("Enter --> start & Esc --> quit.", 28, WINDOW_W / 3 - 140, WINDOW_H / 2)
        self.update()
        self.wait_game_input()



    def game_over(self):
        # 先停止播放背景音乐
        pygame.mixer.music.stop()
        # 再播放音效
        self.gameover_sound.play()
        # 贴背景图片
        self.draw_map()
        self.draw_game_text(" U are Hited, score:%d" % self.score, 28, WINDOW_W / 3 - 100, WINDOW_H / 3)
        self.draw_game_text("Enter --> start & Esc --> quit.", 28, WINDOW_W / 3 - 140, WINDOW_H / 2)
        self.update()
        self.wait_game_input()



    def run(self):
        self.game_start()
        while True:

            self.draw()

            self.update()

            self.event()

            self.action()

            time.sleep(0.02)

            if self.is_over:
                self.game_over()





def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()

