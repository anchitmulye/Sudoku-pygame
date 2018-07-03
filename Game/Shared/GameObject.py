
class GameObject:

    def __init__(self, position, size, sprite):
        self.__position = position
        self.__size = size
        self.__sprite = sprite

    def setPosition(self, position):
        self.__position = position

    def getSize(self):
        return self.__size

    def getPosition(self):
        return self.__position

    def getSprits(self):
        return self.__sprite

    def intersects(self, other):
        pass