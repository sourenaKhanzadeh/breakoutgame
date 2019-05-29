from setting import *
from Prefabs.GameEnviroment.level.level import Levels

class LevelManager:

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
        self.scene.append(Paddle(w=50))
        self.level.level_1()


    def collisions(self):
        """
        COLLISION SYSTEM
        """
        # BALL COLLISION
        for colliders in range(1, len(self.scene)):
            self.scene[0].collision(self.scene[colliders])


    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
