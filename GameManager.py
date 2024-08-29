from BoardManager import BoardManager, Cell

from AIPlayer import AIPlayer

from Player import Player


class GameManager:

    def __init__(self, size: int, noMines: int, mode: str = "ai") -> None:

        self.boardManager = BoardManager(size, noMines)
        self.size = size
        self.noMines = noMines
        self.player = AIPlayer(size, noMines) if mode == "ai" else Player(size, noMines)
        print("Game Initialized.")
        print(
            f"Config: \n Grid Size: {self.size}x{self.size} \n No. of Mines: {self.noMines} \n Mode: {mode}"
        )

    def maskCell(self, cell: Cell) -> str:

        if cell.isMine:

            return "U"

        return str(cell)

    def displayMaskedBoard(self, realBoard: list[list[str]]) -> None:

        print("   ", end=" ")

        print(" ".join([str(i) for i in range(self.size)]))
        print("   ", end=" ")

        print(" ".join(["_" for i in range(self.size)]))

        for index, i in enumerate(realBoard):

            print(index, end=" ")
            print("|", end=" ")
            for j in i:

                print(j, end=" ")
            print()

    def displayRealBoard(self, realBoard: list[list[Cell]]):

        print("   ", end=" ")

        print(" ".join([str(i) for i in range(self.size)]))
        print("   ", end=" ")

        print(" ".join(["_" for i in range(self.size)]))

        for index, i in enumerate(realBoard):

            print(index, end=" ")
            print("|", end=" ")

            for j in i:

                print(j, end=" ")
            print()

    def maskBoard(self, board: list[list[Cell]]) -> list[list[str]]:

        maskedBoard = [["" for j in range(self.size)] for i in range(self.size)]

        for i in range(self.size):

            for j in range(self.size):

                maskedBoard[i][j] = self.maskCell(board[i][j])

        return maskedBoard

    def isMoveValid(self, t: tuple[int], realBoard: list[list[Cell]]) -> bool:

        i, j = t

        return not realBoard[i][j].isMine and not realBoard[i][j].isVisited

    def startPlay(self) -> bool:
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
                indices = [-1, 0, 1]
                queue = [move]
                while queue:
                    move = queue.pop(0)
                    if not realBoard[move[0]][move[1]].isVisited:
                        correctVisits += 1
                        self.boardManager.updateBoard(move)
                        realBoard = self.boardManager.getBoard()
                    if realBoard[move[0]][move[1]].adjMineCount == 0:
                        for i in indices:
                            for j in indices:
                                newMove = (move[0] + i, move[1] + j)
                                if (
                                    newMove[0] in range(0, self.size)
                                    and newMove[1] in range(0, self.size)
                                    and not realBoard[newMove[0]][newMove[1]].isVisited
                                ):
                                    print("New move:", newMove)
                                    self.boardManager.updateBoard(newMove)
                                    realBoard = self.boardManager.getBoard()
                                    correctVisits += 1
                                    if (
                                        realBoard[newMove[0]][newMove[1]].adjMineCount
                                        == 0
                                    ):
                                        queue.append(newMove)
                continue
            else:
                print("Player hit a mine. Game over.")
                print("Correctly visited cells:", correctVisits)
                exit(1)
        print("All cells visited. Player wins.")
        self.displayRealBoard(realBoard)
