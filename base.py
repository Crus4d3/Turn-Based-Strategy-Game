import pygame

from gameObject import GameObject
from window import Window
from infoBox import InfoBox
from menuIcon import MenuIcon

class Base(GameObject):
    def __init__(self, x, y, width, height, assets, game):
        super().__init__(x, y ,width, height, assets.BaseImage, game)
        self.assets = assets

    def onClick(self):
        self.info()
        self.makeMenuIcon()

    def info(self):
        infoBox = InfoBox(self.x, self.y, "This is your base!", self.game)

    def makeMenuIcon(self):
        menuIcon = MenuIcon(
            self.window.width - 50,
            self.window.height - 50,
            50,
            50,
            self.assets,
            self.game,
            False,
        )
