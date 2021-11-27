import pygame

from gameObject import GameObject

class MouseClick(GameObject):
    def __init__(self, x, y, width, height, assets, game):
        super().__init__(x, y, width, height, assets.RedCircleImage, game)
        self.x = int(self.x - self.width/2)
        self.y = int(self.y - self.height/2)

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
