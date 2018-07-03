import pygame
from Game.Scenes.Scene import Scene
from Game.Board.Board import Board
from Game.Shared.GameConstants import GameConstants


class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

        self.game = game
        self.run = 0
        self.screen = pygame.display.set_mode()
        self.counter = 0
        self.time = ''
        self.mouse = []
        self.key = 0
        self.score = None

        pygame.time.set_timer(pygame.USEREVENT, 1000)

        self.__playSprite1 = pygame.image.load(GameConstants.SPRITE_CLOCK)
        self.__playSprite2 = pygame.image.load(GameConstants.SPRITE_PLAY)

    def render(self):
        super(PlayingGameScene, self).render()

        self.getGame().screen.blit(self.__playSprite1, (700, 50))
        self.getGame().screen.blit(self.__playSprite2, (650, 350))

        game = self.getGame()

        puzzle = Board.tiles(self)

        if self.key == 0 or len(self.mouse) == 0:
            PlayingGameScene.makeboard(self, game , puzzle)
            self.run += 1

        else:
            key = self.key
            x = self.mouse[0]
            y = self.mouse[1]
            if puzzle[x][y] == 0:
                puzzle[x][y] = key
                PlayingGameScene.makeboard(self, game, puzzle)
            else:
                PlayingGameScene.makeboard(self, game, puzzle)

        self.clearText()

    def setscore(self):
        puzzle = self.unsolve
        score = Board.checkboard(self, puzzle)
        return score

    def storetime(self, time):
        self.time = time

    def gettime(self):
        return self.time

    def displaybox(self, screen):
        pygame.draw.rect(self.screen, (86, 47, 14), [50, 50, 500, 500], 25)

    def makeboard(self, game, puzzle):
        bag = []
        for i in range(0, 9):
            for j in range(0, 9):
                num = puzzle[i][j]
                name = GameConstants.TILE_PATH + '/' + str(num) + '.jpg'
                bag.append(name)

        numbers = []
        for i in range(0, len(bag)):
            board = pygame.image.load(bag[i])
            numbers.append(board)
        n = 0
        for i in range(0, 9):
            for j in range(0, 9):
                game.screen.blit(numbers[n], (75 + GameConstants.TILE_SIZE[0] * i, 75 + GameConstants.TILE_SIZE[1] * j))
                n = n + 1

    def clock(self, text):
        time = ''
        if text >= 60:
            min = int(text/60)
            sec = int(text - min*60)
            time = str(min)+ str(':') + str(sec)
            return time
        else:
            time = '0'+ ':' + str(text)
            return time

    def cursor(self, pos):
        x = int(pos[0])
        y = int(pos[1])
        if (x > 75 and x < 525) and (y > 75 and y <525):
            i = (x - 75) / 50
            j = (y - 75) / 50
            return (int(i), int(j))
        else:
            return pos

    def keyboard(self, key):
        if key == 256 or key == 48:
            flag = 0
        if key == 257 or key == 49:
            flag = 1
        if key == 258 or key == 50:
            flag = 2
        if key == 259 or key == 51:
            flag = 3
        if key == 260 or key == 52:
            flag = 4
        if key == 261 or key == 53:
            flag = 5
        if key == 262 or key == 54:
            flag = 6
        if key == 263 or key == 55:
            flag = 7
        if key == 264 or key == 56:
            flag = 8
        if key == 265 or key == 57:
            flag = 9
        return flag

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()
                Board.newboard()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pressed()
                pos = pygame.mouse.get_pos()
                if mouse[0] == 1:
                    point = PlayingGameScene.cursor(self, pos)
                    self.getGame().playSound(GameConstants.SOUND_CLICK)
                    self.mouse = point

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.getGame().changeScene(GameConstants.MENU_SCENE)

                if event.key == pygame.K_F1:
                    self.getGame().changeScene(GameConstants.MENU_SCENE)

                if event.key == pygame.K_F2:
                    test = PlayingGameScene.setscore(self)
                    if test == True:
                        self.getGame().changeScene(GameConstants.SAVING_SCENE)
                    else:
                        self.getGame().playSound(GameConstants.SOUND_GAMEOVER)
                        self.getGame().changeScene(GameConstants.GAMEOVER_SCENE)

                if event.key == pygame.K_F4:
                    exit()

                key = event.key

                if (key >= 48 and key <= 57) or (key >= 256 and key <= 265):
                    final = PlayingGameScene.keyboard(self, key)

                else:
                    final = 0

                self.key = final

            if event.type == pygame.USEREVENT:
                self.counter += 1
                text = str(self.counter)
                text1 = int(text)

                time = PlayingGameScene.clock(self, text1)
                self.addText(time, x=700, y=175, size=50)
                game =self.getGame()
                game.setTime(time)
