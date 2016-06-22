import pygame
 
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
PI = 3.141592653

size = (800, 600)
screen = pygame.display.set_mode(size)

spriteSheet = pygame.image.load("assets/spritesheet.png")
 
pygame.display.set_caption("My Lovely Game")

 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(WHITE)
 
    #imagerect = spriteSheet.get_rect()
    screen.blit(spriteSheet, (0,0), (64,128,16,16))
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()