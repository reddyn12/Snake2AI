import random
#[blank, snake, food]
class Snake:
    def __init__(self, rows = 10, cols = 10):
        self.rows = rows
        self.cols = cols
        self.initGrid()
        self.expand = None
        self.direction = None
        self.moves = [(-1,0), (0,1), (0,-1), (1,0)]
        self.gameOver = False
        self.score = 0
        self.growing = False
    def initGrid(self):
        self.board = [[0 for j in range(self.cols)] for i in range(self.rows)]
        redo = True
        while(redo):
            r = random.randint(0,self.rows-1)
            c = random.randint(0, self.cols-1)
            if(self.board[r][c]==0):
                # self.board[r][c] = 1
                print(r,c)
                self.path = [(r,c)]
                redo = False
        redo = True
        while(redo):
            r = random.randint(0,self.rows-1)
            c = random.randint(0, self.cols-1)
            if(self.board[r][c]==0 and (r,c) not in self.path):
                self.board[r][c] = 2
                self.food = (r,c)
                print(r,c)
                redo = False
    #[up, right, left, down]
    def step(self, action = None):
        if(action is None):
            action = self.direction
        else:
            self.direction = action
        nr = self.path[0][0] + self.moves[self.direction][0]
        nc = self.path[0][1] + self.moves[self.direction][1]
        if(nr<0 or nr>=self.rows):
            self.gameOver = True
        if(nc<0 or nc>=self.cols):
            self.gameOver = True
        if((nr,nc) in self.path):
            if(self.growing):
                self.gameOver = True
            else:
                if(self.path[-1] == (nr,nc)):
                    self.gameOver = True
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
    def boardComp(self):
        # HOW DOES THIS BREAK???? FUCK COPY vs DEEPCOPY
        # self.finalBoard = self.board
        self.finalBoard = [row[:] for row in self.board]
        # print(self.path)
        for x in self.path:
            self.finalBoard[x[0]][x[1]] = 1
            
        pass