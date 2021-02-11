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
    screen.blit(hunger_value_text, (250, 230))

    hunger_value_text = font.render('Y: '+str(current_tamagotchi.age), True, (0,0,0), None) 
    screen.blit(hunger_value_text, (310, 230))


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


def cashnotification():
    global notificationloop
    font = pygame.font.SysFont('timesnewroman', 23)
    if current_tamagotchi.popup_cash_state:
        cash_text = font.render('+$100', True, (0,0,0), None)
        screen.blit(cash_text, (171,254))
        if notificationloop == False:
            pygame.time.set_timer(pygame.USEREVENT+4,3000,1)
            notificationloop = True
    if current_tamagotchi.popup_rent_state:
        cash_text = font.render('-$40 Rent', True, (0,0,0), None)
        screen.blit(cash_text, (171,254))
        if notificationloop == False:
            pygame.time.set_timer(pygame.USEREVENT+4,3000,1)
            notificationloop = True


def warning():
    global testloop
    font = pygame.font.SysFont('timesnewroman', 15)
    if current_tamagotchi.warning:
        warning_text = font.render("(!)", True, (0,0,0), None)
        screen.blit(warning_text, (220, 230))
        if testloop == False:
            pygame.time.set_timer(pygame.USEREVENT+3,5000,1)
            testloop = True
    elif current_tamagotchi.buy:
        warning_text = font.render("-$10", True, (0,0,0), None)
        screen.blit(warning_text, (220, 230))
        if testloop == False:
            pygame.time.set_timer(pygame.USEREVENT+3,5000,1)
            testloop = True


def use_eat():
    global animation_itteration 
    animation_itteration = 0
    if current_tamagotchi.hunger_state:
        if current_tamagotchi.cash >= 10: 
            current_tamagotchi.cash -= 10
            global eating_animation
            eating_animation = True
            current_tamagotchi.buy = True
            sound_eating()        
        else:
            current_tamagotchi.warning = True
            sound_warning()


def buttonA():
    current_tamagotchi.hunger_state = not current_tamagotchi.hunger_state
    current_tamagotchi.energy_state = not current_tamagotchi.energy_state
    sound_buttonpress()


def buttonB():
    sound_buttonpress()
    use_eat()
    if current_tamagotchi.energy_state:
        global sleeping_animation
        sleeping_animation = True
        sound_sleeping()


def buttonC():
    current_tamagotchi.popup_state = not current_tamagotchi.popup_state
    sound_buttonpress()


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


# Local path to assets folder for user
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
testloop = False
notificationloop = False

# Menu vars
mid_w, mid_h = width / 2, (height / 2) - 50
cursor_rect = pygame.Rect(0, 0, 20, 20)
offset = - 185
cursor_state = "Start"
menu_state = "Main"
startx, starty = mid_w , mid_h + 30
optionsx, optionsy = mid_w, mid_h + 70
creditsx, creditsy = mid_w, mid_h + 110

cursor_rect.midtop = (startx + offset, starty)

#--------------------------------------
# Menu funcs
def draw_text(text, size, x, y ):
    font = pygame.font.Font(None,size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_surface,text_rect)

def draw_cursor():
    draw_text('->', 65, cursor_rect.x, cursor_rect.y)

def display_main_menu():
    background(assetpath + 'tama.jpg')

    draw_text("Start Game", 65, startx,starty)
    draw_text("create player", 65, optionsx, optionsy)
    draw_text("Credits", 65,creditsx,creditsy)
    draw_cursor()
    screen.blit(screen, (0,0))

def display_credits():
    background(assetpath+'tama.jpg')
    draw_text("Jesper", 45, mid_w, mid_h - 60)
    draw_text("Emil", 45, mid_w, mid_h - 30)
    draw_text("Denijad", 45, mid_w, mid_h)
    draw_text("Robert", 45, mid_w, mid_h  + 30)
    draw_text("Alex", 45, mid_w, mid_h  + 60)
    draw_text("Haydar", 45, mid_w, mid_h  + 90)
    screen.blit(screen, (0,0))


def creat_character(name, date):
    global current_tamagotchi
    current_tamagotchi = Tamagotchi(name, date)

#---------------------------------------

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT+1,game_speed)


# Default Object character
current_tamagotchi = Tamagotchi("Dude",19911014)


# Animtaion and timer to controll the speed
animation = Animation()
pygame.time.set_timer(pygame.USEREVENT+2,500)
eating_animation = False
sleeping_animation = False
animation_itteration = 0

menus = True

#Character creation
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()
name_input_box = pygame.Rect(640/2, 180-16, 140, 32)
date_input_box = pygame.Rect(640/2, 280-16, 140, 32)
name_text = ''
date_text = ''
date_num = 0
name = True
date = False
charactercreation = False

# -------- Main Program Loop -----------
while not done:
    while menus:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menus = False
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    #self.START_KEY = True
                    if cursor_state == "Start":
                        menus = False
                    elif cursor_state == "Credits":
                        menu_state = "Credits"
                if event.key == pygame.K_BACKSPACE:
                    if menu_state == "Credits":
                        menu_state = "Main"
                if event.key == pygame.K_DOWN:
                    if cursor_state == "Start":
                        cursor_rect.midtop = (optionsx + offset, optionsy)
                        cursor_state = "Create_Player"
                    elif cursor_state == "Create_Player":
                        cursor_rect.midtop = (creditsx + offset, creditsy)
                        cursor_state = "Credits"
                if event.key == pygame.K_UP:
                    if cursor_state == "Create_Player":
                        cursor_rect.midtop = (startx + offset, starty)
                        cursor_state = "Start"
                    elif cursor_state == "Credits":
                        cursor_rect.midtop = (optionsx + offset, optionsy)
                        cursor_state = "Create_Player"
        if menu_state == "Main":
            display_main_menu()
        elif menu_state == "Credits":
            display_credits()
        clock.tick(60)
        pygame.display.flip()

    while not charactercreation:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                charactercreation = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if name:
                        name = False
                        date = True
                    elif date and len(date_text) == 6:
                        try:
                            date_num = int(date_text)
                            charactercreation = True
                            creat_character(name_text, date_num)
                        except:
                            pass
                elif event.key == pygame.K_BACKSPACE:
                    if name:
                        name_text = name_text[:-1]
                    if date:
                        date_text = date_text[:-1]
                elif len(name_text) < 10 and name:
                    if name:
                        name_text += event.unicode
                elif len(date_text) < 6 and date:
                    if date:
                        date_text += event.unicode
        
        background(assetpath + 'tama.jpg')
        # Render the current text.
        nametxt_surface = font.render(name_text, True, pygame.Color('white'))
        datetxt_surface = font.render(date_text, True, pygame.Color('white'))
        # Resize the box if the text is too long.
        width = nametxt_surface.get_width()
        name_input_box.w = width
        
        name_width = nametxt_surface.get_width()
        date_width = datetxt_surface.get_width()
        
        # Blit the name text.
        name_input_box.x = (screen.get_width()/2)-name_width/2
        date_input_box.x = (screen.get_width()/2)-date_width/2
        screen.blit(nametxt_surface, (name_input_box.x+5, name_input_box.y+5))
        staticnametext = font.render('Input charter name:', True, pygame.Color('white'))
        screen.blit(staticnametext, (((screen.get_width())-(11*len('Input charter name:')))/2, 140-16))
        # Blit the date text.
        screen.blit(datetxt_surface, (date_input_box.x+5, date_input_box.y+5))
        staticnametext = font.render('Input charter birthdate (xxxxxx):', True, pygame.Color('white'))
        screen.blit(staticnametext, (((screen.get_width())-(10*len('Input charter birthdate (xxxxxx):')))/2, 240-16))
        

        pygame.display.flip()
        clock.tick(30)
    
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
        #KEY TRIGGERS
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
            if not current_tamagotchi.dead:
                current_tamagotchi.update()
                if seconds_elapsed % 365 == 0:
                    current_tamagotchi.age += 1
                if seconds_elapsed % 30 == 0:
                    current_tamagotchi.cash += 100
                    current_tamagotchi.popup_cash_state = True
                if seconds_elapsed % 34 == 0:
                    current_tamagotchi.cash -= 40
                    current_tamagotchi.popup_rent_state = True
            if current_tamagotchi.hunger < 20:
                sound_alarm()

        #Animation timer cycle
        elif event.type==pygame.USEREVENT+2:
            if current_tamagotchi.dead:
                animation.play_dying()
            elif current_tamagotchi.asleep:
                sleeping_animation = True
                current_tamagotchi.asleep = False
            elif eating_animation:
                animation_itteration += 1
                animation.play_eat()
                if animation_itteration >= 4:
                    eating_animation = False
                    animation_itteration = 0
                    current_tamagotchi._eat()
            elif sleeping_animation:
                animation_itteration += 1
                animation.play_sleep()
                if animation_itteration >= 8:
                    sleeping_animation = False
                    animation_itteration = 0
                    current_tamagotchi._sleep()
                    current_tamagotchi.asleep = False
            elif seconds_elapsed % 365 == 0 and seconds_elapsed != 0:
                animation.play_birthday()
            else:
                animation.play_idle()
            grid = animation.play_animation()
        elif event.type == pygame.USEREVENT+3:
            current_tamagotchi.warning = False
            current_tamagotchi.buy = False
            testloop = False
        elif event.type == pygame.USEREVENT+4:
            current_tamagotchi.popup_cash_state = False
            current_tamagotchi.popup_rent_state = False
            notificationloop = False


    # Set the screen background
    background(assetpath + 'background.png')


    if show_debug:
        debug(["Day: " + str(seconds_elapsed), "Year: " + str(current_tamagotchi.age),"Hunger: " + str(current_tamagotchi.hunger), "Energy: " + str(current_tamagotchi.energy),
        "One day = " + str(game_speed) + " ms","FPS: " + str(int(clock.get_fps())) ], 10, 10, 20)

    
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


    # Call for functions
    food()
    sleep()
    timepassed()
    popup()
    cashnotification()
    warning()


    # Limit to 60 frames per second
    clock.tick(60)


    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


# Needs to be the last line in the code, or it will hang on close/quit
pygame.quit()