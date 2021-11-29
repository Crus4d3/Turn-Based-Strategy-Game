import pygame

from base import Base
from infoBox import InfoBox
from menuIcon import MenuIcon
from mouseClick import MouseClick

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

    def initGame(self):
        self.mouseClick = MouseClick(-10, -10, 15, 15, self.assets, self)
        self.base = Base(self.window.width/2, self.window.height/2, 50, 50, self.assets, self)
        self.menuIcon = MenuIcon(0, self.window.width - 50, 50, 50, self.assets, self, False)
        self.base.window = self.window
        self.toDraw = [self.mouseClick, self.base, self.menuIcon]

    def main(self):
        self.takeInputs()
        self.mouseClick.moveToMouseClick()
        self.mouseClick.itemsClicked(self.toDraw)
        self.window.drawFrame(self)
        self.removeInfoBox()

    def mainMenu(self):
        pygame.mouse.set_visible(True)
        self.initGame()
        while self.run:
            self.main()
