from Game.Scenes.Scene import Scene
from Game.Shared import GameConstants
from Game.Board import Board
import pygame


class GameOverScene(Scene):

    def __init__(self, game):
        super(GameOverScene, self).__init__(game)

        self.__sad1 = pygame.image.load(GameConstants.SPRITE_SAD_1)
        self.__sad2 = pygame.image.load(GameConstants.SPRITE_SAD_2)
        self.__gameover = pygame.image.load(GameConstants.SPRITE_GAMEOVER)

    def render(self):
        super(GameOverScene, self).render()

        self.addText("Try next time! :(", x=350, y=250, size=30)
        self.getGame().screen.blit(self.__gameover, (250, 0))
        self.getGame().screen.blit(self.__sad1, (5, 350))
        self.getGame().screen.blit(self.__sad2, (650, 350))

    def handleEvents(self, events):
        super(GameOverScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    exit()

                if event.key == pygame.K_F4:
                    exit()

                if event.key == pygame.K_F1:
                    Board.newboard(self)
                    self.getGame().changeScene(GameConstants.MENU_SCENE)
