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
            (window.WIDTH, window.HEIGHT)
        )
        self.BaseImage = pygame.image.load(
            os.path.join(
                "assets",
                "BaseImage.png"
            )
        )
