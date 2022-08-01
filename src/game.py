# Pygame template - skeleton for a new pygame project
import pygame
import random
import settings
from player import Player

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(settings.FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    # Update
    all_sprites.update()
    # Draw / render
    screen.fill(settings.BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
