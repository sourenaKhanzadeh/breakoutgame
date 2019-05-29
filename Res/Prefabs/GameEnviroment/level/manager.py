from setting import *
from Prefabs.GameEnviroment.level.level import Levels

class LevelManager:
    level = 0
    def __init__(self):
        self._scene = []
        self.brickManager = BrickManagement(self.scene)
        self.level = Levels(self.scene)
        # awake objects
        self.awake()


    def awake(self):
        """
        Awake all game objects
        """
        self.scene.append(Ball(y=100))
        self.scene.append(Paddle(w=PS.DEFAULT_BRICKS_SIZE))
        print(LevelManager.level)
        # levels
        if LevelManager.level == 0:
            self.level.level_1()
        elif LevelManager.level == 1:
            self.level.level_2()
        else:
            self.level.level_3()

    def collisions(self):
        """
        COLLISION SYSTEM
        """
        # BALL COLLISION
        for colliders in range(1, len(self.scene)):
            self.scene[0].collision(self.scene[colliders])

    def nextLevel(self):
        """
        Go to the next level
        if all bricks are destroyed
        """
        if len(self.brickManager) == 0:
            LevelManager.level += 1
            self.scene = []
            self.awake()

    def update(self):
        self.nextLevel()

    def updateScene(self):
        """
        """

        # update level
        self.update()
        # get all gameObjects in the scene
        for gameObject in self.scene:
            # update each
            gameObject.update()

        # update the display
        pygame.display.update()
        # update brick manager
        # self.brickManager.update()

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
