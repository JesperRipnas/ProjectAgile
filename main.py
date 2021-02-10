import pygame
import math
import os
from tamagotchi import * 
from animation import Animation
from sounds import *


def button(circlecenter):
    x1, y1 = pygame.mouse.get_pos()
    x2, y2 = circlecenter
    distance = math.hypot(x1 - x2, y1 - y2)
    return distance


def background(path):
    screen.fill(GRAY)
    backgroundPic = pygame.image.load(path)
    backgroundPic = pygame.transform.scale(backgroundPic, (580, 745))
    printPic = backgroundPic.get_rect()
    screen.blit(backgroundPic, printPic)


def debug(debug_var_list, x ,y, fontsize):
    debug_font = pygame.font.Font(None, fontsize)
    
    debug_pos = [x,y]
    for i, line in enumerate(debug_var_list):
        screen.blit(debug_font.render(line,1, (0,0,0)), (x, y + (i * 20)))


def timepassed():
    font = pygame.font.SysFont('timesnewroman', 15)
    hunger_value_text = font.render('D: '+str(seconds_elapsed), True, (0,0,0), None) 
    screen.blit(hunger_value_text, (235, 230))

    hunger_value_text = font.render('Y: '+str(current_tamagotchi.age), True, (0,0,0), None) 
    screen.blit(hunger_value_text, (305, 230))


def food():
    if current_tamagotchi.hunger_state == True:
        hunger_icon = pygame.image.load(assetpath + 'foodselect.png')
    elif current_tamagotchi.hunger_state == False:
        hunger_icon = pygame.image.load(assetpath + 'foodfade.png')

    font = pygame.font.SysFont('timesnewroman', 15)
    hunger_value_text = font.render(str(current_tamagotchi.hunger), True, (0,0,0), None) 
    screen.blit(hunger_value_text, (195, 230))

    hunger_icon = pygame.transform.scale(hunger_icon, (20, 20))
    screen.blit(hunger_icon, (170, 230))


def sleep():
    if current_tamagotchi.energy_state == True:
        energy_icon = pygame.image.load(assetpath + 'bedselect.png')
    elif current_tamagotchi.energy_state == False:
        energy_icon = pygame.image.load(assetpath + 'bedfade.png')

    font = pygame.font.SysFont('timesnewroman', 15)
    energy_value_text = font.render(' '+str(current_tamagotchi.energy), True, (0,0,0), None)
    screen.blit(energy_value_text, (385,230))

    energy_icon = pygame.transform.scale(energy_icon, (20, 20))
    screen.blit(energy_icon, (365, 230))


def buttonA():
    current_tamagotchi.hunger_state = not current_tamagotchi.hunger_state
    current_tamagotchi.energy_state = not current_tamagotchi.energy_state
    buttonpress()


def buttonB():
    if current_tamagotchi.hunger_state:
        current_tamagotchi._eat()
    elif current_tamagotchi.energy_state:
        current_tamagotchi._sleep()
    buttonpress()


def buttonC():
    current_tamagotchi.popup_state = not current_tamagotchi.popup_state
    buttonpress()


def popup():
    popupbg = pygame.image.load(assetpath + 'popupbg.png')
    popupbg = pygame.transform.scale(popupbg, (127, 150))
    font = pygame.font.SysFont('timesnewroman', 13)
    popuptext_name = font.render('Name: '+str(current_tamagotchi.name), True, (0,0,0), None)
    popuptext_birthday = font.render('Birthday: '+str(current_tamagotchi.birthday), True, (0,0,0), None)
    popuptext_cash = font.render('Cash: $'+str(current_tamagotchi.cash), True, (0,0,0), None)
    popuptext_loan = font.render('Loan: $'+str(current_tamagotchi.loan), True, (0,0,0), None)
    popuptext_happiness = font.render('Happiness: '+str(current_tamagotchi.happiness), True, (0,0,0), None)
    popuptext_exercise = font.render('Workout: '+str(current_tamagotchi.exercise), True, (0,0,0), None)
    popuptext_drunk = font.render('Drunk: '+str(current_tamagotchi.drunk), True, (0,0,0), None)
    if current_tamagotchi.popup_state == False:
        popupbg = pygame.image.load(assetpath + 'popupbgtrans.png')
    elif current_tamagotchi.popup_state == True:
        screen.blit(popupbg, (290,252))
        screen.blit(popuptext_name, (295,260))
        screen.blit(popuptext_birthday, (296,280))
        screen.blit(popuptext_cash, (296,300))
        screen.blit(popuptext_loan, (296,320))
        screen.blit(popuptext_happiness, (296,340))
        screen.blit(popuptext_exercise, (296,360))
        screen.blit(popuptext_drunk, (296,380))

assetpath = os.path.dirname(os.path.abspath(__file__)) + '\\Assets\\'

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
LGRAY = (157, 157, 157)


# Mouse buttons
LEFT = 1
RIGHT = 3


# Width & Height of each cell
WIDTH = 6
HEIGHT = 6


# Margin between cells
MARGIN = 2

# Window Margin
WINDOWMARGINX = 160
WINDOWMARGINY = 250

seconds_elapsed = 0
show_debug = False


# Create a 2 dimensional array.
grid = []
for row in range(32):
    grid.append([])
    for column in range(32):
        grid[row].append(0)


# Initialize pygame
pygame.init()


# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = width, height = 580, 740
screen = pygame.display.set_mode(WINDOW_SIZE)


# Set title of screen
pygame.display.set_caption("Tamagotchi")


# Loop until the user clicks the close button.
done = False
game_speed = 1000
paused = False


# Used to manage how fast the screen updates
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT+1,game_speed)


# Default Object character
current_tamagotchi = Tamagotchi("Dude",19911014)


# Animtaion and timer to controll the speed
animation = Animation()
pygame.time.set_timer(pygame.USEREVENT+2,500)


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:

            if button((180, 590)) <= 25:    # Button A
                buttonA()
            if button((290, 625)) <= 25:    # Button B
                buttonB()
            if button((390, 590)) <= 25:    # Button C
                buttonC()

            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()

            if pos[0] > WINDOWMARGINX and pos[1] > WINDOWMARGINY:
                try:
                # Change the x/y screen coordinates to grid coordinates
                    column = (pos[0] - WINDOWMARGINX)// (WIDTH + MARGIN)
                    row = (pos[1] - WINDOWMARGINY)// (HEIGHT + MARGIN)
                # Set that location to one
                    grid[row][column] = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)
                except:
                    pass
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            #try:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            if pos[0] > WINDOWMARGINX and pos[1] > WINDOWMARGINY:
                try:
                # Change the x/y screen coordinates to grid coordinates
                    column = (pos[0] - WINDOWMARGINX) // (WIDTH + MARGIN)
                    row = (pos[1] - WINDOWMARGINY) // (HEIGHT + MARGIN )
                # Set that location to one
                    grid[row][column] = 0
                    print("Click ", pos, "Grid coordinates: ", row, column)
                except:
                    pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                buttonA()
            if event.key == pygame.K_2:
                buttonB()
            if event.key == pygame.K_3:
                buttonC()
            if event.key == pygame.K_d:
                show_debug = not show_debug
            if event.key == pygame.K_l:
                if game_speed - 100 <= 0:
                    game_speed = 0
                    pygame.time.set_timer(pygame.USEREVENT+1,game_speed)
                else:
                    game_speed = game_speed - 100
                    pygame.time.set_timer(pygame.USEREVENT+1,game_speed)
            if event.key == pygame.K_k:
                game_speed += 100
                pygame.time.set_timer(pygame.USEREVENT+1,game_speed)

            if event.key == pygame.K_p:
                if paused:
                    pygame.time.set_timer(pygame.USEREVENT+1,game_speed)
                    paused = not paused
                else:
                    pygame.time.set_timer(pygame.USEREVENT+1,0)
                    paused = not paused
        elif event.type==pygame.USEREVENT+1:
            seconds_elapsed += 1
            current_tamagotchi.update()
            if seconds_elapsed % 365 == 0:
                animation.play_birthday()
                current_tamagotchi.age += 1
                print("Happy bday")
            else:
                animation.play_idle()
            if current_tamagotchi.hunger < 20:
                warningsound()
        elif event.type==pygame.USEREVENT+2:
            grid = animation.play_animation()


    # Set the screen background
    background(assetpath + 'background.png')


    if show_debug:
        debug(["Day: " + str(seconds_elapsed), "Year: " + str(current_tamagotchi.age),"Hunger: " + str(current_tamagotchi.hunger), "Energy: " + str(current_tamagotchi.energy),
        "One day = " + str(game_speed) + " ms" ], 10, 10, 20)

    
    # Draw the grid
    for row in range(32):
        for column in range(32):
            color = LGRAY  # Cell color inside at 0
            if grid[row][column] == 1:
                color = BLACK  # Cell color inside at 1
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN + WINDOWMARGINX,
                              (MARGIN + HEIGHT) * row + MARGIN + WINDOWMARGINY,
                              WIDTH,
                              HEIGHT])
    food()
    sleep()
    timepassed()
    popup()


    # Limit to 60 frames per second
    clock.tick(60)


    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


# Needs to be the last line in the code, or it will hang on close/quit
pygame.quit()