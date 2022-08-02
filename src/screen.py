import pygame
from settings import *

def show_start_screen(game):
    # game splash/start screen
    game.screen.fill(BG_COLOR)
    draw_text(game, TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
    draw_text(game, "Arrows to move, Space to fire harpoon", 22, WHITE, WIDTH / 2, HEIGHT / 2)
    draw_text(game, "Press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    wait_for_key(game)

def show_go_screen(game):
    # game over/continue
    if not game.running:
        return
    game.screen.fill(BG_COLOR)
    draw_text(game, "GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
    draw_text(game, "Score: " + "???" ,  22, WHITE, WIDTH / 2, HEIGHT / 2)
    draw_text(game, "Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    wait_for_key(game)

def show_level_screen(game, level):
    game.screen.fill(BG_COLOR)
    draw_text(game, "LEVEL " + str(level + 1), 48, WHITE, WIDTH / 2, HEIGHT / 4)
    pygame.display.flip()
    pygame.time.wait(int(LEVEL_SCREEN_PAUSE * 1000))

def show_winner_screen(game):
    game.screen.fill(BG_COLOR)
    draw_text(game, "CONGRATULATIONS!" , 48, WHITE, WIDTH / 2, HEIGHT / 4)
    draw_text(game, "You won!!!" ,  22, WHITE, WIDTH / 2, HEIGHT / 2)
    draw_text(game, "Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    wait_for_key(game)
    

def wait_for_key(game):
    waiting = True
    while waiting:
        game.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                    game.playing = False
                    game.running = False
                else: 
                    waiting = False

def draw_text(game, text, size, color, x, y):
    font = pygame.font.Font(FONT, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    game.screen.blit(text_surface, text_rect)
