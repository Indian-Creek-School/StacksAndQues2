import pygame
from pygame.math import Vector2
import random   
from solver import *

class Maze:


    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Maze")
        self.width = 900
        self.height = 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.exit = False
        self.lengths = [0, random.randint(50,300), random.randint(100,300), random.randint(75,200), random.randint(100,400), random.randint(30,50), random.randint(200,400), random.randint(100,275), random.randint(50,300), random.randint(90,150), 700]
        self.prevX = 0
        self.prevY = 0
    
    def drawBorder(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True
        width = self.width
        pygame.draw.line(self.screen, (255, 255, 255), (0,0), (width, 0), 20)
        pygame.draw.line(self.screen, (255, 255, 255), (0,0), (0, width), 20)
        pygame.draw.line(self.screen, (255, 255, 255), (0,width), (width, width), 20)
        pygame.draw.line(self.screen, (255, 255, 255), (width,width), (width, 0), 20)

    def drawPath(self, x, y, rotate = 0):
        # for row in self.grid:
        #     for cell in row:
        #         cell.draw(screen)
        # l1 = Line()
        # l1.draw(screen)
        self.prevX = x
        self.prevY = y

        if rotate == 0:
            self.drawLine(self.prevX, self.prevY, 1,0)
            self.drawLine(self.prevX, self.prevY, 0,2)
            self.drawLine(self.prevX, self.prevY, 3,0)
            self.drawLine(self.prevX, self.prevY, 0,4)
            self.drawLine(self.prevX, self.prevY, 5,0)
            self.drawLine(self.prevX, self.prevY, 0,6)
            self.drawLine(self.prevX, self.prevY, 7,0)
            self.drawLine(self.prevX, self.prevY, 0,8)
            self.drawLine(self.prevX, self.prevY, 9,0)
            self.drawLine(self.prevX, self.prevY, 0,10)
        elif rotate == 90:
            self.rotate90(self.prevX, self.prevY, 1,0)
            self.rotate90(self.prevX, self.prevY, 0,2)
            self.rotate90(self.prevX, self.prevY, 3,0)
            self.rotate90(self.prevX, self.prevY, 0,4)
            self.rotate90(self.prevX, self.prevY, 5,0)
            self.rotate90(self.prevX, self.prevY, 0,6)
            self.rotate90(self.prevX, self.prevY, 7,0)
            self.rotate90(self.prevX, self.prevY, 0,8)
            self.rotate90(self.prevX, self.prevY, 9,0)
            self.rotate90(self.prevX, self.prevY, 0,10)
        elif rotate == 180:
            self.rotate180(self.prevX, self.prevY, 1,0)
            self.rotate180(self.prevX, self.prevY, 0,2)
            self.rotate180(self.prevX, self.prevY, 3,0)
            self.rotate180(self.prevX, self.prevY, 0,4)
            self.rotate180(self.prevX, self.prevY, 5,0)
            self.rotate180(self.prevX, self.prevY, 0,6)
            self.rotate180(self.prevX, self.prevY, 7,0)
            self.rotate180(self.prevX, self.prevY, 0,8)
            self.rotate180(self.prevX, self.prevY, 9,0)
            self.rotate180(self.prevX, self.prevY, 0,10)
        elif rotate == 270:
            self.rotate270(self.prevX, self.prevY, 1,0)
            self.rotate270(self.prevX, self.prevY, 0,2)
            self.rotate270(self.prevX, self.prevY, 3,0)
            self.rotate270(self.prevX, self.prevY, 0,4)
            self.rotate270(self.prevX, self.prevY, 5,0)
            self.rotate270(self.prevX, self.prevY, 0,6)
            self.rotate270(self.prevX, self.prevY, 7,0)
            self.rotate270(self.prevX, self.prevY, 0,8)
            self.rotate270(self.prevX, self.prevY, 9,0)
            self.rotate270(self.prevX, self.prevY, 0,10)
        elif rotate == 360:
            self.rotate360(self.prevX, self.prevY, 1,0)
            self.rotate360(self.prevX, self.prevY, 0,2)
            self.rotate360(self.prevX, self.prevY, 3,0)
            self.rotate360(self.prevX, self.prevY, 0,4)
            self.rotate360(self.prevX, self.prevY, 5,0)
            self.rotate360(self.prevX, self.prevY, 0,6)
            self.rotate360(self.prevX, self.prevY, 7,0)
            self.rotate360(self.prevX, self.prevY, 0,8)
            self.rotate360(self.prevX, self.prevY, 9,0)
            self.rotate360(self.prevX, self.prevY, 0,10)

    def drawLine(self, x1, y1, lenx, leny):
        x2 = x1+self.lengths[lenx]
        y2 = y1+self.lengths[leny]
        pygame.draw.line(self.screen, (0,255,0), (x1,y1), (x2,y2), 20)
        self.prevX = x2
        self.prevY = y2

    def rotate90(self, x1, y1, lenx,leny):
        x2 = x1+self.lengths[lenx]
        y2 = y1-self.lengths[leny]
        pygame.draw.line(self.screen, (165,42,42), (x1,y1), (x2,y2), 20)
        self.prevX = x2
        self.prevY = y2
    
    def rotate180(self,x1,y1,lenx,leny):
        x2 = x1-self.lengths[lenx]
        y2 = y1-self.lengths[leny]
        pygame.draw.line(self.screen, (165,42,42), (x1,y1), (x2,y2), 20)
        self.prevX = x2
        self.prevY = y2

    def rotate270(self, x1, y1, lenx, leny):
        x2 = x1-self.lengths[lenx]
        y2 = y1+self.lengths[leny]
        pygame.draw.line(self.screen, (165,42,42), (x1,y1), (x2,y2), 20)
        self.prevX = x2
        self.prevY = y2
    
    def rotate360(self, x1, y1, lenx, leny):
        x2 = x1+self.lengths[lenx]
        y2 = y1+self.lengths[leny]
        pygame.draw.line(self.screen, (165,42,42), (x1,y1), (x2,y2), 20)
        self.prevX = x2
        self.prevY = y2
    
    def LegalMove(self, x):
        return False

    def moveTurtle(self):
        t = solver(0.0,40.0)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "turtle.png")
        turtle_image = pygame.image.load(image_path)
        rotated = pygame.transform.rotate(turtle_image,0)
        while self.screen.get_at((int(t.position.x),int(t.position.y))) == (0,255,0):
            t.xIncrease()
            self.screen.blit(rotated, t.position)
            print(t.position)
        



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
    count = 0
    rand = random.randrange(0,maze.width/2,20)
    rand2 = random.randrange(0,maze.width/2,20)
    rand3 = random.randrange(0,maze.width/2,20)
    rand4 = random.randrange(maze.width/2,maze.width,20)
    rand5 = random.randrange(maze.width/2,maze.width,20)
    rand6 = random.randrange(maze.width/2,maze.width,20)
    while not maze.exit:
        maze.drawBorder()
        maze.drawPath(rand, maze.width, 90)
        maze.drawPath(maze.width, rand, 180)
        maze.drawPath(0, rand, 360)

        maze.drawPath(rand2, maze.width, 90)
        maze.drawPath(maze.width, rand2, 180)
        maze.drawPath(0, rand2, 360)

        maze.drawPath(rand3, maze.width, 90)
        maze.drawPath(maze.width, rand3, 180)
        maze.drawPath(0, rand3, 360)

        maze.drawPath(rand4, maze.width, 90)
        maze.drawPath(maze.width, rand4, 180)
        maze.drawPath(0, rand4, 360)

        maze.drawPath(rand5, maze.width, 90)
        maze.drawPath(maze.width, rand5, 180)
        maze.drawPath(0, rand5, 360)

        maze.drawPath(rand6, maze.width, 90)
        maze.drawPath(maze.width, rand6, 180)
        maze.drawPath(0, rand6, 360)

        maze.drawPath(0, 40)

        maze.moveTurtle()

        pygame.display.flip()
    

