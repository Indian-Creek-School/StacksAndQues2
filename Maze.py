import pygame
from math import sin, radians, degrees, copysign
from pygame.math import Vector2

class Maze:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Maze")
        self.width = 900
        self.height = 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.exit = False
        
    
    def drawBorder(self):
        while not self.exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
            self.screen.fill((0, 0, 0))
            width = self.width
            pygame.draw.line(self.screen, (255, 255, 255), (0,0), (width, 0), 20)
            pygame.draw.line(self.screen, (255, 255, 255), (0,0), (0, width), 20)
            pygame.draw.line(self.screen, (255, 255, 255), (0,width), (width, width), 20)
            pygame.draw.line(self.screen, (255, 255, 255), (width,width), (width, 0), 20)
            pygame.display.flip()

    def drawPath(self):
        while not self.exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
            width = self.width
            pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    maze = Maze()
    maze.drawBorder()
