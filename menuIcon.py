import pygame

from gameObject import GameObject
from infoBox import InfoBox

class MenuIcon(GameObject):
    def __init__(self, x, y, width, height, assets, game):
        super().__init__(x, y, width, height, assets.BaseImage, game)

    def onClick(self):
        self.info()

    def info(self):
        infoBox = InfoBox(self.x, self.y, "This is a menu icon", self.game)
