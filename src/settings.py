import pygame

WIDTH = 720
HEIGHT = 480
FPS = 60
TITLE = "Bubble Trouble in pygame"
#TITLE = "A GAME"
#TITLE_SCREEN_INSTRUCTIONS = "Figure it out"
TITLE_SCREEN_INSTRUCTIONS ="Arrows to move, Space to fire harpoon"

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

# define colors. Used for development
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (173,216,230)
YELLOW = (238,238, 238)
BG_COLOR = BLACK



FONT_NAME = "arial" 
# If font doesn't exist on system, use closest matching font that exists
FONT = pygame.font.match_font(FONT_NAME)
# How long to wait between levels. In seconds
LEVEL_SCREEN_PAUSE = 1
# How long to wait after death. In seconds
AFTER_DEATH_PAUSE = 1
# How long to wait after level cleared. In seconds
AFTER_LVL_CLEARED_PAUSE = 0.5
