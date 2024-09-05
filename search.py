from GameManager import GameManager
from rich import print 

gameManager = GameManager(5, 4, "ai")
# results = gameManager.startPlay()
while True:
    result = gameManager.nextMove()
    if result:
        print(result)
        break