import pygame
import numpy as np

class Level(object):

    spriteSheet = pygame.image.load("assets/spritesheet.png")
    tiles = np.load("assets/level.npy")
    spriteSheetWidth = 320
    spriteSheetHeight = 272
    tileWidth = 16
    tileHeight = 16
    position = 0

    def __init__(self, screen):
        self.screenWidth, self.screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.screen = screen

    def getTile(self, tileNumber):
        row = tileNumber / (self.spriteSheetWidth/self.tileWidth)
        column = tileNumber % (self.spriteSheetWidth/self.tileWidth)
        x = column * self.tileWidth
        y = row * self.tileHeight
        return [x, y, self.tileWidth, self.tileHeight]

    def fetchTiles(self):
        startColumn = self.position / self.tileWidth
        endColumn = startColumn + (self.screenWidth / self.tileHeight) + 1
        tilesToDraw = self.tiles[0:self.screenHeight/self.tileHeight, startColumn:endColumn]
        for rowCount, row in enumerate(tilesToDraw):
            for columnCount, column in enumerate(row):
                yield rowCount, columnCount

    def update(self, hero):
        if(hero.position[0] >= self.screenWidth * 0.65 and hero.speed[0] > 0):
            self.position += hero.speed[0]

    def render(self):
        for rowCount, columnCount in self.fetchTiles():
            self.screen.blit(self.spriteSheet, (columnCount * self.tileWidth - (self.position % self.tileWidth), rowCount * self.tileHeight), self.getTile(62))