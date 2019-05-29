from Prefabs.GameObjects.bricks.manager import BrickManagement
from setting import *

class Levels:

    def __init__(self, scene):
        self.brickManager = BrickManagement(scene)

    def level_1(self):
        """
         -----
        |     |
        | 000 |
        |     |
        |  ^  |
         -----
        """
        for bricks in range(0, 30, 10):
            self.brickManager.appendScene(1, x=(WIDTH//2 - PS.DEFAULT_BRICKS_SIZE) + bricks*6, y=200)


    def level_2(self):
        """
         ------
        |      |
        | 1010 |
        |      |
        |  ^   |
         ------
        """
        self.brickManager.appendScene(2, x=WIDTH//2 - PS.DEFAULT_BRICKS_SIZE*2  , y=200)
        self.brickManager.appendScene(1, x=WIDTH//2  - PS.DEFAULT_BRICKS_SIZE, y=200)
        self.brickManager.appendScene(2, x=WIDTH//2  , y=200)
        self.brickManager.appendScene(1, x=WIDTH//2 + PS.DEFAULT_BRICKS_SIZE  , y=200)

    def level_3(self):
        """
         ------
        |  22  |
        | 1010 |
        |  00  |
        |  ^   |
         ------
        """
        self.brickManager.appendScene(3, x=WIDTH//2 - PS.DEFAULT_BRICKS_SIZE  , y=100)
        self.brickManager.appendScene(3, x=WIDTH//2  , y=100)
        self.brickManager.appendScene(2, x=WIDTH // 2 - PS.DEFAULT_BRICKS_SIZE * 2, y=200)
        self.brickManager.appendScene(1, x=WIDTH // 2 - PS.DEFAULT_BRICKS_SIZE, y=200)
        self.brickManager.appendScene(2, x=WIDTH // 2, y=200)
        self.brickManager.appendScene(1, x=WIDTH // 2 + PS.DEFAULT_BRICKS_SIZE, y=200)

