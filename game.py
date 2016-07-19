import pygame
from random import randint
import numpy as np
from World import World

pygame.init()
 
########################
### Config Constants ###
########################
screenWidth = 480
screenHeight = 320

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
world = World()
debug = True

################# 
### Game loop ###
#################
while not done:
 
    # Read cotrols
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                world.hero.startJump()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                world.hero.endJump()
 
    # Update
    world.update(pygame.key.get_pressed())

    #Render
    world.render(screen)

    pygame.display.flip()
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()