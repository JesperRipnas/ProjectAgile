import pygame
import math
import os


# Path to users asset folder
assetpath = os.path.dirname(os.path.abspath(__file__)) + '\\Assets\\'


# Init mixer
pygame.mixer.init(frequency = 44100, size = -16, channels = 3, buffer = 2**12)


# Seperate channels
channel_1 = pygame.mixer.Channel(0)
channel_2 = pygame.mixer.Channel(1)
channel_3 = pygame.mixer.Channel(2)
channel_4 = pygame.mixer.Channel(3)


# Background music
bgsound = pygame.mixer.Sound(assetpath + 'backgroundsong.mp3')
channel_1.play(bgsound, loops = -1)
channel_1.set_volume(0.5)


# Button press sound
def sound_buttonpress():
    sound = pygame.mixer.Sound(assetpath + 'buttonpress.mp3')
    channel_2.play(sound, loops = 0)
    channel_2.set_volume(1)


# Play warning sounds if hunger gets to low
def sound_alarm():
    sound = pygame.mixer.Sound(assetpath + 'alarm.mp3')
    channel_3.play(sound, loops = 0)
    channel_3.set_volume(1)


# Play warning sounds if hunger gets to low
def sound_warning():
    sound = pygame.mixer.Sound(assetpath + 'warning_eating.wav')
    channel_3.play(sound, loops = 0)
    channel_3.set_volume(1)


# Eating sound
def sound_eating():
    sound = pygame.mixer.Sound(assetpath + 'eating.wav')
    channel_4.play(sound, loops = 0)
    channel_4.set_volume(1)

# Sleeping sound
def sound_sleeping():
    sound = pygame.mixer.Sound(assetpath + 'snoring.wav')
    channel_4.play(sound, loops = 0)
    channel_4.set_volume(1)