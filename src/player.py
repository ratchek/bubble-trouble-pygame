from settings import *
import pygame
from harpoon import Harpoon

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.midbottom =  (WIDTH/2, HEIGHT)
        self.speedx = 0
        self.max_harpoons = 1
        self.lives = NO_OF_LIVES_AT_BEGINNING
    def shoot(self):
        harpoon = Harpoon(self.rect.centerx, self.rect.top)
        return harpoon

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx -= PLAYER_SPEED
        if keystate[pygame.K_RIGHT]:
            self.speedx += PLAYER_SPEED
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

