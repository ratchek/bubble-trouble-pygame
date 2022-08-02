# Pygame template - skeleton for a new pygame project
import pygame
from settings import *
from player import Player
from bubble import Bubble
from levels import LEVELS, NO_OF_LEVELS
from screen import *

class Game:
    def __init__(self):
        # initialize game window, mixer, clock, etc
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
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
        self.current_level = 0
        self.load_level(self.current_level)

        self.run()

    def load_level(self, level):
        for b in LEVELS[level]["bubbles"]:
            print(b)
            bubble = Bubble(**b)
            self.bubbles.add(bubble)
            self.all_sprites.add(bubble)
        player_x_coords  = LEVELS[level]["player"]["x"]
        player_y_coords  = LEVELS[level]["player"]["y"]
        self.player.rect.midbottom = (player_x_coords, player_y_coords)
        show_level_screen(game, level)
 
    def run(self):
        # game loop
        # self.playing controls the current game (until you die or quit).
        # self.running controls the game window (until you hit ESCAPE or click "x")
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
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
        self.screen.fill(BG_COLOR)
        self.all_sprites.draw(self.screen)
        # after drawing everything, flip the display
        pygame.display.flip()

    def update(self):
        # all the updates
        hits = pygame.sprite.groupcollide(self.bubbles, self.harpoons, True, True)
        if hits:
            for bubble in hits:
                if bubble.stage > 0:
                    bubble_one = Bubble(bubble.rect.x, bubble.rect.y, bubble.stage - 1, bubble.color, bubble.speed_x, BUBBLE_HARPOON_SPEED_BOOST)
                    bubble_two = Bubble(bubble.rect.x, bubble.rect.y, bubble.stage - 1, bubble.color, bubble.speed_x * -1, BUBBLE_HARPOON_SPEED_BOOST)
                    self.all_sprites.add(bubble_one, bubble_two)
                    self.bubbles.add(bubble_one, bubble_two)
        # If you killed all the bubbles
        if not self.bubbles:
            pygame.time.wait(int(AFTER_LVL_CLEARED_PAUSE * 1000))
            self.current_level += 1
            if self.current_level >= NO_OF_LEVELS:
                self.winner()
            else:
                self.load_level(self.current_level)

        hits = pygame.sprite.spritecollide(self.player, self.bubbles, False)
        if hits:
            self.game_over()

        # I want update to happen at the end so that the "hit" is drawn before the game freezes
        # Otherwise it'll look like you died before you actually got hit.
        self.all_sprites.update()
    
    def game_over(self):
        self.died_animation()
        # cleanup
        for sprite in self.all_sprites:
            sprite.kill()
        self.playing = False

    def died_animation(self):
        pygame.time.wait(int(AFTER_DEATH_PAUSE * 1000))
        show_go_screen(game)
    
    def winner(self):
        show_winner_screen(game)
        for sprite in self.all_sprites:
            sprite.kill()
        self.playing = False
        

game = Game()
show_start_screen(game)
while game.running:
    game.new()

pygame.quit()


