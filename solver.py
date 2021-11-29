import os
import pygame
from pygame.math import Vector2
from collections import deque
class solver:
    
    def __init__(self, m):
        pygame.sprite.Sprite.__init__(self)
        self.w = 20
        self.h = 20
        self.maze=m
        self.path=deque()
        
    def move(self, x):
        image_path = os.path.join(current_dir, "car.png")
        car_image = pygame.image.load(image_path)
        if(self.maze.LegalMove(x)):
            self.path.append(x)
        else:
            self.pop