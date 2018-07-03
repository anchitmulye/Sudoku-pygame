from Game.Scenes.Scene import Scene
from Game.Shared import *
from Game import Highscore
import pygame


class SavingScene(Scene):

    def __init__(self, game):
        super(SavingScene, self).__init__(game)

        self.__playerName = ""
        self.__highscore =[]
        self.__won = pygame.image.load(GameConstants.SPRITE_WON)

    def render(self):
        self.clearText()
        self.getGame().screen.blit(self.__won, (250, 0))
        self.addText("Congrats", x=355, y=60, size=40)
        self.addText("Save the Game", x=325, y=210, size=30)
        self.addText("Your Name:  ", 75, 300, size=30)
        self.addText(self.__playerName, 250, 300, size = 30)

        super(SavingScene, self).render()

    def handleEvents(self, events):
        super(SavingScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game = self.getGame()
                    score = game.getTime()
                    print(score)
                    # Highscore.add(self,self.__playerName, score)
                    self.getGame().changeScene(GameConstants.HIGHSCORE_SCENE)

                elif event.key >= 65 and event.key <=122:
                    self.__playerName += chr(event.key)

                if event.key == pygame.K_ESCAPE:
                    exit()

                if event.key == pygame.K_F1:
                    self.getGame().changeScene(GameConstants.MENU_SCENE)

                if event.key == pygame.K_F4:
                    exit()
