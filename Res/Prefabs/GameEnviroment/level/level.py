from Prefabs.GameObjects.bricks.manager import BrickManagement

class Levels:

    def __init__(self, scene):
        self.brickManager = BrickManagement(scene)

    def level_1(self):
        for bricks in range(1, 50, 10):
            self.brickManager.appendScene(1, x=bricks*10, y=200)


