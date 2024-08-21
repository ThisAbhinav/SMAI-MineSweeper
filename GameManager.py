from BoardManager import BoardManager, Cell
from Player import Player
class GameManager:
    def __init__(self, boardManager: BoardManager, player: Player) -> None:
        self.boardManager = board
        self.player = player 

    def maskCell(self, cell: Cell) -> str:
        if cell.isMine:
            return "U"
        return str(cell)
    def displayBoard(self, board: List[List[str]]) -> None:
        for i in board:
            for j in i: 
                print(j, end=" ")
            print()
    def maskBoard(self, board: List[List[Cell]]) -> List[List[str]]:
        maskedBoard = [["" for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                maskedBoard[i][j] = maskCell(board[i][j])

    def isMoveValid(self, (i, j): Tuple[int]) -> bool:
        return not realBoard[i][j].isMine

    def play(self) -> bool:
        correctVisits = 0
        totalVisits = boardManager.cells_unvisited
        while correctVisits < totalVisits:
            realBoard = boardManager.getBoard()
            maskedBoard = self.maskBoard(realBoard)
            self.displayBoard(maskedBoard)
            move = player.makeMove(maskedBoard)
            if (self.isMoveValid(move)):
                correctVisits += 1
                boardManager.updateBoard(move)
                continue
            else:
                print("Player hit a mine. Game over.")
                print("Correctly visited cells:", correctVisits)
                exit(1)
        print("All cells visited. Player wins.")
            