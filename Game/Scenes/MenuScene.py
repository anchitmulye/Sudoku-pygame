import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import *


class MenuScene(Scene):

    def __init__(self, game):
        super(MenuScene, self).__init__(game)

        self.addText("F1 - Start Game", x=620, y=200, size=35)
        self.addText("F2 - High Scores", x=620, y=300, size=35)
        self.addText("F3 - Instructions", x=620, y=400, size=35)
        self.addText("F4 - Quit", x=620, y=500, size=35)

        self.__menuSprite1 = pygame.image.load(GameConstants.SPRITE_MENU)
        self.__menuSprite2 = pygame.image.load(GameConstants.SPRITE_MAINMENU)

    def render(self):
        super(MenuScene, self).render()

        self.getGame().screen.blit(self.__menuSprite1, (0, 0))
        self.getGame().screen.blit(self.__menuSprite2, (600, 0))

    def handleEvents(self, events):
        super(MenuScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

                if event.key == pygame.K_F1:
                    self.getGame().playSound(GameConstants.SOUND_SCREEN)
                    self.getGame().changeScene(GameConstants.PLAYING_SCENE)

                if event.key == pygame.K_F2:
                    self.getGame().changeScene(GameConstants.HIGHSCORE_SCENE)

                if event.key == pygame.K_F3:
                    self.getGame().changeScene(GameConstants.INSTRUCTION)

                if event.key == pygame.K_F4:
                    exit()
