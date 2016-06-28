import pygame
import math
phi = math.pi * 2

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

    framesToDelay = 3
    framesDelayed = 0
    currentFrame = 0

    orbitFramesDelayed = 0
    currentOrbitFrameDelayed = 0

    minOrbitRadius = 35
    maxOrbitRadius = 300
    orbitRadius = 35

    orbitPos = [0,0]
   
    def __init__(self, screen):
        self.screenWidth, self.screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.screen = screen
        self.surface = pygame.Surface(self.tileSize)
        self.runGen = self.getRunFrame()
        self.standGen = self.getStandFrame()
        self.jumpGen = self.getJumpFrame()
        self.updateHeroFrame()

    def getTile(self, tileNumber):
        row = tileNumber / (self.spriteSheetSize[0]/self.tileSize[0])
        column = tileNumber % (self.spriteSheetSize[0]/self.tileSize[0])
        x = column * self.tileSize[0]
        y = row * self.tileSize[1]
        return [x, y, self.tileSize[0], self.tileSize[1]]

    def updateHeroFrame(self):
        self.framesDelayed += 1
        if(self.state == 'stand'):
            if(self.framesDelayed >= 10):
                self.framesDelayed = 0
                self.currentFrame = next(self.standGen)
        elif(self.state == 'run'):
            if(self.framesDelayed >= 5):
                self.framesDelayed = 0
                self.currentFrame = next(self.runGen)
        elif(self.state == 'jump'):
            if(self.framesDelayed >= 3):
                self.framesDelayed = 0
                self.currentFrame = next(self.jumpGen)

    def updateOrbitPos(self):
        #self.orbitFramesDelayed += 1
        #if(self.framesDelayed >= 5):
            #self.orbitFramesDelayed = 0
        self.orbitPos = self.orbit([self.position[0] + self.tileSize[0] / 2, self.position[1] + self.tileSize[1] / 2], self.orbitRadius, pygame.time.get_ticks() * 0.001)

    def getRunFrame(self):
        while True:
            yield 5
            yield 6
            yield 7
            yield 8
            yield 9
            yield 10
            yield 11
            yield 12
            yield 13
            yield 14
            yield 15
            yield 16

    def getStandFrame(self):
        while True:
            yield 17
            yield 18
            yield 19
            yield 20

    def getJumpFrame(self):
        yield 0
        yield 1
        yield 2
        yield 3

        while True:
            yield 4

    def startJump(self):
        if(self.onGround):
            self.speed[1] = -16
            self.state = 'jump'
            self.onGround = False

    def endJump(self):
        if(self.speed[1] < -8):
            self.speed[1] = -8

    def update(self):
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_d]:
            self.speed[0] = 3
            if self.onGround:
                self.state = 'run'
        elif keystate[pygame.K_a]:
            self.speed[0] = -3
            if self.onGround:
                self.state = 'run'
        else:
            self.speed[0] = 0
            if self.onGround:
                self.state = 'stand'

        if keystate[pygame.K_SPACE]:
            if(self.orbitRadius < self.maxOrbitRadius):
                self.orbitRadius += 2
        else:
            if(self.orbitRadius > self.minOrbitRadius):
                self.orbitRadius -= 3

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

    def orbit(self, origin, radius, time):
        #normalise phi, to get the angle in time
        angle = phi * time 
        rsa = radius * math.sin(angle)
        rca = radius * math.cos(angle)
        return (int(origin[0] + rca), int(origin[1] + rsa))

    def render(self):
        self.updateHeroFrame()
        self.updateOrbitPos()
        
        self.screen.blit(self.spriteSheet, (self.position[0], self.position[1]), self.getTile(self.currentFrame))
        pygame.draw.circle(self.screen, [255,255,255], self.orbitPos, self.orbitRadius / 7)