import pygame
from random import randint
import numpy as np

pygame.init()
 
# Define some colors
# Load assets 
spriteSheet = pygame.image.load("assets/spritesheet.png")

#Config vars
spriteSheetWidth = 320
spriteSheetHeight = 272
screenWidth = 480
screenHeight = 320
tileSize = 16

levelWidth = 4800

# for now assume level is horizontal only
levelHeight = screenHeight

pixelsScrolled = 0
levelPosition = 0

size = (screenWidth, screenHeight)

# build the 2D numpy tile list - Todo, make this pull in a non random array
tiles = np.ones((levelHeight/tileSize, levelWidth/tileSize), dtype=np.int)

# Game setup
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Lovely Game")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# get a tile from the spritesheet by number
def getTile(tileNumber):
    row = tileNumber / (spriteSheetWidth/tileSize)
    column = tileNumber % (spriteSheetWidth/tileSize)
    x = column * tileSize
    y = row * tileSize
    return [x,y,tileSize,tileSize]

# Draw the tile array to the screen
def drawScreenTiles(tiles, pixelsScrolled, levelPosition):

    startColumn = levelPosition / tileSize
    endColumn = startColumn + (screenWidth / tileSize) + 1

    tilesToDraw = tiles[0:20, startColumn:endColumn]

    print(startColumn)
    print(endColumn)

    rowCount = 0
    for row in tilesToDraw:
        columnCount = 0
        for column in row:
            screen.blit(spriteSheet, (columnCount * tileSize - pixelsScrolled, rowCount * tileSize), getTile(61))
            columnCount += 1
        rowCount += 1
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill([255,255,255])

    #tilesToDraw = tiles[0:640]

    levelPosition +=1

    pixelsScrolled += 1
    if pixelsScrolled >= tileSize:
        pixelsScrolled = 0

    drawScreenTiles(tiles, pixelsScrolled, levelPosition)
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()