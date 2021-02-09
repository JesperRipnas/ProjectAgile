import pygame
import math
import os
from tamagotchi import * 

def knapp(circlecenter):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:   ##### DOWN NU, FIXA!
        x1, y1 = pygame.mouse.get_pos()
        x2, y2 = circlecenter
        distance = math.hypot(x1 - x2, y1 - y2)
        if distance <= 25:  ##### 25 = circle area
            print("X")

def background(path):
    screen.fill(GRAY)
    backgroundPic = pygame.image.load(path)
    backgroundPic = pygame.transform.scale(backgroundPic, (580, 745)) ###### FIXA!
    printPic = backgroundPic.get_rect()
    screen.blit(backgroundPic, printPic)
    
def debug(debug_var_list, x ,y, fontsize):
    debug_font = pygame.font.Font(None, fontsize)
    
    debug_pos = [x,y]
    for i, line in enumerate(debug_var_list):
        screen.blit(debug_font.render(line,1, (0,0,0)), (x, y + (i * 20)))


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

#
WINDOWMARGINX = 160
WINDOWMARGINY = 250

seconds_elapsed = 0


# Create a 2 dimensional array.
grid = []
for row in range(32):
    grid.append([])
    for column in range(32):
        grid[row].append(0)

# Set specific row/column to 1 (pixel on)
# grid[X][X] = 1

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = width, height = 580, 740
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Tamagotchi")

# Background music
pygame.mixer.music.load(assetpath + 'backgroundsong.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT+1,100)

current_tamagotchi = Tamagotchi("Dude",19911014)


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:

            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()

            if pos[0] > 100 and pos[1] > 100:
                try:
                # Change the x/y screen coordinates to grid coordinates
                    column = (pos[0] - WINDOWMARGINX)// (WIDTH + MARGIN)
                    row = (pos[1] - WINDOWMARGINY)// (HEIGHT + MARGIN)
                # Set that location to one
                    grid[row][column] = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)
                except:
                    print("utanför!")
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            #try:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            if pos[0] > 100 and pos[1] > 100:
                try:
                # Change the x/y screen coordinates to grid coordinates
                    column = (pos[0] - WINDOWMARGINX) // (WIDTH + MARGIN)
                    row = (pos[1] - WINDOWMARGINY) // (HEIGHT + MARGIN )
                # Set that location to one
                    grid[row][column] = 0
                    print("Click ", pos, "Grid coordinates: ", row, column)
                except:
                    print("Utanför!")
        elif event.type==pygame.USEREVENT+1:
            seconds_elapsed += 1
            print(seconds_elapsed)
            if seconds_elapsed % 365 == 0:
                current_tamagotchi.age += 1
                print("Happy bday")
    # Set the screen background
    background(assetpath + 'test.png')


    pygame.draw.circle(screen, BLACK, (190, 600), 25)  ##### TA BORT EFTER TEST!  A
    knapp((180, 590)) # Knapp A
    pygame.draw.circle(screen, BLACK, (290, 625), 25)  ##### TA BORT EFTER TEST!  B
    knapp((280,600))    # Knapp B
    pygame.draw.circle(screen, BLACK, (390, 600), 25)  ##### TA BORT EFTER TEST!  C
    knapp((390, 590))   # Knapp C
    debug(["Day", str(seconds_elapsed), "Year", str(current_tamagotchi.age)], 10, 10, 20)
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

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Needs to be the last line in the code, or it will hang on close/quit
pygame.quit()