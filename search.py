from GameManager import GameManager
from rich import print 

# gameManager = GameManager(5, 3, "ai")
# play method 1
# results = gameManager.startPlay()
# print(results)
# play method 2 
# while True:
#     result = gameManager.nextMove()
#     if result:
#         print(result)
#         break
# results = gameManager.BFS((0, 0))
# print(results)

gameManager = GameManager(5, 3, "ai")
results = gameManager.DFS((0, 0))
print(results)