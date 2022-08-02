# Pygame template - skeleton for a new pygame project
import pygame
import settings
from player import Player
from bubble import Bubble

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
harpoons = pygame.sprite.Group()
bubbles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

bubble0 = Bubble(settings.WIDTH/5, 60, 0, settings.BLUE, settings.BUBBLE_HORIZONTAL_SPEED, 0)
all_sprites.add(bubble0)
bubbles.add(bubble0)
bubble1 = Bubble(2*settings.WIDTH/5, 60, 1, settings.BLUE, settings.BUBBLE_HORIZONTAL_SPEED, 0)
all_sprites.add(bubble1)
bubbles.add(bubble1)
bubble2 = Bubble(3*settings.WIDTH/5, 60, 2, settings.BLUE, settings.BUBBLE_HORIZONTAL_SPEED, 0)
all_sprites.add(bubble2)
bubbles.add(bubble2)
bubble3 = Bubble(4*settings.WIDTH/5, 60, 3, settings.BLUE, settings.BUBBLE_HORIZONTAL_SPEED, 0)
all_sprites.add(bubble3)
bubbles.add(bubble3)

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE and len(harpoons) < player.max_harpoons:
                harpoon = player.shoot() 
                harpoons.add(harpoon)
                all_sprites.add(harpoon)
    # Update
    all_sprites.update()
    # Draw / render
    screen.fill(settings.BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()
    
    # Check if player got hit
    hits = pygame.sprite.spritecollide(player, bubbles, False)
    if hits:
        #running = False
        while running:
            # Pause screen after hit 
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
    hits = pygame.sprite.groupcollide(bubbles, harpoons, True, True)
    if hits:
        for bubble in hits:
            if bubble.level > 0:
                bubble_one = Bubble(bubble.rect.x, bubble.rect.y, bubble.level - 1, bubble.color, bubble.speed_x, settings.BUBBLE_HARPOON_SPEED_BOOST)
                bubble_two = Bubble(bubble.rect.x, bubble.rect.y, bubble.level - 1, bubble.color, bubble.speed_x * -1, settings.BUBBLE_HARPOON_SPEED_BOOST)
                all_sprites.add(bubble_one, bubble_two)
                bubbles.add(bubble_one, bubble_two)

pygame.quit()
