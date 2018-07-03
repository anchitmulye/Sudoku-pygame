from Game.Shared import GameObject
from Game.Shared import GameConstants
from Game.Puzzle import Puzzle
from Game import Level


class Board(GameObject):

    def __init__(self, position, sprite, game):
        self.__game = game
        self.__tag = 1
        self.solve = []
        self.unsolve = []
        self.run = 0

        super(Board, self).__init__(position, GameConstants.TILE_SIZE, sprite)

    def tiles(self):
        if self.run == 0:
            self.solve = Puzzle.build()
            self.unsolve = Level.unsolve(self.solve)
        return self.unsolve

    def checkboard(self, puzzle):
        n = len(puzzle)
        for row in puzzle:
            i = 1
            while i <= n:
                if i not in row:
                    return False
                i += 1
        j = 0
        transpose = []
        temp_row = []
        while j < n:
            for row in puzzle:
                temp_row.append(row[j])
            transpose.append(temp_row)
            temp_row = []
            j += 1
        for row in transpose:
            i = 1
            while i <= n:
                if i not in row:
                    return False
                i += 1
        return True

    def update_board(self, mouse, key):
        x = mouse[0]
        y = mouse[1]
        self.unsolve[x][y] = key
        return self.unsolve

    def newboard(self):
        self.run = 0

    def getGame(self):
        return self.__game

    def isReplaceable(self):
        return self.__tag <= 0
