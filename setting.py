import pygame
import Res.Constants.color as CC
import Res.Constants.physics as PS


# WINDOW CONFIGURATION
WIDTH  = 500
HEIGHT = 600

def setWindow(title):
    screen  = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(title)
    return screen


# set the window
screen = setWindow("Break Out Game")
