import settings
import pygame
from harpoon import Harpoon

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT))
        self.image.fill(settings.RED)
        self.rect = self.image.get_rect()
        self.rect.midbottom =  (settings.WIDTH/2, settings.HEIGHT)
        self.speedx = 0
        self.max_harpoons = 1
    def shoot(self):
        harpoon = Harpoon(self.rect.centerx, self.rect.top)
        return harpoon

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx -= settings.PLAYER_SPEED
        if keystate[pygame.K_RIGHT]:
            self.speedx += settings.PLAYER_SPEED
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > settings.WIDTH:
            self.rect.right = settings.WIDTH

