# Jake Johnson, 6/6/23, to create a car game
#Imports
import pygame
import time
import random
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
dark_green = (1,50,32)
bright_red = (255,0,0)
bright_green = (0,255,0)

block_colour = (53,115,255)

#Car size
car_width = 75

#Sets game window and name
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('BROOOM BROOOM')
clock = pygame.time.Clock()

#Images
#creates car
carImg = pygame.image.load('Images/car.png')
car_size = pygame.transform.scale(carImg, (100, 150))
roadImg = pygame.image.load('Images/road.png')
road_Big = pygame.transform.scale(roadImg, (800, 600))


#Will count the amount of times dodged
def things_dodged(count):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))
    

def things(thingx, thingy, thingw, thingh, colour):
    pygame.draw.rect(gameDisplay, colour, [thingx, thingy, thingw, thingh])

#places the car on screen
def car(x,y):
    gameDisplay.blit(car_size, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#Creates the message font and size
#Resets game when crashed
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    #Waits 2 seconds before taking user back into the game
    time.sleep(2)

    game_loop()

#Displays Crashed message on screen
def crash():
    message_display('You Crashed')

#Menu screen buttons and actions
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("BROOM BROOM", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("GO!",150,450,100,50,green,bright_green,"play")         
        button("Quit",550,450,100,50,red,bright_red,"quit")     
 
        pygame.display.update()
        clock.tick(15)



def game_loop():
    
    #Cars start position 
    x = (display_width * 0.45) #0.45
    y = (display_height * 0.76) #0.85

    #Used to change the cars position
    x_change = 0

    #Random starting position
    thing_startx = random.randrange(0, display_width)
    #Rectangle size and speed
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    dodge = 0

    gameExit = False

    while not gameExit:

        #closes game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #arrow keys move car
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -4
                elif event.key == pygame.K_RIGHT:
                    x_change = 4

            #Stops the car once key is lifted
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


        x += x_change

        #Background colour
        gameDisplay.fill(dark_green)

        gameDisplay.blit(road_Big, (0,0))

        things(thing_startx, thing_starty, thing_width, thing_height, block_colour)
        thing_starty += thing_speed
                
        #car position
        car(x,y)


        things_dodged(dodge)

        if x > 630 - car_width or x < 150:
            crash()

        #checks dogdes and makes rectangles faster
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodge += 1
            thing_speed += 1
            

        if y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width:
                crash()

        #Updating the display by 60 ticks a second
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()