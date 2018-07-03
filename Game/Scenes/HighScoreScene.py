from Game.Scenes.Scene import Scene
from Game.Shared.GameConstants import GameConstants
from Game import Highscore

import pygame


class HighScoreScene(Scene):

    def __init__(self, game):
        super(HighScoreScene, self).__init__(game)

        self.__score1 = pygame.image.load(GameConstants.SPRITE_PRIZE)
        self.__score2 = pygame.image.load(GameConstants.SPRITE_STAND)
        self.__highscore = pygame.image.load(GameConstants.SPRITE_HIGHSCORE)

    def render(self):
        super(HighScoreScene, self).render()
        self.getGame().screen.blit(self.__highscore, (250, 0))
        self.getGame().screen.blit(self.__score2, (450, 50))
        self.getGame().screen.blit(self.__score1, (5, 250))

        highscore = Highscore()

        x = 450
        y = 250
        for score in highscore.getScores():
            self.addText(score[0], x, y, size=25)
            self.addText(str(score[1]), x+200, y, size=25)
            y +=30

    def handleEvents(self, events):
        super(HighScoreScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

                if event.key == pygame.K_F4:
                    exit()

                if event.key == pygame.K_F1:
                    self.getGame().changeScene(GameConstants.MENU_SCENE)
