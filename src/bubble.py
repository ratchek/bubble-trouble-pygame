import pygame
from settings import *

class Bubble (pygame.sprite.Sprite):
    # level 0 bubbles are the smallest. 
    def __init__(self, x, y, level, color, speed_x, speed_y):
        super().__init__()
        self.level = level
        self.image = pygame.Surface((BUBBLE_SIZES[level], BUBBLE_SIZES[level]))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.gravity = BUBBLE_GRAVITY
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.bottom >= HEIGHT:
            self.speed_y *= -1
        elif self.speed_y <= BUBBLE_MAX_SPEEDS[self.level]:
            self.speed_y += self.gravity
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1
