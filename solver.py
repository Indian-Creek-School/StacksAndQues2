import os
import pygame
from math import sin, radians, degrees, copysign
from pygame.math import Vector2
from collections import deque
class solver:
    
    def __init__(self, m):
        self.maze=m
        self.path=deque()
        
    def move(self, x):
        if(self.maze.LegalMove(x)):
            self.path.append(x)
        else:
            self.pop