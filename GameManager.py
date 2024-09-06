from BoardManager import BoardManager, Cell
import streamlit as st
from AIPlayer import AIPlayer
from rich import print
from Player import Player
import streamlit as st
from typing import Optional


class GameManager:

    def __init__(self, size: int, noMines: int, mode: str = "ai") -> None:

        self.boardManager = BoardManager(size, noMines)
        self.size = size
        self.noMines = noMines
        self.player = AIPlayer(size, noMines) if mode == "ai" else Player(size, noMines)
        self.correctVisits = 0
        self.minesHit = 0
        print("Game Initialized.")
        print(
            f"Config: \n Grid Size: {self.size}x{self.size} \n No. of Mines: {self.noMines} \n Mode: {mode.upper()}"
        )

    def maskCell(self, cell: Cell) -> str:

        if cell.isMine and not cell.isVisitedMine:

            return "U"

        return str(cell)

    def displayBoard(self, realBoard: list[list[str]]) -> None:
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

    def isUnvisitedSafe(self, t: tuple[int], realBoard: list[list[Cell]]) -> bool:

        i, j = t

        return not realBoard[i][j].isVisited and not realBoard[i][j].isMine

    def isMoveMine(self, t: tuple[int], realBoard: list[list[Cell]]) -> bool:
        i, j = t 
        return realBoard[i][j].isMine and not realBoard[i][j].isVisited

    def displayWinMsg(self):
        print("All cells visited. Player wins.")
        self.displayBoard(self.boardManager.getBoard())
        print("Number of mines hit:", self.minesHit)

    def startPlay(self) -> dict:
        totalVisits = self.boardManager.cells_unvisited
        while self.correctVisits < totalVisits:
            self.nextMove()
        self.displayWinMsg()
        results = self.getResults()
        return results
    
    def getResults(self) -> dict:
        safeCellsVisited = self.size**2 - self.noMines
        totalCellsVisited = self.correctVisits + self.minesHit
        
        results = {
            "total_safe_cells": self.size**2 - self.noMines,
            "safe_cells_visited": self.correctVisits,
            "mines_hit": self.minesHit,
            "total_mines": self.noMines,
            "total_cells_visited": totalCellsVisited,
        }

        results["victory"] = results["total_safe_cells"] == results["safe_cells_visited"]

        return results

    def nextMove(self) -> Optional[dict]:
        print("Next Move")
        if self.boardManager.cells_unvisited == 0:
            self.displayWinMsg()
            results = self.getResults()
            return results
        else:
            realBoard = self.boardManager.getBoard()
            # print("Real Board")
            # self.displayBoard(realBoard)
            maskedBoard = self.maskBoard(realBoard)
            # st.table(maskedBoard)
            # st.table(maskedBoard)
            print("Masked Board")
            self.displayBoard(maskedBoard)
            move = self.player.makeMove(maskedBoard)
            if self.isUnvisitedSafe(move, realBoard):
                indices = [-1, 0, 1]
                queue = [move]
                while queue:
                    move = queue.pop(0)
                    if not realBoard[move[0]][move[1]].isVisited:
                        self.correctVisits += 1
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
                                    self.correctVisits += 1
                                    if (
                                        realBoard[newMove[0]][newMove[1]].adjMineCount
                                        == 0
                                    ):
                                        queue.append(newMove)
                    continue
            elif self.isMoveMine(move, realBoard):
                print("[red]Player hit a mine. The game must go on!")
                self.boardManager.markVisitedMine(move)
                self.minesHit += 1
                self.player.informMine(move)
                
                # exit(1)
            else:
                print("Player hit an invalid move. Game over.")
                print("Correctly visited cells:", correctVisits)
                print("Number of mines hit:", self.minesHit)
                exit(1)
            return None

    def getBoard(self):
        realBoard =  self.boardManager.getBoard()
        maskedBoard = self.maskBoard(realBoard)
        return maskedBoard

    def BFS(self, startMove: tuple[int]) -> dict:
        # does BFS on the board
        queue = [startMove]
        indices = [-1, 0, 1]
        visited = [[False]*self.size for i in range(self.size)]
        visited[startMove[0]][startMove[1]] = True
        while queue:
            print("[green]Number of elements in queue:", len(queue))
            realBoard = self.boardManager.getBoard()
            currentMove = queue.pop(0)
            x, y = currentMove
            print("[blue]Taking Move:", currentMove)
            if self.isUnvisitedSafe(currentMove, realBoard):
                self.boardManager.updateBoard(currentMove)
                self.correctVisits += 1
                for i in indices:
                    for j in indices:
                        newMove = (x + i, y + j)
                        i1, j1 = newMove
                        if i1 in range(0, self.size) and j1 in range(0, self.size) and not visited[i1][j1]:
                            queue.append(newMove)
                            visited[i1][j1] = True
            elif self.isMoveMine(currentMove, realBoard):
                self.boardManager.markVisitedMine(currentMove)
                self.minesHit += 1
                # not appending to queue
            
                        
            realBoard = self.boardManager.getBoard()
            maskedBoard = self.maskBoard(realBoard)
            print("Masked Board:")
            self.displayBoard(maskedBoard)
        print("[red]Queue is empty. BFS over.")
        results = self.getResults()
        return results

    def DFS(self, startMove: tuple[int]) -> bool:
        stack = [startMove]
        indices = [-1, 0, 1]
        visited = [[False]*self.size for i in range(self.size)]
        visited[startMove[0]][startMove[1]] = True
        while stack:
            print("[green]Number of elements in stack:", len(stack))
            realBoard = self.boardManager.getBoard()
            currentMove = stack.pop()
            x, y = currentMove
            print("[blue]Taking Move:", currentMove)
            if self.isUnvisitedSafe(currentMove, realBoard):
                self.boardManager.updateBoard(currentMove)
                self.correctVisits += 1
                for i in indices:
                    for j in indices:
                        newMove = (x + i, y + j)
                        i1, j1 = newMove
                        if i1 in range(0, self.size) and j1 in range(0, self.size) and not visited[i1][j1]:
                            stack.append(newMove)
                            visited[i1][j1] = True
            elif self.isMoveMine(currentMove, realBoard):
                self.boardManager.markVisitedMine(currentMove)
                self.minesHit += 1
                # not appending to stack
            
                        
            realBoard = self.boardManager.getBoard()
            maskedBoard = self.maskBoard(realBoard)
            print("Masked Board:")
            self.displayBoard(maskedBoard)
        print("[red]Stack is empty. BFS over.")
        results = self.getResults()
        return results
