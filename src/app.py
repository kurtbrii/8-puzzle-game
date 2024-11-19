# Punzalan, Kurt Brian Daine B. Punzalan
# 2020-00772
# CMSC 170 X-4L
# Exer 02

import os

import pygame

from gameplay_functions import *
from settings import *

os.system("clear")

# MAIN FILE
terminal_list = []
terminal_list = readFile()

tiles_list = []
tiles_list = addTiles()

# initialize pygame
pygame.init()

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("8 Puzzle Game")
icon = pygame.image.load("./src/assets/jigsaw.png")
pygame.display.set_icon(icon)

font = pygame.font.Font("freesansbold.ttf", 20)
not_solvable, textRect = textDisplay(font, "Puzzle is not Solvable!", RED, WIN_WIDTH)
won, textRect_won = textDisplay(font, "You Win!", BLACK, WIN_WIDTH)

# if number of inversions is odd, it is not solvable
is_solvable = True
if not isSolvable(terminal_list):
    is_solvable = False

is_playable = True
is_running = True
while is_running:
    screen.fill(LIGHT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # renders/reprints all tiles
    printTiles(tiles_list, terminal_list, screen, PINK_100, BLACK)

    if winnerCheck(terminal_list):
        screen.blit(won, textRect_won)
        printTiles(tiles_list, terminal_list, screen, PINK_50, BLACK_50)
        is_playable = False  # user will not be able to click anymore

    if not is_solvable:
        screen.blit(not_solvable, textRect)

    if event.type == pygame.MOUSEBUTTONDOWN:  # on click
        try:
            x, y = pygame.mouse.get_pos()
            row_clicked, col_clicked = calculateCoordinate(tiles_list, x, y)

            printArray(terminal_list)
            if is_playable:
                if terminal_list[row_clicked][col_clicked] == 0:
                    print("You cannot click this cell")
                else:
                    gameplay(terminal_list, row_clicked, col_clicked)
        except TypeError:
            print("This area cannot be clicked")

    pygame.display.update()

pygame.quit()
