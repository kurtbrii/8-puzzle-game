# Punzalan, Kurt Brian Daine B. Punzalan
# 2020-00772
# CMSC 170 X-4L
# Exer 03

import os
from tkinter import filedialog as fd

import pygame

from a_star_func import *
from bfs_dfs import *
from gameplay_functions import *
from settings import *

os.system("cls")

# MAIN FILE
terminal_list = []
terminal_list = readFile("src/read.in")

tiles_list = []
tiles_list = addTiles()

# initialize pygame
pygame.init()

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("8 Puzzle Game")
icon = pygame.image.load("./src/assets/jigsaw.png")
pygame.display.set_icon(icon)


font = pygame.font.Font("freesansbold.ttf", 20)
not_solvable, textRect = textDisplay(
    font, "Puzzle is not Solvable!", RED, WIN_WIDTH, 150, 25
)
won, textRect_won = textDisplay(font, "You Win!", BLACK, WIN_WIDTH, 150, 25)

# if number of inversions is odd, it is not solvable
is_solvable = True
if not isSolvable(terminal_list):
    is_solvable = False

is_file_dialog = False
is_path_seen = False
is_next_running = False
is_playable = True
is_bfs_clicked = ""
to_be_solved = ""

is_running = True
while is_running:
    screen.fill(LIGHT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # renders/reprints all tiles
    if not is_next_running:  # if playable
        printTilesOnClick(
            tiles_list,
            terminal_list,
            screen,
            PINK_100,
            BLACK,
            BLACK,
            PINK_100,
            None,
            None,
        )
    else:  # if not playable because user already clicked bfs/dfs
        printTilesOnClick(
            tiles_list, terminal_list, screen, PINK_100, BLACK, PINK_50, BLACK_50, i, j
        )

    # if number of inversions is odd, it is not solvable
    if not is_solvable:
        screen.blit(not_solvable, textRect)

    if winnerCheck(terminal_list):
        screen.blit(won, textRect_won)
        printTilesOnClick(
            tiles_list,
            terminal_list,
            screen,
            PINK_50,
            BLACK_50,
            PINK_50,
            BLACK_50,
            None,
            None,
        )
        is_playable = False  # user will not be able to click anymore
        is_path_seen = False

    if is_path_seen:
        pathText, pathTextRect = textDisplay(
            font, f"Path Cost: {str(path_cost)}", BLACK, WIN_WIDTH, 150, 25
        )
        screen.blit(pathText, pathTextRect)

        path_list_text, path_list_rect = textDisplay(
            font,
            f"Path: {outputPath}",
            BLACK,
            WIN_WIDTH * 2,
            WIN_HEIGHT * 2,
            WIN_HEIGHT - 50,
        )
        screen.blit(path_list_text, path_list_rect)

    # BFS-DFS Specs
    select_file = Button(400, 245, "Select File")
    select_file.drawTile(screen, PINK_100, BLACK)

    solution = Button(400, 285, "Solution")
    solution.drawTile(screen, PINK_100, BLACK)

    bfs = Button(400, 50, "BFS")
    dfs = Button(400, 90, "DFS")
    a_star = Button(400, 130, "A*")
    clickedBfsDfs(
        screen, dfs, bfs, a_star, PINK_100, PINK_100, BLACK, BLACK, BLACK, PINK_100
    )

    next = Button(400, 325, "Next")
    if is_next_running:
        next.drawTile(screen, PINK_100, BLACK)

    if is_bfs_clicked == "1":  # bfs button clicked
        clickedBfsDfs(
            screen,
            dfs,
            bfs,
            a_star,
            PINK_50,
            PINK_100,
            BLACK_50,
            BLACK,
            BLACK,
            PINK_100,
        )

    elif is_bfs_clicked == "2":  # dfs button clicked
        clickedBfsDfs(
            screen,
            dfs,
            bfs,
            a_star,
            PINK_100,
            PINK_50,
            BLACK_50,
            BLACK_50,
            BLACK,
            PINK_100,
        )

    elif is_bfs_clicked == "3":  # a_star button clicked
        clickedBfsDfs(
            screen,
            dfs,
            bfs,
            a_star,
            PINK_100,
            PINK_100,
            BLACK,
            BLACK,
            BLACK_50,
            PINK_50,
        )

    # GAMEPLAY
    if event.type == pygame.MOUSEBUTTONDOWN:
        try:
            x, y = pygame.mouse.get_pos()

            # every next button clicked, actions_index which serves as the index for the list of actions generated is incremented by 1
            if next.isClicked(x, y):
                if currentState and not winnerCheck(terminal_list):
                    i, j = findEmptyCell(terminal_list)

                    # swap and update the board with the string actions as the indicator on where the cells will move
                    match actions_string_list[actions_index]:
                        case "L":
                            terminal_list = swapCells(terminal_list, i, j, i, j - 1)
                        case "R":
                            terminal_list = swapCells(terminal_list, i, j, i, j + 1)
                        case "U":
                            terminal_list = swapCells(terminal_list, i, j, i - 1, j)
                        case "D":
                            terminal_list = swapCells(terminal_list, i, j, i + 1, j)
                    actions_index += 1

            if x <= 400:  # tiles are being checked/played
                row_clicked, col_clicked = calculateCoordinate(tiles_list, x, y)

                printArray(terminal_list)

                if is_playable:
                    if terminal_list[row_clicked][col_clicked] == 0:
                        print("You cannot click this cell")
                    else:
                        gameplay(terminal_list, row_clicked, col_clicked)

            else:  # specification for BFS and DFS
                # click whether user wants to solve using dfs or bfs
                if select_file.isClicked(x, y):
                    try:
                        filename = fd.askopenfilename()

                        terminal_list = readFile(filename)
                        is_file_dialog = True
                        print(filename)
                    except:
                        print("Invalid file")

                if dfs.isClicked(x, y):
                    is_bfs_clicked = "2"
                    print(f"Checking for the solution using {dfs.name}")
                    to_be_solved = "dfs"

                elif bfs.isClicked(x, y):
                    is_bfs_clicked = "1"
                    print(f"Checking for the solution using {bfs.name}")
                    to_be_solved = "bfs"

                elif a_star.isClicked(x, y):
                    is_bfs_clicked = "3"
                    print(f"Checking for the solution using {a_star.name}")
                    to_be_solved = "a_star"

                # When solution button is clicked and bfs or dfs is selected
                if solution.isClicked(x, y) and (
                    to_be_solved == "bfs"
                    or to_be_solved == "dfs"
                    or to_be_solved == "a_star"
                ):
                    is_playable = False  # user cannot play anymore

                    if is_file_dialog:
                        terminal_list = readFile(filename)  # resets the board
                    else:
                        terminal_list = readFile("src/read.in")  # resets the board

                    # user cannot choose bfs or dfs if the puzzle is not solvable
                    if not isSolvable(terminal_list):
                        print("Puzzle is Not Solvable!")
                    else:
                        print(f"Solution for {to_be_solved}")
                        is_next_running = True

                        i, j = findEmptyCell(terminal_list)
                        initial = Node(terminal_list, i, j, None, None, 0, 0, 0)

                        if (
                            to_be_solved == "bfs"
                        ):  # inset at the first index, remove at the last index
                            currentState = BFS_DFS(initial, 0)
                        elif (
                            to_be_solved == "dfs"
                        ):  # insert at the last index, remove at the last index
                            currentState = BFS_DFS(initial, -1)
                        else:  # A*
                            currentState = AStar(initial)

                        # returns the list of actions as well as the path cost
                        actions_string_list, path_cost = findPath(currentState)
                        actions_index = 0
                        print(actions_string_list)
                        fileWrite(
                            actions_string_list
                        )  # outputs all actions in puzzle.out
                        is_path_seen = True

                        # reads the input of puzzle.out and use it to display all moves on the screen
                        outputPath = readOutputFile()

        except TypeError:
            print("This area cannot be clicked")
    # time.sleep(0.03)
    pygame.display.update()

pygame.quit()
