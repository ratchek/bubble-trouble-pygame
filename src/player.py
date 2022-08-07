from settings import *
import pygame
from harpoon import Harpoon
from spritesheet import Spritesheet
import itertools 
from settings import TIME_PER_CHARACTER_ANIMATION_FRAME

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        sprite_sheet = Spritesheet()
        self.idle_image = sprite_sheet.get_image("idle", PLAYER_HEIGHT)
        self.image = self.idle_image
        self.rect = self.image.get_rect()
        self.rect.midbottom =  (WIDTH/2, GAME_FLOOR)
        self.speedx = 0
        self.max_harpoons = 1
        self.lives = NO_OF_LIVES_AT_BEGINNING
        self.animation_frames = [ sprite_sheet.get_image("walk_{}".format(i), PLAYER_HEIGHT) for i in range(1,5)]
        self.animation_iterator = itertools.cycle(self.animation_frames)
        self.walking = False
        self.last_update = 0

    def shoot(self):
        harpoon = Harpoon(self.rect.centerx, self.rect.top)
        return harpoon

    def update(self):
        self.speedx = 0
        # get input and calculate move
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx -= PLAYER_SPEED
        if keystate[pygame.K_RIGHT]:
            self.speedx += PLAYER_SPEED
       
        if self.speedx != 0:
            frame = self.get_animation_frame()
            if frame:
                self.image = frame
        else:
            self.image = self.idle_image

        # move
        self.rect.x += self.speedx
        # be careful about walls
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        # update collision mask
        self.mask = pygame.mask.from_surface(self.image)

    def get_animation_frame(self):
        if pygame.time.get_ticks() > self.last_update + TIME_PER_CHARACTER_ANIMATION_FRAME:
            self.last_update = pygame.time.get_ticks()
            next_frame = next(self.animation_iterator)
            if self.speedx < 0:
                next_frame = pygame.transform.flip(next_frame, True, False,)
            return next_frame 
        else:
            return None

