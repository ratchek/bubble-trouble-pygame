from  settings import *
from os import path


pygame.mixer.init()
audio_dir = path.join(path.dirname(__file__), AUDIO_PATH)
sounds = {name: pygame.mixer.Sound(path.join(audio_dir, name + AUDIO_EXTENSION)) for name in SOUND_NAMES}
bubble_pop_sounds = [sounds["bubble_pop2"], sounds["bubble_pop"]]
