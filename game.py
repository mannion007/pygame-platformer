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

################# 
### Game loop ###
#################
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hero.startJump()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                hero.endJump()
 
    # Drawing
    screen.fill([255,255,255])
    
    # Updating
    level.update(hero)
    hero.update()

    level.render()    
    hero.render()

    # Update screen
    pygame.display.flip()

    # Framerate
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()