import pygame

class Spritesheet(object):
    
    def __init__(self, filename, mask):
        self.spriteSheet = pygame.image.load(filename)
        self.mask = mask

    def getTile(self, tileNumber):
        row = tileNumber / (self.spriteSheet.get_rect().width/self.mask.width)
        column = tileNumber % (self.spriteSheet.get_rect().width/self.mask.width)
        rect = pygame.Rect(column * self.mask.width, row * self.mask.height, self.mask.width, self.mask.height)
        tile = pygame.Surface(rect.size)
        tile.set_colorkey([255,0,255], pygame.RLEACCEL)
        tile.blit(self.spriteSheet, (0, 0), rect)
        return tile

    def getTiles(self, tileNumbers):
        return [self.getTile(tileNumber) for tileNumber in tileNumbers]