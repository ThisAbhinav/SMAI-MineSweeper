from GameManager import GameManager
from rich import print 

# Run DFS 
# gameManager = GameManager(5, 3, "ai", False)
# resultsDFS = gameManager.DFS((0, 0))

# # Run BFS
gameManager = GameManager(5, 3, "ai", False)
resultsBFS = gameManager.BFS((0, 0))

# Run Best Search First
# gameManager = GameManager(5, 3, "ai", False)
# results = gameManager.startPlay((0, 0))

print(resultsBFS)