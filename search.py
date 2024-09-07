from GameManager import GameManager
from rich import print 
from tqdm import tqdm 
from datetime import datetime

N = 100
SIZE = 6
MINES = 8
# Run DFS
dfsTotalSteps = 0
startTime = datetime.now()
for i in range(N):
    gameManager = GameManager(SIZE, MINES, "ai", False)
    resultsDFS = gameManager.DFS((0, 0))
    dfsTotalSteps += resultsDFS["total_cells_visited"]
endTime = datetime.now()
dfsAvgSteps = dfsTotalSteps / N 
print("Time taken for DFS:", ((endTime-startTime)/100).total_seconds()*1000)


# Run BFS
bfsTotalSteps = 0
startTime = datetime.now()
for i in range(N):
    gameManager = GameManager(SIZE, MINES, "ai", False)
    resultsBFS = gameManager.BFS((0, 0))
    bfsTotalSteps += resultsBFS["total_cells_visited"]
endTime = datetime.now()
bfsAvgSteps = bfsTotalSteps / N 
print("Time taken for BFS:", ((endTime-startTime)/100).total_seconds()*1000)


# Run Best First Search 
bestFirstTotalSteps = 0
startTime = datetime.now()
for i in range(N):
    gameManager = GameManager(SIZE, MINES, "ai", False)
    results = gameManager.startPlay((0, 0))
    bestFirstTotalSteps += results["total_cells_visited"]
endTime = datetime.now()
bestFirstAvgSteps = bestFirstTotalSteps / N
print("Time taken for Best First Search:", ((endTime-startTime)/100).total_seconds()*1000)


print("Average number of steps taken by DFS:", dfsAvgSteps)
print("Average number of steps taken by BFS:", bfsAvgSteps)
print("Average number of steps taken by Best First Search:", bestFirstAvgSteps)


