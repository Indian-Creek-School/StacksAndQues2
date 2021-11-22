import pygame
from math import sin, radians, degrees, copysign
from pygame.math import Vector2
import random

class Maze:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Maze")
        self.width = 900
        self.height = 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.exit = False
        self.line1 = []
        
    
    def drawBorder(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True
        self.screen.fill((0, 0, 0))
        width = self.width
        pygame.draw.line(self.screen, (255, 255, 255), (0,0), (width, 0), 20)
        pygame.draw.line(self.screen, (255, 255, 255), (0,0), (0, width), 20)
        pygame.draw.line(self.screen, (255, 255, 255), (0,width), (width, width), 20)
        pygame.draw.line(self.screen, (255, 255, 255), (width,width), (width, 0), 20)

    def findPath(self):
        width = self.width
        flip = False
        x1 = 0
        y1 = 40
        x2 = 0
        y2 = 0
        if flip == False:
            x2 = random.randint(x1 ,x1+20)
            y2=y1
            line1 = [self.screen, (255, 0, 0), (x1,y1), (x2, y2), 20]
            self.line1.append(line1)
            x1= x2
            y1 = y2
            flip = True

    def drawPath(self):
        print(self.line1)
    
    def LegalMove(self, x):
        return False

    pygame.quit()

if __name__ == '__main__':
    maze = Maze()
    while not maze.exit:
        maze.drawBorder()
        maze.drawPath()
        pygame.display.flip()

