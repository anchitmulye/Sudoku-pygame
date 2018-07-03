import random


class Level:
    def unsolve(puzzle):
        unsolve = puzzle
        d = random.randint(20, 35)

        for i in range(0, d):
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            puzzle[x][y] = 0
        return puzzle
