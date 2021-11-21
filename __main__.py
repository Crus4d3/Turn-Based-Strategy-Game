import pygame
import os
import time
import random
pygame.init()

class Window():
    def __init__(self):
        #Setting up window
        self.WIDTH = 1000
        self.HEIGHT = 1000
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Turn based strategy game")

class Assets():
    def __init__(self, window):
        # Setting up images
        self.RedCircleImage = pygame.image.load(
            os.path.join(
                "assets",
                "RedCircleImage.png"
            )
        )
        self.BGImage = pygame.transform.scale(
            pygame.image.load(
                os.path.join(
                    "assets",
                    "BGImage.png"
                )
            ),
            (window.WIDTH, window.HEIGHT)
        )
        self.BaseImage = pygame.image.load(
            os.path.join(
                "assets",
                "BaseImage.png"
            )
        )

# #Setting up window
# wIDTH, HEIGHT = 1000, 1000
# wINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Turn based strategy game")
# 
# # Setting up images
# redCircleImage = pygame.image.load(
#     os.path.join(
#         "assets",
#         "RedCircleImage.png"
#     )
# )
# bGImage = pygame.transform.scale(
#     pygame.image.load(
#         os.path.join(
#             "assets",
#             "BGImage.png"
#         )
#     ),
#     (WIDTH, HEIGHT)
# )
# BaseImage = pygame.image.load(
#     os.path.join(
#         "assets",
#         "BaseImage.png"
#     )
# )

class Game:
    def __init__(self, window, assets, mouseClick):
        self.window = window
        self.assets = assets
        self.mouseClick = mouseClick
        self.run = True
        self.lost = False
        self.toDraw= []
        self.FPS = 15
        self.clock = pygame.time.Clock()
        self.infoFont = pygame.font.SysFont("arial", 20)

    def drawFrame(self):
        self.window.WINDOW.blit(self.assets.BGImage, (0,0))
        for item in self.toDraw:
            self.window.WINDOW.blit(item.image, (item.x, item.y))
        pygame.display.update()

    def takeInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    def main(self):
        self.takeInputs()
        self.mouseClick.moveToMouseClick()
        self.mouseClick.itemsClicked(self.toDraw)
        self.drawFrame()

    def mainMenu(self):
        pygame.mouse.set_visible(True)
        while self.run:
            self.main()

class GameObject:
    def __init__(self, x, y, width, height, image, game):
        self.x = int(x)
        self.y = int(y)
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.game = game

    def onClick(self):
        pass

class InfoBox(GameObject):
    def __init__(self, x, y, message, game):
        self.image = game.infoFont.render(message, 1, (255, 255, 255)) 
        super().__init__(x, y, self.image.get_width(), self.image.get_height(), self.image, game)
        self.mask = pygame.mask.from_surface(self.image)
        game.toDraw.append(self)

class Base(GameObject):
    def __init__(self, x, y, width, height, assets, game):
        super().__init__(x, y ,width, height, assets.BaseImage, game)
        self.mask = pygame.mask.from_surface(self.image)

    def onClick(self):
        self.info()

    def info(self):
        infoBox = InfoBox(self.x, self.y - self.height, "This is your base!", self.game)

class MouseClick(GameObject):
    def __init__(self, x, y, width, height, assets):
        super().__init__(x, y, width, height, assets.RedCircleImage, "Haha this is a bad hack deal with it!")
        self.x = int(self.x - self.width/2)
        self.y = int(self.y - self.height/2)
        self.mask = pygame.mask.from_surface(self.image)

    def moveToMouseClick(self):
        if pygame.mouse.get_pressed()[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            self.x, self.y = int(mouseX - self.width/2), int(mouseY - self.height/2)

    def itemsClicked(self, toDraw):
        for item in toDraw:
            overlapX = item.x - self.x
            overlapY = item.y - self.y
            if self.mask.overlap(item.mask, (overlapX, overlapY)) and type(item) != type(self):
                item.onClick()

def main():
    # Creating instances
    window = Window()
    assets = Assets(window)
    mouseClick = MouseClick(-10, -10, 15, 15, assets)
    game = Game(window, assets, mouseClick)
    base = Base(window.WIDTH/2, window.HEIGHT/2, 50, 50, assets, game)
    # Starting game
    game.toDraw = [mouseClick, base]
    game.mainMenu()

if __name__ == "__main__":
    main()
