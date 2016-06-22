import pygame
from random import randint

pygame.init()
 
# Define some colors
# Load assets 
spriteSheet = pygame.image.load("assets/spritesheet.png")

#Config vars
spriteSheetWidth = 320
spriteSheetHeight = 272
screenWidth = 480
screenHeight = 320
size = (screenWidth, screenHeight)
tileSize = 16

# build tile array - Todo, make this pull in a non random array
tiles = []
for i in range(0, 640):
    tiles.append(randint(3,340))

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
def drawTiles(tiles):
    xOffset = 0
    yOffset = 0
    for tile in tiles:
        if(xOffset > screenWidth):
            xOffset = 0
            yOffset += tileSize
        screen.blit(spriteSheet, (xOffset, yOffset), getTile(tile))
        xOffset += tileSize
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill([255,255,255])
    
    drawTiles(tiles)
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()