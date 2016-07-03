import pygame
from random import randint
import numpy as np
#from Character import Hero
#from Level import Level
#from Weapon import Orb
from World import World

pygame.init()
 
########################
### Config Constants ###
########################
screenWidth = 480
screenHeight = 320
levelWidth = 4800
levelHeight = screenHeight
debug = False

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

################# 
### Game loop ###
#################
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                world.hero.startJump()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                world.hero.endJump()
 
    # Bavkground
    screen.fill([0,0,0])
    
    # Update
    world.hero.update()
    world.level.update(world.hero)
    world.orb.update(world.hero)

    #Render
    if(world.level.getCurrentSurface() == 1):
        screen.blit(world.level.surface1, [0 - world.level.position % (screenWidth + 160),0])
        screen.blit(world.level.surface2, [0 - world.level.position % (screenWidth + 160) + screenWidth + 160,0])
    else:
        screen.blit(world.level.surface2, [0 - world.level.position % (screenWidth + 160),0])
        screen.blit(world.level.surface1, [0 - world.level.position % (screenWidth + 160) + screenWidth + 160,0])

    screen.blit(world.hero.render(), (world.hero.position[0], world.hero.position[1]))
    pygame.draw.circle(screen, [255,255,255], world.orb.orbitPos, world.orb.getRadius())

    # Update screen
    pygame.display.flip()

    # Framerate
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()