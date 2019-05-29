from Prefabs.GameObjects.shapes.shapes import *
from Prefabs.GameObjects.bricks.bricks import Brick
from setting import *

class Ball(Circle):


    def __init__(self, x=WIDTH // 2, y=WIDTH // 2, color=CC.RED, width=0, rad=10):
        super().__init__(x, y, color, width, rad)

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

        # debug the ball
        self.debug(DEBUG)

        # move x axis
        self.incX(self.dx)
        # move y axis
        self.decY(self.dy)

    def debug(self, active):
        if active:
            if self.getY() > HEIGHT:
                self.setY(0)


    def collision(self, col:Shape):
        # very simple ball collision logic
        if self.getY() - self.dy == col.getY()  and \
                                col.getX() <= self.getX() <= col.getX() + col.getW():
            self.dy = -self.dy

            # if the collided is a brick then change the hit number of the brick
            if len(col) == OO.BRICKS:
                col.hits -= 1


    def __len__(self):
        return OO.BALL
