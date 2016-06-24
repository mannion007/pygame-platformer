import pygame

class Hero:

    spriteSheet = pygame.image.load("assets/hero.png")
    spriteSheetSize = [630,48]
    tileSize = [30,48]
    speed = [0,0]
    
    frame = 0
    state = 'stand'
    position = [50,0]

    gravity = 0.75
    onGround = False
   
    def __init__(self, screen):
        self.screenWidth, self.screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.screen = screen
        self.surface = pygame.Surface(self.tileSize)

    def getTile(self, tileNumber):
        row = tileNumber / (self.spriteSheetSize[0]/self.tileSize[0])
        column = tileNumber % (self.spriteSheetSize[0]/self.tileSize[0])
        x = column * self.tileSize[0]
        y = row * self.tileSize[1]
        return [x, y, self.tileSize[0], self.tileSize[1]]

    def startJump(self):
        if(self.onGround):
            self.speed[1] = -16
            self.frame = 4
            self.onGround = False

    def endJump(self):
        if(self.speed[1] < -8):
            self.speed[1] = -8

    def update(self):
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_d]:
            self.speed[0] = 3
            if self.onGround:
                self.frame = 8
                self.state = 'run'
        elif keystate[pygame.K_a]:
            self.speed[0] = -3
            if self.onGround:
                self.frame = 8
                self.state = 'run'
        else:
            self.speed[0] = 0
            if self.onGround:
                self.frame = 20
                self.state = 'stand'

        self.speed[1] += self.gravity
        self.position[1] += self.speed[1]
        
        if(self.position[1] > 250):
            self.position[1] = 250
            self.speed[1] = 0
            self.onGround = True

        if(self.speed[0] > 0):
            if(self.position[0] < self.screenWidth * 0.65 and self.speed[0] > 0):
                self.position[0] += self.speed[0]
        elif(self.speed[0] < 0):
            if(self.position[0] > 0):
                self.position[0] += self.speed[0]

    def render(self):
        self.screen.blit(self.spriteSheet, (self.position[0], self.position[1]), self.getTile(self.frame))