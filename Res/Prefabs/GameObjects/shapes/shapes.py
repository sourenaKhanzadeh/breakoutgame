from abc import abstractmethod, ABC
from setting import *


class Shape(ABC):
    """
    ABSTRACTION OF ALL SHAPES
    RECTANGLE
    """
    @abstractmethod
    def __init__(self, x=WIDTH//2, y=WIDTH//2, color=CC.RED, width=0):
        self._x = x
        self._y = y
        self._color = color
        self._width = width

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def update(self):
        # draw the object
        self.draw()
        # move the object
        self.move()


    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def isMovable(self):
        pass

    # increments
    def incX(self, value):
        self._x += value

    def incY(self, value):
        self._y += value

    # decrements
    def decX(self, value):
        self._x -= value

    def decY(self, value):
        self._y -= value

    # setters and getters
    # SETTERS
    def setX(self, value):
        self._x = value

    def setY(self, value):
        self._y = value

    def setColor(self, value):
        self._color = value

    def setWidth(self, value):
        self._width = value

    # GETTERS
    def getX(self):
       return self._x

    def getY(self):
        return self._y

    def getColor(self):
       return self._color

    def getWidth(self):
        return self._width


#import all shapes
from Prefabs.GameObjects.shapes.rectangle import Rectangle
from Prefabs.GameObjects.shapes.circle import Circle
