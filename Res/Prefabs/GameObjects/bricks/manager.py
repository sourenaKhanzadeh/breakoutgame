from Prefabs.GameObjects.bricks.bricks import Brick
from setting import *

class BrickManagement:


    def __init__(self, scene):
        self._total_bricks = 0
        self._scene = scene

    def types(self, x, y):
        """
        (BrickManagement) -> dict of {str: Brick}
        return all brick types
        """
        return {
            1:Brick(hits=1, color=CC.YELLOW, w=50, x=x, y=y),
            2:Brick(hits=2, color=CC.BLUE, w=50, x=x, y=y),
            3:Brick(hits=3, color=CC.GREEN, w=50, x=x, y=y),
            4:Brick(hits=4, color=CC.PURPLE, w=50, x=x, y=y),
        }


    def getBrick(self, type, x, y):
        """
        (BrickManagement, str) -> Brick
        Get the brick type
        """
        return self.types(x, y)[type]

    def appendScene(self, brick, x=WIDTH//2, y=HEIGHT//2):
        """
        (Brick) -> None
        append the brick to the
        scene
        """
        self.total_bricks += 1
        self.scene.append(self.getBrick(brick, x, y))



    @property
    def total_bricks(self):
        return self._total_bricks

    @total_bricks.setter
    def total_bricks(self, value):
        self._total_bricks = value

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value