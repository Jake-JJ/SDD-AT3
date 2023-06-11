# Jake Johnson, 10/6/23, separate file to open the main game
#Imports
import pygame
from AT3V4 import *


#Used to initialize all imported pygame modules
pygame.init()

#make window size
display_width = 800
display_height = 600

#Colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,200,0)
dark_green = (1, 50, 32)
bright_red = (255,0,0)
bright_green = (0,255,0)

#Car size
car_width = 75

#Sets game window and name
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('BROOM BROOM')
clock = pygame.time.Clock()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
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
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("GET AWAY", largeText)
        TextRect.center = ((display_width / 2), (50))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 350, 300, 100, 50, green, bright_green, "play")
        button("Quit", 350, 500, 100, 50, red, bright_red, "quit")
        button("Help", 350, 400, 100, 50, blue, bright_blue, "help")

        pygame.display.update()
        clock.tick(15)


game_intro()