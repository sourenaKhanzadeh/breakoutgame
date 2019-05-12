from breakoutgame.Res.Prefabs.GameObjects.player import Paddle, Ball
from breakoutgame.setting import *

# create the scene environment
scene = []

def initializeScene():
    """
    """
    scene.append(Paddle(w=50))
    scene.append(Ball())


initializeScene()

def updateScene():
    """
    """
    # get all gameObjects in the scene
    for gameObject in scene:
        # update each
        gameObject.update()

    # update the display
    pygame.display.update()


run = True

# While game is running
while run:
    # get all PyGame events
    for event in pygame.event.get():
        # if pressed on quit
        if event.type == pygame.QUIT:
            # then quit out of the window
            run = False

    # fill the window color
    screen.fill(CC.white)
    # update window
    updateScene()

# quit Out Of PyGame
pygame.quit()