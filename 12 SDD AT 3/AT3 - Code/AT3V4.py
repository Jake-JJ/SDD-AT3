# Jake Johnson, 10/6/23, to create a car game
# Imports
import pygame
import random

# Used to initialize all imported pygame modules
pygame.init()

# Make window size
display_width = 800
display_height = 600

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (153, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
bright_blue = (0, 150, 255)
dark_green = (1, 50, 32)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
block_colour = (53, 115, 255)

# Car size
car_width = 75

# Sets game window and name
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('GET AWAY')
clock = pygame.time.Clock()

# Images
carImg = pygame.image.load('Images/car.png').convert_alpha()
car_size = pygame.transform.scale(carImg, (100, 150)).convert_alpha()
car_rect = car_size.get_rect(center = (400,200))
car_normal = car_size, car_rect
# Was going to be used to turn the are left when moving left
car_left = pygame.transform.rotate(car_size, (20))

roadImg = pygame.image.load('Images/road.png').convert_alpha()
road_Big = pygame.transform.scale(roadImg, (800, 600)).convert_alpha()

enemy = pygame.image.load('Images/enemy.png').convert_alpha()
enemy_size = pygame.transform.scale(enemy, (100,150)).convert_alpha()

bars = pygame.image.load('Images/bars.png').convert_alpha()
bars_size = pygame.transform.scale(bars, (800,600))
bars_rect = bars_size.get_rect(topleft = (0,0))

# Icon
pygame.display.set_icon(carImg)

pause = False


# Will count the amount of times dodged
def things_dodged(count):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))
    return count


# Blocks/Enemy/Police
def things(thingx, thingy, thingw, thingh, colour):
    gameDisplay.blit(enemy_size, (thingx, thingy, thingw, thingh))


# places the car on screen
def car(x, y):
    gameDisplay.blit(car_size, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

# Quit function
def quitgame():
    pygame.quit()
    quit()

# Used to unpause game
def unpause():
    global pause
    pause = False

# Used to pause game
def paused():

    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 150, 450, 100, 50, green, bright_green, 'continue')
        button("Menu", 550, 450, 100, 50, red, bright_red, 'Menu')

        pygame.display.update()
        clock.tick(15)

# Displays Crashed message on screen
def crash(count):
    gameDisplay.fill(dark_green)
    gameDisplay.blit(bars_size, bars_rect)

    # Big text after death
    largeText = pygame.font.SysFont("comicsansms", 110)
    TextSurf, TextRect = text_objects("You Got Caught", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    # Attempting to show score on death screen
    largeText = pygame.font.SysFont("comicsansms", 50)
    TextSurf, TextRect = text_objects("Dodged: " + str(count), largeText)
    TextRect.center = ((display_width / 2), (400))
    gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Buttons
        button("Escape", 150, 450, 100, 50, green, bright_green, 'play')
        button("Menu", 550, 450, 100, 50, red, bright_red, 'Menu')

        pygame.display.update()
        clock.tick(15)


def game_help():
    helps = True
    while helps:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Background colour
        gameDisplay.fill(dark_green)

        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects("GET AWAY: HELP", largeText)
        TextRect.center = ((display_width / 2), (50))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects("CONTROLS", largeText)
        TextRect.center = ((display_width / 2), (120))
        gameDisplay.blit(TextSurf, TextRect)

        text = pygame.font.SysFont("comicsansms", 20)
        TextSurf, TextRect = text_objects("To move the car left or right you can either use:", text)
        TextRect.center = ((display_width / 2), (150))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("'a''d' or the left and right arrows keys", text)
        TextRect.center = ((display_width / 2), (170))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Pause the game by pressing 'ESC', can be used to return to the menu", text)
        TextRect.center = ((display_width / 2), (200))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("AIM OF THE GAME", largeText)
        TextRect.center = ((display_width / 2), (260))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Your on the run from the police", text)
        TextRect.center = ((display_width / 2), (290))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Moving your car left and right to dodge the police driving towards you", text)
        TextRect.center = ((display_width / 2), (310))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("You will lose and get caught if you run off the road or get hit by the police", text)
        TextRect.center = ((display_width / 2), (330))
        gameDisplay.blit(TextSurf, TextRect)

        ########
        # REACHING DIFFERENT STAGES THE LONGER YOU LAST

        
        button("Menu", 350, 450, 100, 50, red, bright_red, 'Menu')

        pygame.display.update()
        clock.tick(15)

# Menu screen buttons and actions
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            #Opens the different screens
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "continue":
                unpause()
            elif action == "Menu":
                game_intro()
            elif action == "help":
                game_help()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

# Intro screen
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Background colour
        gameDisplay.fill(dark_green)
        # Car
        gameDisplay.blit(car_size, car_rect)
        # Title
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("GET AWAY", largeText)
        TextRect.center = ((display_width / 2), (50))
        gameDisplay.blit(TextSurf, TextRect)

        # Buttons
        button("GO!", 350, 300, 100, 50, green, bright_green, "play")
        button("Quit", 350, 500, 100, 50, red, bright_red, "quit")
        button("Help", 350, 400, 100, 50, blue, bright_blue, "help")

        # Updates display
        pygame.display.update()
        clock.tick(15)

# Main game loop
def game_loop():
    global pause
    # Cars start position
    x = (display_width * 0.45)  # 0.45
    y = (display_height * 0.76)  # 0.85

    # Used to change the cars position
    x_change = 0

    # Random starting position
    thing_startx = random.randrange(200, 550)
    # Rectangle size and speed
    thing_starty = -600
    thing_speed = 4
    thing_width = 60
    thing_height = 60

    score = 1
    dodge = 0

    gameExit = False

    while not gameExit:

        # closes game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # arrow keys move car
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -4
                elif event.key == pygame.K_RIGHT:
                    x_change = 4
                elif event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            # Stops the car once key is lifted
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            
            # Using 'a' and 'd' to move the car left and right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -4
                elif event.key == pygame.K_d:
                    x_change = 4

            # Stops the car once key is lifted
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

        # Cars postion
        x += x_change

        # Background colour
        gameDisplay.fill(dark_green)

        # Road / Where the car can go
        gameDisplay.blit(road_Big, (0, 0))

        things(thing_startx, thing_starty, thing_width, thing_height, block_colour)
        thing_starty += thing_speed

        # car position
        car(x, y)

        things_dodged(dodge)

        # Crashes if car runs off the road
        if x > 630 - car_width or x < 150:
            crash(dodge)

        # checks dodges and makes rectangles faster
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(200, 550)
            dodge += 1
            thing_speed += 0.5
            # Progressively enemy gets faster
            if thing_speed >= 10 and thing_speed < 10:
                thing_speed += 1
            if thing_speed >= 15:
                thing_speed += 1.5

            # Adds Score
            if thing_speed == 5:
                score += 1
            if thing_speed == 10:
                score += 1
            if thing_speed == 20:
                score += 1
            if thing_speed == 30:
                score += 1

        # Displaying the stage number on the screen
        font = pygame.font.SysFont(None, 50)
        display_score = font.render("Wanted: " + str(score), True, black)
        gameDisplay.blit(display_score, (630, 0))

        # Detects collisions for crashing
        if y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width:
                crash(dodge)

        # Updating the display by 60 ticks a second
        pygame.display.update()
        clock.tick(60)


# Running the main functions
game_intro()
game_loop()
game_help()

pygame.quit()
quit()
