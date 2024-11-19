from settings import *
from tiles import Tiles


# terminal functions
def readFile():
    list = []
    # from https://stackoverflow.com/questions/61617165/input-data-from-file-to-2d-array-in-python
    with open("src/read.in", "r") as file:
        for line in file:
            newList = line.split()
            newList = [
                int(c) for c in newList
            ]  # put as int before appending to the list
            list.append(newList)

    return list


def printArray(list):
    # prints the contents of the array
    for i in list:
        print("\t".join(map(str, i)))


def winnerCheck(list):
    # from https://stackoverflow.com/questions/50775024/itertools-chain-from-iterable
    # undo all nesting of our list, check if they are ascending (excluding 0), then prints if they are
    list = [
        j for sub in list for j in sub
    ]  # detaches all nested list, and put it in a single-dimensional one

    if list[-1] == 0:
        list.pop()
        return list == sorted(list)


def textDisplay(font, text, color, WIN_WIDTH, WIN_HEIGHT, height):
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = (WIN_WIDTH // 2 - WIN_HEIGHT // 2, height)

    return text, textRect


def getInversionCount(list):
    newList = [j for sub in list for j in sub]  # put elements in a single list
    newList.remove(0)  # so that 0 is not included in the counting of inv counts

    # checks how many numbers are greater than the current one being checked
    inversionCount = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if newList[i] > newList[j]:
                inversionCount += 1

    return inversionCount


def isSolvable(list):
    return getInversionCount(list) % 2 == 0


def addTiles():
    # y coordinate will start at 50; x at 0
    # instantiate objects reflecting terminal_array (storage from read.in) in app.py
    # taking note of their positions on screen

    tiles_list = []

    y_pos = 45
    for i in range(3):
        new_list = []
        x_pos = 45
        for j in range(3):
            new_list.append(Tiles(x_pos, y_pos))
            x_pos += 105
        y_pos += 105
        tiles_list.append(new_list)

    return tiles_list


def swapCells(list, i, j, row_clicked, col_clicked):
    terminal_temp = list[i][j]
    list[i][j] = list[row_clicked][col_clicked]
    list[row_clicked][col_clicked] = terminal_temp

    return list


def calculateCoordinate(tiles_list, x, y):
    # check which cell being clicked by calculating which x and y ranges it belongs to
    # (checking kung anong current position niya sa screen)
    for i in range(3):
        for j in range(3):
            tiles = tiles_list[i][j]
            if tiles.isClicked(x, y):
                print(f"coordinates being clicked: ({i}, {j})")
                return i, j


def gameplay(terminal_list, row_clicked, col_clicked):
    for i in range(row_clicked - 1, row_clicked + 2):
        for j in range(col_clicked - 1, col_clicked + 2):  # check neighboring cells
            if (
                (i == row_clicked - 1 and j == col_clicked)
                or (i == row_clicked and j == col_clicked - 1)
                or (i == row_clicked and j == col_clicked + 1)
                or (i == row_clicked + 1 and j == col_clicked)
            ):
                try:
                    # for non-adjacent cells whose neighbor is 0
                    if j < 0 or i < 0:
                        continue

                    if terminal_list[i][j] == 0:  # the neighboring cell is 0
                        print(f"empty cell found: ({i}, {j})")

                        terminal_list = swapCells(
                            terminal_list, i, j, row_clicked, col_clicked
                        )

                        continue

                except IndexError:
                    continue
