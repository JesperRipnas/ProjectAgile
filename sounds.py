import pygame
import math
import os

# Path to users asset folder
assetpath = os.path.dirname(os.path.abspath(__file__)) + '\\Assets\\'


# Init mixer
pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)


# Seperate channels
channel_1 = pygame.mixer.Channel(0)
channel_2 = pygame.mixer.Channel(1)


# Background music
bgsound = pygame.mixer.Sound(assetpath + 'backgroundsong.mp3')
channel_1.play(bgsound, loops = -1)
channel_1.set_volume(0.5)


# Button press sound
def buttonpress():
    sound = pygame.mixer.Sound(assetpath + 'buttonpress.mp3')
    channel_2.play(sound, loops = 0)
    channel_2.set_volume(1)