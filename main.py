from setting import *

# create the scene environment
levelManager = LevelManager()



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
    screen.fill(CC.BLACK)
    # collisions
    levelManager.collisions()
    # update window
    levelManager.updateScene()

# quit Out Of PyGame
pygame.quit()
