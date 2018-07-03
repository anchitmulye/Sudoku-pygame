from Game.Scenes.Scene import Scene
from Game.Shared import *
import pygame


class Instructions(Scene):

    def __init__(self, game):
        super(Instructions, self).__init__(game)

        self.addText("NAVIGATION: ", x=5, y=100, size=30)
        self.addText("Press F1- to move back to main menu from any screen.", x=5, y=135, size=15)
        self.addText("Press F4 or ESC- to quit from any screen.", x=5, y=155, size=15)
        self.addText("GAME PLAY: ", x=5, y=185, size=30)
        self.addText("To pause the game press F1 and to resume press F1. To insert a number on board press the respective number", x=5, y=220, size=15)
        self.addText("key on keyboard and then click the mouse pointer where the number is to be placed. Press F2 to Submit.", x=5, y=240, size=15)
        self.addText("Press F4 to Quit. If your board is 100% correct then only you can save the game.", x=5, y=260, size=15)
        self.addText("HOW TO SAVE THE GAME: ", x=5, y=290, size=30)
        self.addText("Enter the name of the player. Then press Enter key. Respective name and time of current game will be", x=5, y=325, size=15)
        self.addText("automatically saved in the database. Top 5 highscores will be displayed then.", x=5, y=345, size=15)
        self.addText("HIGH-SCORE: ", x=5, y=375, size=30)
        self.addText("This section loads top 10 highscores from database and display player name with time.", x=5, y=410, size=15)
        self.addText("The highscore are displayed in ascending order of time.", x=5, y=430, size=15)
        self.addText("CREDITS: ", x=5, y=460, size=30)
        self.addText("The game is developed by ANCHIT MULYE using pygame.", x=5, y= 495, size=15)
        self.addText("The graphics and sounds used in this game are designed by ANCHIT MULYE.", x=5, y= 515, size=15)
        self.addText("The game is branded by ARTELLIGENCE MACHINE.", x=5, y= 535, size=15)

        self.__instruction = pygame.image.load(GameConstants.SPRITE_INSTRUCTION)

    def render(self):
        super(Instructions, self).render()

        self.getGame().screen.blit(self.__instruction, (250, 0))

    def handleEvents(self, events):
        super(Instructions, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

                if event.key == pygame.K_F1:
                    self.getGame().changeScene(GameConstants.MENU_SCENE)

                if event.key == pygame.K_F4:
                    exit()
