import pygame
import os
import time
import random

from game import Game
from gameObject import GameObject
from infoBox import InfoBox
from window import Window
from assets import Assets
from base import Base
from mouseClick import MouseClick

def main():
    # Initialise pygame
    pygame.init()
    # Creating instances
    window = Window()
    assets = Assets(window)
    game = Game(window, assets)
    mouseClick = MouseClick(-10, -10, 15, 15, assets, game)
    game.mouseClick = mouseClick
    base = Base(window.WIDTH/2, window.HEIGHT/2, 50, 50, assets, game)
    # Starting game
    game.toDraw = [mouseClick, base]
    game.mainMenu()

if __name__ == "__main__":
    main()
