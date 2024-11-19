import time

import pygame

from gameplay_functions import printArray, swapCells, winnerCheck


class Node:
    def __init__(self, board, empty_row, empty_column, action, parent):
        self.board = board
        self.empty_row = empty_row
        self.empty_column = empty_column
        self.action = action
        self.parent = parent


class Button:
    def __init__(self, x_pos, y_pos, name):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.name = name

    def drawTile(self, screen, TILE_COLOR, FONT_COLOR):
        pygame.draw.rect(screen, TILE_COLOR, [self.x_pos, self.y_pos, 100, 30], 0, 15)

        font = pygame.font.Font("freesansbold.ttf", 15)
        screen.blit(
            font.render(self.name, True, FONT_COLOR),
            [(self.x_pos + self.x_pos + 40) / 2, (self.y_pos + self.y_pos + 15) / 2],
        )

    def isClicked(self, x, y):
        time.sleep(0.05)
        return x in range(self.x_pos, self.x_pos + 100) and y in range(
            self.y_pos, self.y_pos + 30
        )


def findPath(currentState):
    actions_string_list = []
    while currentState.parent:
        actions_string_list.insert(0, currentState.action)
        currentState = currentState.parent

    return actions_string_list, len(actions_string_list)


def findEmpty(terminal_list):
    for i in range(3):
        for j in range(3):
            if terminal_list[i][j] == 0:
                return i, j


def copyBoard(currentStateBoard):
    new_board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(currentStateBoard[i][j])
        new_board.append(row)

    return new_board


def swapping(currentState, row_index, col_index, action_string):
    new_board = copyBoard(currentState.board)
    i, j = findEmpty(new_board)
    print("=======")
    print("PARENT")
    printArray(new_board)
    print("=======")

    try:
        if (
            i + row_index >= 0 and j + col_index >= 0
        ):  # the row and column being checked must be greater than 0
            new_node_board = swapCells(
                new_board, i, j, i + row_index, j + col_index
            )  # swap the two cells
            i, j = findEmpty(new_board)
            newNode = Node(
                new_node_board, i, j, action_string, currentState
            )  # instantiate Node

            print("------------------")
            printArray(newNode.board)
            print(f"Parent Node: {newNode.parent}")
            print(
                f"Empty Cell Coordinate: ({newNode.empty_row}, {newNode.empty_column})"
            )
            print("------------------")

            return newNode
        return -1
    except IndexError:
        return -1


def addToActions(newNode, action_list):
    if newNode != -1:
        action_list.append(newNode)

    return action_list


# gets all possible actions and put all of it into action_list
def Actions(currentState):
    action_list = []

    newNode = swapping(currentState, -1, 0, "U")
    action_list = addToActions(newNode, action_list)

    newNode = swapping(currentState, 0, +1, "R")
    action_list = addToActions(newNode, action_list)

    newNode = swapping(currentState, 1, 0, "D")
    action_list = addToActions(newNode, action_list)

    newNode = swapping(currentState, 0, -1, "L")
    action_list = addToActions(newNode, action_list)

    print(len(action_list))
    return action_list


def inExploredOrFrontier(node, explored):
    for item in explored:
        if node.board == item.board:
            return True
    return False


def BFS_DFS(initial, index_popped):
    frontier = [initial]
    explored = []

    while frontier:
        currentState = frontier.pop(
            index_popped
        )  # depending on the data structure used (BFS/DFS)
        printArray(currentState.board)
        explored.append(currentState)
        print(f"Explored States: {len(explored)}")
        if winnerCheck(currentState.board):
            print("Goal state achieved!")
            return currentState
        else:
            # gets all the elements of the list then loop to check if it already exists in explored or frontier
            nodes_list = Actions(currentState)
            for item in nodes_list:
                if not inExploredOrFrontier(
                    item, explored
                ) and not inExploredOrFrontier(item, frontier):
                    frontier.append(item)


def findEmptyCell(terminal_list):
    for i in range(3):
        for j in range(3):
            if terminal_list[i][j] == 0:  # the neighboring cell is 0
                print(f"empty cell found: ({i}, {j})")
                return i, j


def fileWrite(actions_list):
    with open("src/puzzle.out", "w") as f:
        f.writelines([f"{x} " for x in actions_list])


def readOutputFile():
    with open("src/puzzle.out", "r") as file:
        data = file.read()
        return data


def clickedBfsDfs(screen, dfs, bfs, bfs_pink, dfs_pink, bfs_black, dfs_black):
    bfs.drawTile(screen, bfs_pink, bfs_black)
    dfs.drawTile(screen, dfs_pink, dfs_black)


def printTilesOnClick(
    tiles_list,
    terminal_list,
    screen,
    PINK_100,
    BLACK,
    TILE_COLOR,
    FONT_COLOR,
    row_index,
    col_index,
):
    for i in range(3):
        for j in range(3):
            if terminal_list[i][j] != 0:
                tile = tiles_list[i][j]
                if i == row_index and j == col_index:
                    tile.drawTile(screen, terminal_list, i, j, TILE_COLOR, FONT_COLOR)
                else:
                    tile.drawTile(screen, terminal_list, i, j, PINK_100, BLACK)
