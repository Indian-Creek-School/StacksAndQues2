import pygame
from pygame.math import Vector2
import random   

lines = []

class Maze:


    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Maze")
        self.width = 900
        self.height = 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.exit = False
        self.lengths = [0, random.randint(50,300), random.randint(100,300), random.randint(75,200), random.randint(100,400), random.randint(30,50), random.randint(30,50), random.randint(30,50), random.randint(30,50), random.randint(30,50), random.randint(30,50),]
        self.prevX = 0
        self.prevY = 40
    
    def drawBorder(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True
        width = self.width
        pygame.draw.line(self.screen, (255, 255, 255), (0,0), (width, 0), 20)
        pygame.draw.line(self.screen, (255, 255, 255), (0,0), (0, width), 20)
        pygame.draw.line(self.screen, (255, 255, 255), (0,width), (width, width), 20)
        pygame.draw.line(self.screen, (255, 255, 255), (width,width), (width, 0), 20)

    def drawPath(self, screen):
        # for row in self.grid:
        #     for cell in row:
        #         cell.draw(screen)
        # l1 = Line()
        # l1.draw(screen)
        self.drawLine(self.prevX, self.prevY, 1,0)
        line1 = [self.prevX, self.prevY]
        lines.append(line1)
        self.drawLine(self.prevX, self.prevY, 0,2)
        line2 = [self.prevX, self.prevY]
        lines.append(line2)
        self.drawLine(self.prevX, self.prevY, 3,0)
        line3 = [self.prevX, self.prevY]
        lines.append(line3)
        self.drawLine(self.prevX, self.prevY, 0,4)
        line4 = [self.prevX, self.prevY]
        lines.append(line4)
        self.drawLine(self.prevX, self.prevY, 5,0)
        line5 = [self.prevX, self.prevY]
        lines.append(line5)
        self.drawLine(self.prevX, self.prevY, 0,6)
        line6 = [self.prevX, self.prevY]
        lines.append(line6)

        print(lines)
        

    def drawLine(self, x1, y1, lenx, leny):
        x2 = x1+self.lengths[lenx]
        y2 = y1+self.lengths[leny]
        pygame.draw.line(self.screen, (255,0,0), (x1,y1), (x2,y2), 20)
        self.prevX = x2
        self.prevY = y2
    
    # def LegalMove(self, x):
    #     return False

    pygame.quit()

# class Line:
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.w = 20
#         self.h = 20
#         self.image = pygame.Surface([self.w, self.h],)
#         self.image.fill((255, 0, 0))
#         self.rect = self.image.get_rect()

#     def draw(self, screen):
#         line1 = self.rect
#         screen.blit(self.image, line1)
#         line2 = self.rect.move(20.0,20.0)
#         screen.blit(self.image, line2)


if __name__ == '__main__':
    maze = Maze()
    while not maze.exit:
        maze.drawBorder()
        maze.drawPath(maze.screen)
        pygame.display.flip()
    

