import pygame
import settings

class Harpoon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.start_y = y + settings.PLAYER_HEIGHT
        self.end_y = y

        self.image = pygame.Surface((settings.HARPOON_WIDTH, self.start_y - self.end_y))
        self.image.fill(settings.WHITE)
        self.rect = self.image.get_rect()
        self.rect.midtop = (self.x, self.end_y)
        self.speed = settings.HARPOON_SPEED

    def update(self):
        self.end_y = self.end_y - self.speed
        self.image = pygame.Surface((settings.HARPOON_WIDTH, self.start_y - self.end_y))
        self.image.fill(settings.WHITE)
        self.rect = self.image.get_rect()
        self.rect.midtop = (self.x, self.end_y)
        # kill if it moves off the top of the screen
        if self.end_y < 0:
            self.kill()
