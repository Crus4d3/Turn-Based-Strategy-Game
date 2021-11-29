import pygame
import time
import logging

from gameObject import GameObject

class InfoBox(GameObject):
    def __init__(self, x, y, message, game):
        self.image = game.infoFont.render(message, 1, (255, 255, 255)) 
        super().__init__(
            x,
            y,
            self.image.get_width(),
            self.image.get_height(),
            self.image,
            game
        )
        self.y -= self.height + 10 # Buffer zone to make things more readable
        game.toDraw.append(self)
        self.startTime = time.time()

    def removeFromToDraw(self):
        logging.info("self.game.mouseClick.clicked = {}".format(self.game.mouseClick.clicked))
        logging.info("self = {}".format(self))
        if self.game.mouseClick.clicked != self:
            self.game.toDraw.remove(self)
