import pygame
import time
import logging

from gameObject import GameObject
from infoBox import InfoBox

class MenuIcon(GameObject):
    def __init__(self, x, y, width, height, assets, game, temp):
        super().__init__(x, y, width, height, assets.MenuIconImage, game)
        self.game.toDraw.append(self)
        self.startTime = time.time()
        self.temp = temp

    def onClick(self):
        self.info()

    def info(self):
        infoBox = InfoBox(self.x, self.y, "This is a menu icon", self.game)

    def removeFromToDraw(self):
        if self.temp:
            logging.info("self.game.mouseClick.clicked = {}".format(self.game.mouseClick.clicked))
            logging.info("self = {}".format(self))
            if self.game.mouseClick.clicked != self:
                self.game.toDraw.remove(self)
