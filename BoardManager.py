import random


class BoardManager:
    def __init__(self, size: int, noOfMines) -> None:
        self.board = self.generateRandomBoard(size, noOfMines)

    def displayBoard(self) -> None:
        print(self.board)

    def generateRandomBoard(self, size, noOfMines) -> any:
        tempboard = [[0 for i in range(size)] for j in range(size)]
        minelocations = random.choices(range(size * size),k=noOfMines)
        mines = []
        for i in minelocations:
            mines.append((i//size, i%size))
        for i in range(size):
            for j in range(size):
                if (i,j) in minelocations:
                    tempboard[i][j] = Cell(True)
                else:
                    tempboard[i][j] = Cell()
        return tempboard

class Cell:
    def __init__(self, isMine=False) -> None:
        self.isMine = isMine
        self.isVisited = False
    