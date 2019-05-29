from Prefabs.GameObjects.bricks.bricks import Brick
from setting import *

class BrickManagement:
    bricks = []

    def __init__(self, scene):
        self._scene = scene

    def types(self, x, y):
        """
        (BrickManagement) -> dict of {str: Brick}
        return all brick types
        """
        return {
            1:Brick(hits=1, color=CC.YELLOW, w=PS.DEFAULT_BRICKS_SIZE, x=x, y=y),
            2:Brick(hits=2, color=CC.BLUE, w=PS.DEFAULT_BRICKS_SIZE, x=x, y=y),
            3:Brick(hits=3, color=CC.GREEN, w=PS.DEFAULT_BRICKS_SIZE, x=x, y=y),
            4:Brick(hits=4, color=CC.PURPLE, w=PS.DEFAULT_BRICKS_SIZE, x=x, y=y),
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
        BrickManagement.bricks.append(self.getBrick(brick, x, y))
        self.scene += BrickManagement.bricks

    # def update(self):
        # check if brick still exist
        # for brick in BrickManagement.bricks:
            # if brick is destroyed then pop out of the list
            # if brick.destroy():
            #     BrickManagement.bricks.pop()
            #     break

    def __len__(self):
        """
        total size of the bricks
        in the scene
        """
        return len(BrickManagement.bricks)


    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value