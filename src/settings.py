import pygame

WIDTH = 720
HEIGHT = 480
FPS = 60
TITLE = "Bubble Trouble in pygame"
#TITLE = "A GAME"
#TITLE_SCREEN_INSTRUCTIONS = "Figure it out"
TITLE_SCREEN_INSTRUCTIONS ="Arrows to move, Space to fire harpoon"

AUDIO_PATH = "../audio/"
AUDIO_EXTENSION = ".ogg"
SOUND_NAMES = ["shoot_harpoon","bubble_pop", "bubble_pop2", "bubble_split", "ingame_start_level", "ingame_dead", "ingame_time_out", "level_won", "game_won", ]

IMAGE_PATH = "../img/"
# The extension is added in the program because the same name
# is used for both the image and the json
SPRITE_SHEET_FILE_NAME = "sprite_sheet"
SPRITES_USED = [
    "shots/single_spiral.png",
    "bubbles/bubble_blue.png",
    "bubbles/bubble_blue_pop.png",
    "bubbles/bubble_green.png",
    "bubbles/bubble_green_pop.png",
    "bubbles/bubble_red.png",
    "bubbles/bubble_red_pop.png",
    "bubbles/bubble_orange.png",
    "bubbles/bubble_orange_pop.png",
    "bubbles/bubble_purple.png",
    "bubbles/bubble_purple_pop.png",
    "bubbles/bubble_yellow.png",
    "bubbles/bubble_yellow_pop.png",
    "bubbles/bubble_pop.png",
    "bubbles/pop_bubble_1.png",
    "bubbles/pop_bubble_2.png",
    "bubbles/pop_bubble_3.png",
    "char/idle.png",
    "char/walk_1.png",
    "char/walk_2.png",
    "char/walk_3.png",
    "char/walk_4.png",
    "char/mouse_contour.png",
    "items/elife.png"
    ]

# define colors. Used for development
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (173,216,230)
YELLOW = (238,238, 238)
BG_COLOR = BLACK
CONSOLE_HEIGHT = 40
CONSOLE_BORDER_LINE_WIDTH = 5
CONSOLE_BORDER_LINE_COLOR = RED

TIMER_HEIGHT =CONSOLE_HEIGHT
TIMER_WIDTH = WIDTH
TIMER_COLOR = RED

# This is where the bottom of the actual game is
GAME_FLOOR = HEIGHT - CONSOLE_HEIGHT

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 40
PLAYER_SPEED = 3
NO_OF_LIVES_AT_BEGINNING = 3
LIFE_ICON_WIDTH = 10
LIFE_ICON_HEIGHT = 20
LIFE_ICON_PADDING = 5
FIRST_LIFE_ICON_X_POSITION = 20
FIRST_LIFE_ICON_Y_POSITION = 20


HARPOON_WIDTH = 5
HARPOON_SPEED = 10

BUBBLE_SIZES = [10, 20, 30, 40]
BUBBLE_MAX_SPEEDS = [5, 6, 7, 8, 10,]
BUBBLE_GRAVITY = 0.2
BUBBLE_HORIZONTAL_SPEED = 1
# When a bubble gets hit by a harpoon, it's "children"
# are "pushed" up by it a little. As if the harpoon
# had mass. This is a quick workaround.
BUBBLE_HARPOON_SPEED_BOOST = -4




FONT_NAME = "arial" 
# If font doesn't exist on system, use closest matching font that exists
FONT = pygame.font.match_font(FONT_NAME)
# How long to wait between levels. In seconds
LEVEL_SCREEN_PAUSE = 1
# How long to wait after death. In seconds
AFTER_DEATH_PAUSE = 1
# How long to wait after level cleared. In seconds
AFTER_LVL_CLEARED_PAUSE = 2 
