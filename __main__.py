import pygame
import logging

from game import Game
from window import Window
from assets import Assets

def main():
    # Initialise pygame
    pygame.init()
    # Start logging
    log()
    # Creating instances
    window = Window()
    assets = Assets(window)
    game = Game(window, assets)
    # Starting game
    game.mainMenu()

def log():
    logging.basicConfig(filename = 'DebuggingFile.txt', level = logging.INFO)
    logging.info("\n\n=====> New Game <=====\n\n")

if __name__ == "__main__":
    main()
