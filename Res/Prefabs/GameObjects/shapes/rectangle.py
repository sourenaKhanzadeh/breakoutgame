from Prefabs.GameObjects.shapes.shapes import *
from setting import *

class Rectangle(Shape):

    def __init__(self, x=WIDTH // 2, y=WIDTH // 2, color=CC.RED, width=0, w=10, h=10):
        super().__init__(x, y, color, width)
        self._w = w
        self._h = h
        self._rect = (self.getX(), self.getY(), self.getW(), self.getH())
        self.dx = self.dy = PS.DEFAULT_XY_VELOCITY

    def draw(self):
        # draw a rectangle
        pygame.draw.rect(screen, self.getColor(), (self.getX(), self.getY(), self.getW(), self.getH()), self.getWidth())

    def update(self):
        super().update()


    # setters and getters
    # SETTERS
    def setW(self, value):
        self._w = value
    def setH(self, value):
        self._h = value
    # GETTERS
    def getW(self):
        return self._w
    def getH(self):
        return self._h
    def getRect(self):
        return self._rect
