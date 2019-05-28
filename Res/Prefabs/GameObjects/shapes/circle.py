from Prefabs.GameObjects.shapes.shapes import *


class Circle(Shape):
    def __init__(self, x=WIDTH // 2, y=WIDTH // 2, color=CC.red, width=0, rad=10):
        """
        """
        super().__init__(x, y, color, width)
        self._pos = (self.getX(), self.getY())
        self._rad = rad
        self.dx = self.dy = PS.DEFAULT_XY_VELOCITY

    def draw(self):
        """
        """
        # draw a circle
        pygame.draw.circle(screen, self.getColor(), (self.getX(), self.getY()),self.getRad(), self.getWidth())

    def isMovable(self):
        """
        """
        flag = True

        return flag

    def move(self):
        """
        """
        super().move()




    def update(self):
        """
        """
        super().update()


    # getters and setters
    # SETTERS
    def setPos(self, value):
        self._pos = value
    def setRad(self, value):
        self._rad = value

    # GETTERS
    def getPos(self):
        return self._pos
    def getRad(self):
        return self._rad
