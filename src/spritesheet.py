from settings import *
import pygame
from os import path
import json

class Spritesheet:
    sprite_coords = None
    sprite_sheet = None

    def __init__(self):
        if Spritesheet.sprite_coords is None:
            img_dir = path.join(path.dirname(__file__), IMAGE_PATH)
            sprite_sheet_image_path= path.join(img_dir, SPRITE_SHEET_FILE_NAME + ".png")
            Spritesheet.sprite_sheet = pygame.image.load(sprite_sheet_image_path).convert()
            sprite_sheet_data_path= path.join(img_dir, SPRITE_SHEET_FILE_NAME + ".json")
            with open (sprite_sheet_data_path) as file:
                sprite_data = json.load(file)
            sprite_data = sprite_data["textures"][0]["frames"]
            Spritesheet.sprite_coords = {}
            for sprite in sprite_data:
                if sprite["f"] in SPRITES_USED:
                    # Since we're not using all that many sprites, we'll extract and use just the
                    # name. Without the grouping structure that's in place
                    name = sprite["f"].split("/")[-1].split(".")[0] 
                    Spritesheet.sprite_coords[name] = (sprite["x"], sprite["y"], sprite["w"], sprite["h"],) 

    def get_image(self, sprite_name, desired_height):
        # grab an image out of a larger spritesheet
        x, y, width, height = Spritesheet.sprite_coords[sprite_name] 
        image = pygame.Surface((width, height))
        image.set_colorkey(BLACK)
        image.blit(Spritesheet.sprite_sheet, (0, 0), (x, y, width, height))
        # scale to desired height, keeping aspect ratio
        new_width = width * desired_height / height
        scaled_image = pygame.transform.scale(image, (new_width, desired_height))
        return scaled_image

    def get_harpoon_image(self, height):
        # This is a bit different, because when we increase height,
        # we don't want to increase width
        x, y, width, full_height = Spritesheet.sprite_coords["single_spiral"]
        image = pygame.Surface((width, height))
        image.set_colorkey(BLACK)
        image.blit(Spritesheet.sprite_sheet, (0, 0), (x, y, width, height))
        # scale to desired height, keeping aspect ratio
        return image

        
