import pygame

from infoBox import InfoBox
from menuIcon import MenuIcon

class Game:
    def __init__(self, window, assets):
        self.window = window
        self.assets = assets
        self.run = True
        self.lost = False
        self.toDraw= []
        self.FPS = 15
        self.clock = pygame.time.Clock()
        self.infoFont = pygame.font.SysFont("arial", 20)

    def takeInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    def removeInfoBox(self):
        for item in self.toDraw:
            if isinstance(item, InfoBox) or isinstance(item, MenuIcon):
                item.removeFromToDraw()

    def main(self):
        self.takeInputs()
        self.mouseClick.moveToMouseClick()
        self.mouseClick.itemsClicked(self.toDraw)
        self.window.drawFrame(self)
        self.removeInfoBox()

    def mainMenu(self):
        pygame.mouse.set_visible(True)
        while self.run:
            self.main()
