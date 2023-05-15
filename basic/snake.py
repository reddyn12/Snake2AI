import random
import pygame
import numpy as np

#[blank, snake, food]
class Snake:
    def __init__(self, rows = 10, cols = 10):
        self.rows = rows
        self.cols = cols
        self.initGrid()
        self.expand = None
        self.direction = 1
        self.moves = [(-1,0), (0,1), (0,-1), (1,0)]
        self.gameOver = False
        self.score = 0
        self.growing = False
        self.display = None
        
        self.cellSize = 50
    def initGrid(self):
        self.board = [[0 for j in range(self.cols)] for i in range(self.rows)]
        redo = True
        while(redo):
            r = random.randint(0,self.rows-1)
            c = random.randint(0, self.cols-1)
            if(self.board[r][c]==0):
                # self.board[r][c] = 1
                # print(r,c)
                self.path = [(r,c)]
                redo = False
        redo = True
        while(redo):
            r = random.randint(0,self.rows-1)
            c = random.randint(0, self.cols-1)
            if(self.board[r][c]==0 and (r,c) not in self.path):
                self.board[r][c] = 2
                self.food = (r,c)
                # print(r,c)
                redo = False
    #[up, right, left, down, NONE]
    def step(self, action = None):
        if(action is None):
            action = self.direction
        elif(action == 4):
            pass
        elif(action==0 and self.direction==3):
            pass
        elif(action==3 and self.direction==0):
            pass
        elif(action==1 and self.direction==2):
            pass
        elif(action==2 and self.direction==1):
            pass
        elif(action>4):
            pass
        else:
            self.direction = action
        nr = self.path[0][0] + self.moves[self.direction][0]
        nc = self.path[0][1] + self.moves[self.direction][1]
        if(nr<0 or nr>=self.rows):
            self.gameOver = True
            return self.gameOver
        if(nc<0 or nc>=self.cols):
            self.gameOver = True
            return self.gameOver
        if((nr,nc) in self.path):
            if(self.growing):
                self.gameOver = True
                return self.gameOver
            else:
                if(self.path[-1] == (nr,nc)):
                    self.gameOver = True
                    return self.gameOver
        self.path = [(nr, nc)] + self.path
        if(not self.growing):
            # self.path.pop()
            del self.path[-1]
        else:
            self.growing = False
        if(self.path[0]==self.food):
            self.score = self.score + 1
            self.growing = True
            self.board[self.food[0]][self.food[1]] = 0
            redo = True
            while(redo):
                r = random.randint(0,self.rows-1)
                c = random.randint(0, self.cols-1)
                if(self.board[r][c]==0 and (r,c) not in self.path):
                    self.board[r][c] = 2
                    self.food = (r,c)
                    redo = False
        return self.gameOver
    def boardComp(self):
        # HOW DOES THIS BREAK???? FUCK COPY vs DEEPCOPY
        # self.finalBoard = self.board
        self.finalBoard = [row[:] for row in self.board]
        # print(self.path)
        for x in self.path:
            self.finalBoard[x[0]][x[1]] = 1

    def getPixels(self):
        pixel_array = pygame.surfarray.array3d(self.display)

        # Return the pixel array
        return pixel_array
    def draw(self):
        if self.display is None:
            pygame.init()
            self.display = pygame.display.set_mode((self.cols * self.cellSize, (self.rows + 1) * self.cellSize + 50))
            self.font = pygame.font.SysFont(None, 40)
            
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.display.fill(pygame.Color("black"))
            self.boardComp()
            for row in range(self.rows):
                for col in range(self.cols):
                    color = pygame.Color("green")
                    if self.finalBoard[row][col] == 1:
                        color = pygame.Color("blue")
                    elif self.finalBoard[row][col] == 2:
                        color = pygame.Color("red")
                    pygame.draw.rect(self.display, color, pygame.Rect(col*self.cellSize, (row+1)*self.cellSize, self.cellSize, self.cellSize))
                    pygame.draw.rect(self.display, pygame.Color("black"), pygame.Rect(col*self.cellSize, (row+1)*self.cellSize, self.cellSize, self.cellSize), 1)
            
            self.scoreText = self.font.render("Score: " + str(self.score), True, pygame.Color("white"))
            self.display.blit(self.scoreText, (10, (self.rows + 1) * self.cellSize + 50 - 40))
            
            pygame.display.update()