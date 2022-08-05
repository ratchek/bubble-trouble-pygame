# pygame template - skeleton for a new pygame project
import sys
import pygame
from settings import *
from player import Player
from bubble import Bubble
from levels import LEVELS, NO_OF_LEVELS
from graphics import Graphics

class Game:
    def __init__(self):
        # initialize game window, mixer, clock, etc
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True 

    def new(self, level= 0):
        # start new game
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        # load level (move this into seperate function)
        # reposition player
        self.harpoons = pygame.sprite.Group()
        self.bubbles = pygame.sprite.Group()
        self.life_icons = pygame.sprite.Group()
        self.current_level = level
        self.load_level(self.current_level)
        self.score = 0

        self.run()

    def load_level(self, level):
        # Need to turn off the ability to fire harpoons while level screen is showing
        temp = self.player.max_harpoons
        self.player.max_harpoons = 0
        Graphics.show_level_screen(game, level)
        self.player.max_harpoons = temp
        # Make sure any moves made "during" loading screen aren't lurking in
        # the event queue
        pygame.event.clear()
        for b in LEVELS[level]["bubbles"]:
            bubble = Bubble(**b)
            self.bubbles.add(bubble)
            self.all_sprites.add(bubble)
        player_x_coords  = LEVELS[level]["player"]["x"]
        player_y_coords  = LEVELS[level]["player"]["y"]
        self.player.rect.midbottom = (player_x_coords, player_y_coords)
        self.level_start_time = pygame.time.get_ticks()
        temp_time = 10
        self.level_end_time = self.level_start_time + (temp_time * 1000)
 
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
        Graphics.draw_console(game)
        Graphics.draw_lives(game)
        # after drawing everything, flip the display
        pygame.display.flip()

    def update(self):
        # all the updates
        hits = pygame.sprite.groupcollide(self.bubbles, self.harpoons, True, True)
        if hits:
            for bubble in hits:
                self.score += 10
                if bubble.stage > 0:
                    bubble_one = Bubble(bubble.rect.x, bubble.rect.y, bubble.stage - 1, bubble.color, bubble.speed_x, BUBBLE_HARPOON_SPEED_BOOST)
                    bubble_two = Bubble(bubble.rect.x, bubble.rect.y, bubble.stage - 1, bubble.color, bubble.speed_x * -1, BUBBLE_HARPOON_SPEED_BOOST)
                    self.all_sprites.add(bubble_one, bubble_two)
                    self.bubbles.add(bubble_one, bubble_two)
        # If you killed all the bubbles
        if not self.bubbles:
            self.score += 100
            pygame.time.wait(int(AFTER_LVL_CLEARED_PAUSE * 1000))
            time_bonus = (self.level_end_time - pygame.time.get_ticks()) / 1000
            self.score += int(time_bonus)
            print("Added {} to score".format(int(time_bonus)))
            self.current_level += 1
            if self.current_level >= NO_OF_LEVELS:
                self.winner()
            else:
                self.load_level(self.current_level)

        # did time run out?
        end_of_time = pygame.time.get_ticks() >= self.level_end_time 
        hits = pygame.sprite.spritecollide(self.player, self.bubbles, False)
        if hits or end_of_time:
            self.player.lives -= 1
            if self.player.lives <= 0:
                self.game_over()
            else:
                self.lost_life()

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
        Graphics.show_go_screen(game)
    
    def winner(self):
        Graphics.show_winner_screen(game)
        for sprite in self.all_sprites:
            sprite.kill()
        self.playing = False

    def lost_life(self):
        pygame.time.wait(int(AFTER_DEATH_PAUSE * 1000))
        for bubble in self.bubbles:
            bubble.kill()
        for harpoon in self.harpoons:
            harpoon.kill()
        self.load_level(self.current_level)

game = Game()
level = 0
if len(sys.argv)==2: # first entry in sys.argv is script itself...
     level = int(sys.argv[1])

Graphics.show_start_screen(game)
while game.running:
    game.new(level)

pygame.quit()


