import pygame

from gameObject import GameObject
from infoBox import InfoBox

class Base(GameObject):
    def __init__(self, x, y, width, height, assets, game):
        super().__init__(x, y ,width, height, assets.BaseImage, game)
        self.mask = pygame.mask.from_surface(self.image)

    def onClick(self):
        self.info()

    def info(self):
        infoBox = InfoBox(self.x, self.y - self.height, "This is your base!", self.game)
