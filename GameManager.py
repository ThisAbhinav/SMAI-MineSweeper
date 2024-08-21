from BoardManager import BoardManager, Cell
from Player import Player


class GameManager:
    def __init__(self, size: int, noMines: int) -> None:
        self.boardManager = BoardManager(size, noMines)
        self.player = Player()

    def maskCell(self, cell: Cell) -> str:
        if cell.isMine:
            return "U"
        return str(cell)

    def displayMaskedBoard(self, board: list[list[str]]) -> None:
        for i in board:
            for j in i:
                print(j, end=" ")
            print()

    def displayRealBoard(self, realBoard: list[list[Cell]]):
        for i in realBoard:
            for j in i:
                print(j, end=" ")
            print()
            
    def maskBoard(self, board: list[list[Cell]]) -> list[list[str]]:
        maskedBoard = [["" for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                maskedBoard[i][j] = self.maskCell(board[i][j])
        return maskedBoard

    def isMoveValid(self, t: tuple[int], realBoard: list[list[Cell]]) -> bool:
        i, j = t
        return not realBoard[i][j].isMine



    def play(self) -> bool:
        correctVisits = 0
        totalVisits = self.boardManager.cells_unvisited
        while correctVisits < totalVisits:
            realBoard = self.boardManager.getBoard()
            print("Real Board")
            self.displayRealBoard(realBoard)
            maskedBoard = self.maskBoard(realBoard)
            print("Masked Board")
            self.displayMaskedBoard(maskedBoard)
            move = self.player.makeMove(maskedBoard)
            if self.isMoveValid(move, realBoard):
                correctVisits += 1
                self.boardManager.updateBoard(move)
                continue
            else:
                print("Player hit a mine. Game over.")
                print("Correctly visited cells:", correctVisits)
                exit(1)
        print("All cells visited. Player wins.")
