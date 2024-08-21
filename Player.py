class Player:
    def __init__(self):
        pass 
    def makeMove(self, board: list[list[str]]):
        while True:
            try:
                move = input("Enter your move (i, j) (0 indexed): ")
                move = [int(x) for x in move.split(",")]
                i, j = move
            except:
                print("Invalid Input.")
                continue
            else:
                if board[i][j] != "U":
                    print("Invalid Position.")
                    continue
                else:
                    break
        return move