import pygame
import math
phi = math.pi * 2

class Orb:

    orbitRadius = 35
    minOrbitRadius = 35
    maxOrbitRadius = 300

    orbitPos = [0,0]

    def __init__(self, screen):
        self.screen = screen

    def calculatePosition(self, origin, radius, time):
        angle = phi * time 
        rsa = radius * math.sin(angle)
        rca = radius * math.cos(angle)
        return (int(origin[0] + rca), int(origin[1] + rsa))

    def update(self, character):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            if(self.orbitRadius < self.maxOrbitRadius):
                self.orbitRadius += 2
        else:
            if(self.orbitRadius > self.minOrbitRadius):
                self.orbitRadius -= 3

        self.orbitPos = self.calculatePosition([character.position[0] + character.tileSize[0] / 2, character.position[1] + character.tileSize[1] / 2], self.orbitRadius, pygame.time.get_ticks() * 0.001)

    def render(self):       
        pygame.draw.circle(self.screen, [255,255,255], self.orbitPos, self.orbitRadius / 7)