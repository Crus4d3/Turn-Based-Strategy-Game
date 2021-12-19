import pygame

class Window():
    def __init__(self):
        #Setting up window
        self.width = 1000
        self.height = 1000
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Turn based strategy game")

    def drawFrame(self, game):
        self.window.blit(game.assets.BGImage, (0,0))
        for item in game.toDraw:
            self.window.blit(item.image, (item.x, item.y))
        pygame.display.update()

    def menuScreen(self, game):
        self.window.blit(game.assets.BGImage, (0,0))
        menuText = game.menuFont.render("Press space to play", 1, (255, 255, 255))
        xpos = self.width/2 - menuText.get_width()/2
        ypos = self.height/2 - menuText.get_height()/2
        self.window.blit(menuText, (xpos, ypos))
        pygame.display.update()
