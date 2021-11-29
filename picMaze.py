import pygame
from solver import *

class picMaze:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Maze")
        self.width = 900
        self.height = 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.exit = False

    def eventQueue(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True

    def pasteMaze(self):
        image = pygame.image.load("maze.jpg")
        self.screen.blit(image, (0, 0))

    pygame.quit()

if __name__ == '__main__':
    maze = picMaze()
    while not maze.exit:
        maze.eventQueue()
        maze.pasteMaze()
        pygame.display.flip()

