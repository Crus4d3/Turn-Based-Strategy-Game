import pygame

class Window():
    def __init__(self):
        #Setting up window
        self.WIDTH = 1000
        self.HEIGHT = 1000
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Turn based strategy game")

    def drawFrame(self, game):
        self.WINDOW.blit(game.assets.BGImage, (0,0))
        for item in game.toDraw:
            self.WINDOW.blit(item.image, (item.x, item.y))
        pygame.display.update()
