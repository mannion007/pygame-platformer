import pygame
from Character import Hero
from Level import Level
from Weapon import Orb

class World:

    def __init__(self):
        self.level = Level()
        self.hero = Hero()
        self.orb = Orb()