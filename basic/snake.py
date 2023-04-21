import random
#[blank, snake, food]
class Snake:
    def __init__(self, rows = 10, cols = 10):
        self.rows = rows
        self.cols = cols
        self.initGrid()
    
    def initGrid(self):
        self.board = [[0 for j in range(self.cols)] for i in range(self.rows)]
        redo = True
        while(redo):
            r = random.randint(0,self.rows-1)
            c = random.randint(0, self.cols-1)
            if(self.board[r][c]==0):
                self.board[r][c] = 1
                print(r,c)
                redo = False
        while(redo):
            r = random.randint(0,self.rows-1)
            c = random.randint(0, self.cols-1)
            if(self.board[r][c]==0):
                self.board[r][c] = 2
                print(r,c)
                redo = False