import pygame

bullet_rect = pygame.Rect(100, 50, 20, 31)
enemy_rect = pygame.Rect(100, 80, 100, 68)

print bullet_rect

print enemy_rect

def is_hited(rect1, rect2):
    res = pygame.Rect.colliderect(rect1, rect2)
    return res

res = is_hited(bullet_rect, enemy_rect)
print res


ziti = pygame.font.get_fonts()

for i in ziti:
    print i