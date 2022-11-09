import pygame
from settings import *
from audio import sounds
from spritesheet import Spritesheet

class Harpoon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.start_y = y + PLAYER_HEIGHT
        self.end_y = y

        self.sprite_sheet = Spritesheet()
        self.image = self.sprite_sheet.get_harpoon_image(self.start_y - self.end_y) 

        self.rect = self.image.get_rect()
        self.rect.midtop = (self.x, self.end_y)
        self.speed = HARPOON_SPEED
        # Each harpoon sound gets their own channel so that
        # you can kill each one individually
        self.sound_channel = pygame.mixer.find_channel()
        self.sound_channel.play(sounds["shoot_fire"] )

    def update(self):
        self.end_y = self.end_y - self.speed
        self.image = self.sprite_sheet.get_harpoon_image(self.start_y - self.end_y) 
        self.rect = self.image.get_rect()
        self.rect.midtop = (self.x, self.end_y)
        self.mask = pygame.mask.from_surface(self.image)
        # kill if it moves off the top of the screen
        if self.end_y < 0:
            self.kill()

    def kill(self):
        if self.sound_channel:
            self.sound_channel.stop()
        super().kill()
