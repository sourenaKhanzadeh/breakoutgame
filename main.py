from setting import *

# create the scene environment
scene = []
brickManager = BrickManagement(scene)

def collisions():
    # ball collisions
    for colliders in range(1, len(scene)):
        scene[0].collision(scene[colliders])

def initializeScene():
    """
    """
    scene.append(Ball(y=100))
    scene.append(Paddle(w=50))
    brickManager.appendScene(1, y=100)
    brickManager.appendScene(2, y=200)
    brickManager.appendScene(3, y=300)
    brickManager.appendScene(4, y=400)



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
    screen.fill(CC.WHITE)
    # collisions
    collisions()
    # update window
    updateScene()

# quit Out Of PyGame
pygame.quit()
