import random

class Cell:
    def __init__(self, isMine=False) -> None:
        self.isMine = isMine
        self.isVisited = False
    def __str__(self) -> str:
        if self.isMine:
            return "M"
        elif self.isVisited:
            return "V"
        else:
            return "U"
class BoardManager:
    def __init__(self, size: int, noOfMines) -> None:
        if size*size < noOfMines:
            print("Number of mines are greater than the size of the board")
            exit(1)
        elif size < 1:
            print("Invalid size of the board")
            exit(1)
        self.board = self.generateRandomBoard(size, noOfMines)
        self.cells_unvisited = size*size - noOfMines
        
    def generateRandomBoard(self, size, noOfMines) -> list[list[Cell]]:
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
    
    def getBoard(self):
        return self.board
    
    def updateBoard(self,i,j):
        if not self.board[i][j].isMine and not self.board[i][j].isVisited:
            self.board[i][j].isVisited = True
            self.cells_unvisited -=1
        else:
            print("Tried to visit a mine or already visited cell")
            exit(1)
        

    