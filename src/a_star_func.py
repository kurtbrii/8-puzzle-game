from gameplay_functions import winnerCheck
from bfs_dfs import *

def findCellBeingChecked(number_checked):
  newBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
  for i in range(3):
    for j in range(3):
      if newBoard[i][j] == number_checked:
        return i, j

def computeH(initial_board):
  total = 0
  for i in range(3):
    for j in range(3):
      if initial_board[i][j] == 0:
        continue
      correct_row, correct_column = findCellBeingChecked(initial_board[i][j])
      
      distance = abs(i - correct_row) + abs(j - correct_column)
      total += distance

  # print(total)
  return total

def removeMinF(openList):
  # removes the node with the minimum F value
  minF = 0
  for i in range(1, len(openList)):
    if openList[i].f < openList[minF].f:
      minF = i

  return openList.pop(minF)

def findDuplicate(openList, item):
  for duplicate in openList:
    if duplicate.board == item.board:
      return duplicate

def AStar(initial):
  openList = [initial] # same as frontier
  closedList = [] # same as explored

  while(openList):
    bestNode = removeMinF(openList)
    closedList.append(bestNode) 
    print(f"Explored States: {len(closedList)}")
    if (winnerCheck(bestNode.board)):
      print("Goal state achieved!")
      return bestNode

    node_list = Actions(bestNode)
    for item in node_list:
      item.g += 1
      item.h = computeH(item.board)
      item.f = item.g + item.h
      
      duplicate = findDuplicate(openList, item)
      if (not inExploredOrFrontier(item, openList) and not inExploredOrFrontier(item, closedList)) or (inExploredOrFrontier(item, openList) and item.g < duplicate.g):  
        openList.append(item)