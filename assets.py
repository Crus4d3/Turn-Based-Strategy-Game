import pygame
import os

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
            (window.width, window.height)
        )
        self.BaseImage = pygame.image.load(
            os.path.join(
                "assets",
                "BaseImage.png"
            )
        )
        self.MenuIconImage = pygame.image.load(
            os.path.join(
                "assets",
                "MenuIconImage.png"
            )
        )
