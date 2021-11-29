import os
import pygame
from pygame.math import Vector2
from collections import deque

class solver:
    
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.position = Vector2(x, y)
        # self.maze=m
        # self.path=deque()
    
    def xIncrease(self):
        self.position.x += 1

    def yIncrease(self):
        self.position.y += 1

    def xDecrease(self):
        self.position.x -= 1
    
    def yDecrease(self):
        self.position.x -=1
        
        
    # def move(self, x):
    #     current_dir = os.path.dirname(os.path.abspath(__file__))
    #     image_path = os.path.join(current_dir, "turtle.png")
    #     turtle_image = pygame.image.load(image_path)
    #     rotated = pygame.transform.rotate(turtle_image, car.angle)
    #     if(self.maze.LegalMove(x)):
    #         self.path.append(x)
    #     else:
    #         self.pop