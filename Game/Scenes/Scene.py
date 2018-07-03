import pygame


class Scene:

    def __init__(self, game):
        self.__game = game
        self.__texts = []
        self.__time = ''
        self.__highscore = []

    def render(self):
        for text in self.__texts:
            self.__game.screen.blit(text[0], text[1])

    def getGame(self):
        return self.__game

    def setTime(self, time):
        self.__time = time

    def getTime(self):
        return self.__time

    def handleEvents(self, events):
        pass

    def displaybox(self, screen):
        pass

    def clearText(self):
        self.__texts = []

    def addText(self, string, x=0, y=0, color=(0, 55, 55), background=(205, 235, 235), size=17):
        font = pygame.font.SysFont("comicsansms", size)
        self.__texts.append([font.render(string, True, color, background), (x, y)])
