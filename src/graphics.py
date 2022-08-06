import pygame
from settings import *
from sprites import Spritesheet
class Graphics:
    sprite_sheet = None
    @staticmethod
    def show_start_screen(game):
        # game splash/start screen
        game.screen.fill(BG_COLOR)
        Graphics.draw_text(game, TITLE, 48, WHITE, WIDTH / 2, GAME_FLOOR / 4)
        Graphics.draw_text(game, TITLE_SCREEN_INSTRUCTIONS, 22, WHITE, WIDTH / 2, GAME_FLOOR / 2)
        Graphics.draw_text(game, "Press a key to play", 22, WHITE, WIDTH / 2, GAME_FLOOR * 3 / 4)
        pygame.display.flip()
        Graphics.wait_for_key(game)

    @staticmethod
    def show_go_screen(game):
        # game over/continue
        if not game.running:
            return
        game.screen.fill(BG_COLOR)
        Graphics.draw_text(game, "GAME OVER", 48, WHITE, WIDTH / 2, GAME_FLOOR / 4)
        Graphics.draw_text(game, "Score: {}".format(game.score) ,  22, WHITE, WIDTH / 2, GAME_FLOOR / 2)
        Graphics.draw_text(game, "Press a key to play again", 22, WHITE, WIDTH / 2, GAME_FLOOR * 3 / 4)
        pygame.display.flip()
        Graphics.wait_for_key(game)

    @staticmethod
    def show_level_screen(game, level):
        game.screen.fill(BG_COLOR)
        Graphics.draw_text(game, "LEVEL " + str(level + 1), 48, WHITE, WIDTH / 2, GAME_FLOOR / 4)
        pygame.display.flip()
        pygame.time.wait(int(LEVEL_SCREEN_PAUSE * 1000))

    @staticmethod
    def show_winner_screen(game):
        game.screen.fill(BG_COLOR)
        Graphics.draw_text(game, "CONGRATULATIONS!" , 48, WHITE, WIDTH / 2, GAME_FLOOR / 4)
        Graphics.draw_text(game, "You won!!!" ,  22, WHITE, WIDTH / 2, GAME_FLOOR / 2)
        Graphics.draw_text(game, "Your score was: {}".format(game.score) ,  22, WHITE, WIDTH / 2, GAME_FLOOR / 2 + 40)
        Graphics.draw_text(game, "Press a key to play again", 22, WHITE, WIDTH / 2, GAME_FLOOR * 3 / 4)
        pygame.display.flip()
        Graphics.wait_for_key(game)
        

    @staticmethod
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

    @staticmethod
    def draw_text(game, text, size, color, x, y):
        font = pygame.font.Font(FONT, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        game.screen.blit(text_surface, text_rect)

    @staticmethod
    def draw_lives(game):
        for i in range(game.player.lives):
            # life_icon = pygame.Surface((LIFE_ICON_WIDTH, LIFE_ICON_HEIGHT))
            # life_icon.fill(RED)
            if Graphics.sprite_sheet is None:
                Graphics.sprite_sheet = Spritesheet()
            life_icon = Graphics.sprite_sheet.get_image("elife", LIFE_ICON_HEIGHT)
            rect = life_icon.get_rect()
            x = FIRST_LIFE_ICON_X_POSITION + (LIFE_ICON_WIDTH + LIFE_ICON_PADDING) * i
            y = FIRST_LIFE_ICON_Y_POSITION
            rect.topleft = (x,y)
            game.screen.blit(life_icon, rect)

    @staticmethod
    def draw_console(game):
        y = HEIGHT - CONSOLE_HEIGHT
        pygame.draw.line(game.screen, CONSOLE_BORDER_LINE_COLOR, (0,y), (WIDTH,y), CONSOLE_BORDER_LINE_WIDTH)
        Graphics.draw_timer(game)


    @staticmethod
    def draw_timer(game):
        top = HEIGHT - TIMER_HEIGHT
        total_level_time = game.level_end_time - game.level_start_time
        current_level_time = game.level_end_time - pygame.time.get_ticks()
        fill_ratio =  current_level_time/total_level_time
        width = WIDTH * fill_ratio
        left = WIDTH - width
        time_left_rect = pygame.Rect(left, top, width, TIMER_HEIGHT) 
        pygame.draw.rect(game.screen, TIMER_COLOR, time_left_rect) 
        
