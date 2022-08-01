import pygame
import settings

class Bubble (pygame.sprite.Sprite):
    # level 0 bubbles are the smallest. 
    def __init__(self, x, y, level, color, speed_x, speed_y):
        super().__init__()
        self.level = level
        self.image = pygame.Surface((settings.BUBBLE_SIZES[level], settings.BUBBLE_SIZES[level]))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.gravity = settings.BUBBLE_GRAVITY
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.bottom >= settings.HEIGHT:
            self.speed_y *= -1
        elif self.speed_y <= settings.BUBBLE_MAX_SPEEDS[self.level]:
            self.speed_y += self.gravity
        if self.rect.left <= 0 or self.rect.right >= settings.WIDTH:
            self.speed_x *= -1
