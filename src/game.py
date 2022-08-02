# Pygame template - skeleton for a new pygame project
import pygame
import settings
from player import Player
from bubble import Bubble

class Game:
    def __init__(self):
        # initialize game window, mixer, clock, etc
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True 

    def new(self):
        # start new game
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        # load level (move this into seperate function)
        # reposition player
        self.harpoons = pygame.sprite.Group()
        self.bubbles = pygame.sprite.Group()
        bubble0 = Bubble(settings.WIDTH/5, 60, 0, settings.BLUE, settings.BUBBLE_HORIZONTAL_SPEED, 0)
        self.all_sprites.add(bubble0)
        self.bubbles.add(bubble0)
        bubble1 = Bubble(2*settings.WIDTH/5, 60, 1, settings.BLUE, settings.BUBBLE_HORIZONTAL_SPEED, 0)
        self.all_sprites.add(bubble1)
        self.bubbles.add(bubble1)
        bubble2 = Bubble(3*settings.WIDTH/5, 60, 2, settings.BLUE, settings.BUBBLE_HORIZONTAL_SPEED, 0)
        self.all_sprites.add(bubble2)
        self.bubbles.add(bubble2)
        bubble3 = Bubble(4*settings.WIDTH/5, 60, 3, settings.BLUE, settings.BUBBLE_HORIZONTAL_SPEED, 0)
        self.all_sprites.add(bubble3)
        self.bubbles.add(bubble3)
        
        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(settings.FPS)
            self.events()
            self.draw()
            self.update()

    def events(self):
        # handle events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.playing = False
                if event.key == pygame.K_SPACE and len(self.harpoons) < self.player.max_harpoons:
                    harpoon = self.player.shoot() 
                    self.harpoons.add(harpoon)
                    self.all_sprites.add(harpoon)
    

    def draw(self):
        # draw stuff
        self.screen.fill(settings.BLACK)
        self.all_sprites.draw(self.screen)
        # after drawing everything, flip the display
        pygame.display.flip()

    def update(self):
        # all the updates
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.player, self.bubbles, False)
        if hits:
            while self.running:
                # Pause screen after hit 
                for event in pygame.event.get():
                    # check for closing window
                    if event.type == pygame.QUIT:
                        self.playing = False
                        self.running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.playing = False
                            self.running = False
        hits = pygame.sprite.groupcollide(self.bubbles, self.harpoons, True, True)
        if hits:
            for bubble in hits:
                if bubble.level > 0:
                    bubble_one = Bubble(bubble.rect.x, bubble.rect.y, bubble.level - 1, bubble.color, bubble.speed_x, settings.BUBBLE_HARPOON_SPEED_BOOST)
                    bubble_two = Bubble(bubble.rect.x, bubble.rect.y, bubble.level - 1, bubble.color, bubble.speed_x * -1, settings.BUBBLE_HARPOON_SPEED_BOOST)
                    self.all_sprites.add(bubble_one, bubble_two)
                    self.bubbles.add(bubble_one, bubble_two)

game = Game()
while game.running:
    game.new()

pygame.quit()


