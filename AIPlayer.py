import random as rand
class AIPlayer:
    def __init__(self):
        self.sentences = []

    def makeMove(self, board: list[list[str]]):
        try:
            if input("AI Playing... Press anything to continue... [q for quitting]: ") == 'q':
                exit(1)
            move = (0,0)
            if len(self.sentences) == 0:
                move = self.makeRandomMove(board)
                self.sentences.append(move)
            print(f"AI chose to move: {move}")
            if board[move[0]][move[1]] != "U":
                print("Already Visited!")
                exit(1)
        except Exception as e:
            print(e)
            print("Invalid Position.")
            exit(1)
        return move

    def makeRandomMove(self, board: list[list[str]]):
        while True:
            move = (rand.choice([*range(len(board))]), rand.choice([*range(len(board))]))
            if board[move[0]][move[1]] == "U":
                break
        return move