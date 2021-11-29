import pygame
from solver import *

class picMaze:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Maze")
        self.width = 280
        self.height = 280
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.exit = False

    def eventQueue(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True

    def pasteMaze(self):
        image = pygame.image.load("maze.jpg")
        self.screen.blit(image, (0, 0))

    def drawTurtle(self):
        t = solver(0.0,40.0)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "turtle.png")
        turtle_image = pygame.image.load(image_path)
        while self.screen.get_at((int(t.position.x),int(t.position.y))) == (255,255,255):
            t.xIncrease()
            self.screen.blit(turtle_image, t.position)

    pygame.quit()

if __name__ == '__main__':
    maze = picMaze()
    while not maze.exit:
        maze.eventQueue()
        maze.pasteMaze()
        pygame.display.flip()

