class Player:
    def __init__(self):
        pass

    def makeMove(self, board: list[list[str]]):
        while True:
            try:
                move = input("Enter your move (i, j) [q for quiting]: ")
                move = [int(x) for x in move.split(",")]
                i, j = move
            except:
                if move == 'q':
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
