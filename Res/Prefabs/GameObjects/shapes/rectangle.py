from Prefabs.GameObjects.shapes.shapes import *

class Rectangle(Shape):

    def __init__(self, x=WIDTH // 2, y=WIDTH // 2, color=CC.red, width=0, w=10, h=10):
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

    def move(self):
        # get pressed keys
        keys = pygame.key.get_pressed()
        direct = {
            'r': pygame.K_RIGHT,
            'l': pygame.K_LEFT,
            'u': pygame.K_UP,
            'd': pygame.K_DOWN
        }
        # if movement is allowed
        if self.isMovable():
            # if right key is pressed
            if keys[direct['r']]:
                # x goes right
                self.incX(self.dx)
            # if left key is pressed
            elif keys[direct['l']]:
                # x goes left
                self.decX(self.dx)
            # if down key is pressed
            elif keys[direct['d']]:
                # y goes down
                self.incY(self.dy)
            # if up key is pressed
            elif keys[direct['u']]:
                # y goes up
                self.decY(self.dy)


    def isMovable(self):
        """
        """
        return self.clamp()


    def clamp(self):
        """
        """
        flag = True
        # if passed the eastern window
        if self.getX() + self.getW() > WIDTH:
            # stop movement
            flag = False
            # move a little back
            self.decX(self.dx)
        # if passed the western window
        elif self.getX() < 0:
            # stop movement
            flag = False
            # move a bit forward
            self.incX(self.dx)
        # if passed ratio of the height
        elif self.getY() < int(HEIGHT/PS.DEFAULT_HEIGHT_CLAMP):
            # stop movement
            flag = False
            # move down a bit
            self.incY(self.dy)
        elif self.getY() + self.getH() > HEIGHT:
            # stop movement
            flag = False
            # move up a bit
            self.decY(self.dy)



        return flag

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