from BoardManager import BoardManager

boardManager = BoardManager(3,3)
board = boardManager.getBoard()
for row in board:
    for cell in row:
        print(cell, end=" ")
    print("\n")
boardManager.updateBoard(0,0)
for row in board:
    for cell in row:
        print(cell, end=" ")
    print("\n")