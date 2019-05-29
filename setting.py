import pygame
import Res.Constants.color as CC
import Res.Constants.physics as PS
import Res.Constants.objectOrder as OO


# WINDOW CONFIGURATION
WIDTH  = 500
HEIGHT = 600

def setWindow(title):
    screen  = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(title)
    return screen


# set the window
screen = setWindow("Break Out Game")


from Res.Prefabs.GameObjects.player.player import Paddle
from Res.Prefabs.GameObjects.player.ball import Ball
from Res.Prefabs.GameObjects.bricks.manager import BrickManagement