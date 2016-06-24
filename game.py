import pygame
from random import randint
import numpy as np
from Character import Hero
from Level import Level

pygame.init()
 
########################
### Config Constants ###
########################
screenWidth = 480
screenHeight = 320
levelWidth = 4800
levelHeight = screenHeight
heroFrame = 0

##################
### Setup game ###
##################
screen = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption("My Lovely Game")
clock = pygame.time.Clock()

###############
## Variables ##
###############
done = False

level = Level(screen)
hero = Hero(screen)

###################
### Load assets ###
###################

################# 
### Game loop ###
#################
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_d]:
        speed = 3
    elif keystate[pygame.K_a]:
        speed = -3
    else:
        speed = 0
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
    screen.fill([255,255,255])
    
    level.render(hero)

    hero.move(speed)

    hero.render()

    
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()