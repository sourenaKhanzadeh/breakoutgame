from Res.Prefabs.GameObjects.player import *
from setting import *

# create the scene environment
scene = []


def collisions():
    scene[0].collision(scene[1])

def initializeScene():
    """
    """
    scene.append(Ball(y=100))
    scene.append(Paddle(w=50))



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
    # delay the game a bit
    pygame.time.delay(PS.DEFAULT_TIME_DELAY)

    # get all PyGame events
    for event in pygame.event.get():
        # if pressed on quit
        if event.type == pygame.QUIT:
            # then quit out of the window
            run = False

    # fill the window color
    screen.fill(CC.white)
    # collisions
    collisions()
    # update window
    updateScene()

# quit Out Of PyGame
pygame.quit()
