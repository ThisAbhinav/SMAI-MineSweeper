import random as rand

from typing import Optional


class Sentence:
    def __init__(self, cells: set, mines: int):
        self.cells = cells
        self.mines = mines

    def __len__(self):
        return len(self.cells)

    def __str__(self):
        return f"{self.cells} : {self.mines}"


class AIPlayer:
    def __init__(self, size: int, noMines: int):
        self.size = size
        self.noMines = noMines
        self.minesDetected = set()

    def printSentences(self, sentences: set[Sentence]) -> None:
        for sentence in sentences:
            print(sentence)

    def makeMove(self, board: list[list[str]]) -> tuple:
        try:
            # if (
            #     input("AI Playing... Press anything to continue... [q for quitting]: ")
            #     == "q"
            # ):
            #     exit(1)
            # # make inference!
            move = self.makeSmartMove(board)

            if not move:
                move = self.makeRandomMove(board)
                print("No inferences can be made random move taken!")
            else:
                print("Inferences made!")
            print(f"AI chose to move: {move}")
            if board[move[0]][move[1]] != "U":
                print("Already Visited!")
                exit(1)
        except Exception as e:
            print(e)
            print("Invalid Position.")
            exit(1)
        return move

    def makeRandomMove(self, board: list[list[str]]) -> tuple:
        while True:
            move = (
                rand.choice([*range(len(board))]),
                rand.choice([*range(len(board))]),
            )
            if board[move[0]][move[1]] == "U" and move not in self.minesDetected:
                break
        return move

    def makeSmartMove(self, board: list[list[str]]) -> tuple | None:

        indices = [-1, 0, 1]
        sentences = set()
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] != "U" and board[i][j] != "0":
                    sentence = set()
                    minesCount = 0
                    for x in indices:
                        for y in indices:
                            if (x == 0 and y == 0) or (
                                i + x < 0
                                or i + x >= self.size
                                or j + y < 0
                                or j + y >= self.size
                            ):
                                continue
                            elif (i + x, j + y) in self.minesDetected:
                                minesCount += 1
                                continue
                            elif board[i + x][j + y] == "U":
                                sentence.add((i + x, j + y))
                    if len(sentence):
                        sentences.add(Sentence(sentence, int(board[i][j]) - minesCount))
        self.printSentences(sentences)
        safeMoves = set()
        # make inferences from sentences
        InferenceMade = True
        while InferenceMade:
            InferenceMade = False
            for sentence in sentences:
                for otherSentence in sentences:
                    if sentence != otherSentence and sentence.cells.issubset(
                        otherSentence.cells
                    ):
                        otherSentence.cells = otherSentence.cells - sentence.cells
                        otherSentence.mines = otherSentence.mines - sentence.mines
                        InferenceMade = True
            for sentence in sentences.copy():
                if sentence.mines == 0:
                    for cell in sentence.cells:
                        safeMoves.add(cell)
                    sentences.remove(sentence)
                elif sentence.mines == len(sentence):
                    for cell in sentence.cells:
                        self.minesDetected.add(cell)
                    sentences.remove(sentence)
        print("Mines Detected: ", self.minesDetected)
        print("Safe Moves Detected: ", safeMoves)
        # fill safe moves
        if safeMoves:
            return safeMoves.pop()
        # can choose any safe move actually # maybe for optimization we can store this but not required for now.
        else:
            return None
