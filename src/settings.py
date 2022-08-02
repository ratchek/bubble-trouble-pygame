import pygame

WIDTH = 720
HEIGHT = 480
FPS = 60
TITLE = "Bubble Trouble"

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 40
PLAYER_SPEED = 3

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
BLUE = (0, 0, 255)
BG_COLOR = BLACK


FONT_NAME = "arial" 
# If font doesn't exist on system, use closest matching font that exists
FONT = pygame.font.match_font(FONT_NAME)
# How long to wait between levels. In seconds
LEVEL_SCREEN_PAUSE = 1
# How long to wait between levels. In seconds
AFTER_DEATH_PAUSE = 1
