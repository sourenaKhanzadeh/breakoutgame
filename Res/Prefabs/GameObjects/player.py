from Prefabs.GameObjects.shapes.shapes import *
from setting import *

class Paddle(Rectangle):
    pass


class Ball(Circle):

    def move(self):

        # go east if less than WIDTH
        if self.getX() + self.getRad() + self.dx > WIDTH:
            self.dx = -self.dx
        # go west if less than WIDTH
        elif self.getX() - (self.getRad() - self.dx) < 0:
            self.dx = -self.dx

        # if hit the up screen bounce down
        if self.getY() + self.getRad() < 0:
            self.dy = -self.dy

        # move x axis
        self.incX(self.dx)
        # move y axis
        self.decY(self.dy)


    def collision(self, col:Rectangle):
        if self.getY() - self.getRad() > col.getY()  and col.getX()  == self.getX() + col.getW():
            self.dy = -self.dy

