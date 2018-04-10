import pygame
from pygame.locals import *
import sys
import random

pygame.init()

screen = pygame.display.set_mode((640,480))
color = (0, 0, 0)
screen.fill(color)

pygame.draw.lines(screen, color, False, [(100,100), (150,200), (200,100)], 1)

pygame.display.flip()