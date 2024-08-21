import random


class Cell:
    def __init__(self, isMine: bool = False) -> None:
        self.isMine = isMine
        self.isVisited = False
        self.adjMineCount = 0

    def __str__(self) -> str:
        if self.isMine:
            return "M"
        elif self.isVisited:
            return str(self.adjMineCount)
        else:
            return "U"


class BoardManager:
    def __init__(self, size: int, noOfMines: int) -> None:
        if size * size < noOfMines:
            print("Number of mines are greater than the size of the board")
            exit(1)
        elif size < 1:
            print("Invalid size of the board")
            exit(1)
        self.board = self.generateRandomBoard(size, noOfMines)
        self.cells_unvisited = size * size - noOfMines

    def generateRandomBoard(self, size: int, noOfMines: int) -> list[list[Cell]]:
        tempboard = [[0 for i in range(size)] for j in range(size)]
        minelocations = random.choices(range(size * size), k=noOfMines)
        mines = []
        for i in minelocations:
            mines.append((i // size, i % size))
        for i in range(size):
            for j in range(size):
                if (i, j) in minelocations:
                    tempboard[i][j] = Cell(True)
                else:
                    tempboard[i][j] = Cell()
        return tempboard

    def getBoard(self) -> list[list[Cell]]:
        return self.board

    def updateBoard(self, t: tuple[int]) -> bool:
        i, j = t
        if not self.board[i][j].isMine and not self.board[i][j].isVisited:
            self.board[i][j].isVisited = True
            self.cells_unvisited -= 1
            self.board[i][j].adjMineCount = self.calculateMineCount((i, j))
        else:
            print("Tried to visit a mine or already visited cell")
            exit(1)

    def calculateMineCount(self, t: tuple[int]) -> int:
        i1, j1 = t
        mineCount = 0
        indices = [-1, 0, 1]
        m = len(self.board)
        n = len(self.board[0])
        for i in indices:
            for j in indices:
                if i1 + i in range(0, m) and j1 + j in range(0, n):
                    if self.board[i1 + i][j1 + j].isMine:
                        mineCount += 1
            return mineCount
