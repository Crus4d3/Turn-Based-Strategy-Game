import pygame
import time

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
        self.mask = pygame.mask.from_surface(self.image)
        game.toDraw.append(self)
        startTime = time.time()
        print(startTime)

    def removeFromToDraw(self):
        pass
