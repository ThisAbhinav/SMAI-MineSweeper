import random as rand
from rich import print
from typing import Optional


class Evidence:

    def __init__(self, cells: set, mines: int):
        self.cells = cells
        self.mines = mines

    def __len__(self):

        return len(self.cells)

    def __str__(self):

        return f"{self.cells} : {self.mines}"


class AIPlayer:

    def __init__(self, size: int, noMines: int, verbose: str):

        self.size = size

        self.noMines = noMines

        self.minesDetected = set()

        self.movesMade = 0

        self.verbose = verbose

    def printSentences(self, sentences: set[Evidence]) -> None:
        for sentence in sentences:

            print(sentence)

    def makeMove(self, board: list[list[str]], startMove: tuple[int]) -> tuple:

        try:

            # if (

            #     input("AI Playing... Press anything to continue... [q for quitting]: ")

            #     == "q"

            # ):

            #     exit(1)

            # # make inference!

            if self.movesMade == 0:

                move = startMove
            else:

                move = self.makeSmartMove(board)

                if not move:

                    move = self.makeRandomMove(board)

                    if self.verbose:

                        print("[blue]No inferences can be made random move taken!")
                else:

                    if self.verbose:

                        print("[green]Inferences made!")

                if self.verbose:

                    print(f"AI chose to move: {move}")

                if board[move[0]][move[1]] != "U":

                    print("Already Visited!")

                    exit(1)

        except Exception as e:

            print(e)

            print("Invalid Position.")

            exit(1)

        self.movesMade += 1

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

        evidences = set()

        for i in range(self.size):

            for j in range(self.size):

                if board[i][j] not in ["U", "T", "0"]:

                    evidence = set()

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

                                evidence.add((i + x, j + y))
                    if len(evidence):

                        evidences.add(Evidence(evidence, int(board[i][j]) - minesCount))

        if self.verbose:

            self.printSentences(evidences)

        safeMoves = set()
        # make inferences from sentences
        InferenceMade = True
        while InferenceMade:
            InferenceMade = False
            for evidence in evidences:
                for otherSentence in evidences:
                    if evidence != otherSentence and evidence.cells.issubset(
                        otherSentence.cells
                    ):
                        otherSentence.cells = otherSentence.cells - evidence.cells
                        otherSentence.mines = otherSentence.mines - evidence.mines
                        InferenceMade = True

            for evidence in evidences.copy():
                if evidence.mines == 0:
                    for cell in evidence.cells:
                        safeMoves.add(cell)
                    evidences.remove(evidence)

                elif evidence.mines == len(evidence):
                    for cell in evidence.cells:
                        self.minesDetected.add(cell)
                    evidences.remove(evidence)

        if self.verbose:
            print("Mines Detected: ", self.minesDetected)
            print("Safe Moves Detected: ", safeMoves)

        # fill safe moves
        if safeMoves:
            return safeMoves.pop()

        # can choose any safe move actually # maybe for optimization we can store this but not required for now.
        else:
            return None

    def informMine(self, move: list[int]) -> bool:
        move = tuple(move)
        self.minesDetected.add(move)
        return True
