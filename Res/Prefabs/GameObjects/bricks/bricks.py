from Prefabs.GameObjects.shapes.shapes import *
from setting import OO

class Brick(Rectangle):
    """
    Brick
    """
    def __init__(self, x=WIDTH // 2, y=WIDTH // 2, color=CC.red, width=0, w=10, h=10, hits = 1):
        super().__init__(x, y, color, width, w, h)
        self._hits = hits

    def isMovable(self):
        """
        (Brick) -> bool
        Brick is not movable
        """
        return False

    def move(self):
        return self.isMovable()

    def update(self):
        """
        Bricks are static
        and can be destroyed
        """
        if not self.destroy():
            self.draw()
        else:
            # destroy the gameObject
            self.setX(PS.VOID)
            self.setY(PS.VOID)
            del self
            self = None


    def destroy(self):
        # destroy the gameObject
        if self.hits <= 0:
            return True
        return False

    def __len__(self):
        """
        Order of priority
        """
        return OO.BRICKS

    @property
    def hits(self):
        return self._hits

    @hits.setter
    def hits(self, value):
        self._hits = value



