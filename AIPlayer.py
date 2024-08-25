import random as rand

from typing import Optional

class Sentence:
    def __init__(self, cells:set, mines:int):
        self.cells = cells
        self.mines = mines
    # overload operator here for sexy sexy union and difference operations
        
    def __str__(self):
        return f"{self.cells} : {self.mines}"


class AIPlayer:
    def __init__(self, size: int, noMines: int):
        self.size = size
        self.noMines = noMines
        
    def printSentences(self,sentences:list[Sentence])->None:
        for sentence in sentences:
            print(sentence) 
    
    def makeMove(self, board: list[list[str]])->tuple:
        try:
            if (
                input("AI Playing... Press anything to continue... [q for quitting]: ")
                == "q"
            ):
                exit(1)
            # make inference!
            move = self.makeSmartMove(board)
            
            if not move: 
                move = self.makeRandomMove(board)
                print("No inferences can be made random move taken!")
            print(f"AI chose to move: {move}")
            if board[move[0]][move[1]] != "U":
                print("Already Visited!")
                exit(1)
        except Exception as e:
            print(e)
            print("Invalid Position.")
            exit(1)
        return move

    def makeRandomMove(self, board: list[list[str]])->tuple:
        while True:
            move = (
                rand.choice([*range(len(board))]),
                rand.choice([*range(len(board))]),
            )
            if board[move[0]][move[1]] == "U":
                break
        return move
    
    def makeSmartMove(self, board: list[list[str]])->Optional[tuple]:
        # if self.sentences == []:
        #     return None
        indices = [-1,0,1]
        # create sentences from the current board
        sentences = []
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] != "U" and board[i][j] != '0':
                    sentence = set()
                    for x in indices:
                        for y in indices:
                            if (x == 0 and y == 0) or (i+x < 0 or i+x >= self.size or j+y < 0 or j+y >= self.size):
                                continue
                            sentence.add((i+x,j+y))
                    sentences.append(Sentence(sentence,board[i][j]))
        self.printSentences(sentences)
        safeMoves = []
        # make inferences from sentences
        # fill safe moves
        if safeMoves:
            return safeMoves[0] # can choose any safe move actually # maybe for optimization we can store this but not required for now. 
        else:
            return None
