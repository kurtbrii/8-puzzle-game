import pygame
from settings import *

class Tiles:
  def __init__(self, x_pos, y_pos):
    self.x_pos = x_pos
    self.y_pos = y_pos

  def drawTile(self, screen, terminal_list, i, j, TILE_COLOR, FONT_COLOR):
    pygame.draw.rect(screen, TILE_COLOR, [self.x_pos, self.y_pos, 100, 100], 0, 15)

    font = pygame.font.Font('freesansbold.ttf', 20)
    screen.blit(font.render(str(terminal_list[i][j]), True, FONT_COLOR), ((self.x_pos+self.x_pos+95)*0.5, (self.y_pos+self.y_pos+95)*0.5))

  def isClicked(self, x, y):
    return x in range(self.x_pos, self.x_pos+100) and y in range(self.y_pos, self.y_pos+100)
