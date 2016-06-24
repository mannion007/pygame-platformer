import pygame
from random import randint
import numpy as np
import hero

pygame.init()
 
########################
### Config Constants ###
########################
spriteSheetWidth = 320
spriteSheetHeight = 272
screenWidth = 480
screenHeight = 320
tileSize = 16
tileWidth = 16
tileHeight = 16
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
pixelsScrolled = 0
levelPosition = 0

###################
### Load assets ###
###################
spriteSheet = pygame.image.load("assets/spritesheet.png")
tiles = np.load("assets/level1.npy")

print(tiles)

##########
## Hero ##
##########
heroSpriteSheet = pygame.image.load("assets/hero.png")
theHero = hero

###############
## Functions ##
###############
def getTile(tileNumber, tileWidth, tileHeight, spriteSheetWidth):
    row = tileNumber / (spriteSheetWidth/tileWidth)
    column = tileNumber % (spriteSheetWidth/tileWidth)
    x = column * tileWidth
    y = row * tileHeight
    return [x,y,tileWidth,tileHeight]

def fetchTiles(startColumn, endColumn):
    tilesToDraw = tiles[0:screenHeight/tileSize, startColumn:endColumn]
    for rowCount, row in enumerate(tilesToDraw):
        for columnCount, column in enumerate(row):
            yield rowCount, columnCount

def drawScreenTiles(tiles, pixelsScrolled, levelPosition):
    startColumn = levelPosition / tileSize
    endColumn = startColumn + (screenWidth / tileSize) + 1
    tilesToDraw = tiles[0:20, startColumn:endColumn]
    for rowCount, columnCount in fetchTiles(startColumn, endColumn):
        screen.blit(spriteSheet, (columnCount * tileSize - pixelsScrolled, rowCount * tileSize), getTile(tiles[rowCount][columnCount], tileWidth, tileHeight, spriteSheetWidth))

def drawHero(heroFrame):
    screen.blit(heroSpriteSheet, (50, 50), getTile(heroFrame, 30, 48, 510))

#np.save("assets/level.txt", tiles)

################# 
### Game loop ###
#################
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_d]:
        if(levelPosition < levelWidth):
            levelPosition +=2
            pixelsScrolled += 2
            if pixelsScrolled >= tileSize:
                pixelsScrolled = 0
    if keystate[pygame.K_a]:
        if(levelPosition > 0):
            levelPosition -=2
            pixelsScrolled -= 2
            if pixelsScrolled <= 0:
                pixelsScrolled = tileSize
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
    screen.fill([255,255,255])
    drawScreenTiles(tiles, pixelsScrolled, levelPosition)

    heroFrame += 1
    if(heroFrame >= 17):
        heroFrame = 0

    drawHero(heroFrame)
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(20)
 
# Be IDLE friendly
pygame.quit()