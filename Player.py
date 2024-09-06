class Player:
    def __init__(self, size: int, noMines: int, verbose: str):
        self.size = size
        self.noMines = noMines
        self.verbose = verbose

    def makeMove(self, board: list[list[str]], startMove: tuple[int]) -> list[int]:
        while True:
            try:
                move = input("Enter your move (i, j) [q for quiting]: ")
                move = [int(x) for x in move.split(",")]
                i, j = move
            except:
                if move == "q":
                    exit()
                print("Invalid Input.")
                continue
            else:
                if board[i][j] != "U":
                    print("Invalid Position.")
                    continue
                else:
                    break
        return move

    def informMine(self, move: list[int]) -> bool:
        return True