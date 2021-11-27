import pygame
import os
import time
import random
import logging

from game import Game
from gameObject import GameObject
from infoBox import InfoBox
from window import Window
from assets import Assets
from base import Base
from mouseClick import MouseClick
from menuIcon import MenuIcon

def main():
    # Initialise pygame
    pygame.init()
    # Creating instances
    window = Window()
    assets = Assets(window)
    game = Game(window, assets)
    mouseClick = MouseClick(-10, -10, 15, 15, assets, game)
    base = Base(window.width/2, window.height/2, 50, 50, assets, game)
    menuIcon = MenuIcon(0, window.width - 50, 50, 50, assets, game, False)
    # Setting variables
    game.mouseClick = mouseClick
    base.window = window
    # Starting game
    game.toDraw = [mouseClick, base, menuIcon]
    game.mainMenu()

if __name__ == "__main__":
    main()
