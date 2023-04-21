from snake import Snake
import pygame
import time
game = Snake()
cellSize = 50
run = True
pygame.init()

display = pygame.display.set_mode((game.cols * cellSize, (game.rows + 1) * cellSize + 50))

font = pygame.font.SysFont(None, 40)

def update():
    display.fill(pygame.Color("black"))
    game.boardComp()
    for row in range(game.rows):
        for col in range(game.cols):
            color = pygame.Color("green")
            if game.finalBoard[row][col] == 1:
                color = pygame.Color("blue")
            elif game.finalBoard[row][col] == 2:
                color = pygame.Color("red")
            pygame.draw.rect(display, color, pygame.Rect(col*cellSize, (row+1)*cellSize, cellSize, cellSize))
            pygame.draw.rect(display, pygame.Color("black"), pygame.Rect(col*cellSize, (row+1)*cellSize, cellSize, cellSize), 1)
    
    scoreText = font.render("Score: " + str(game.score), True, pygame.Color("white"))
    display.blit(scoreText, (10, (game.rows + 1) * cellSize + 50 - 40))
    
    pygame.display.update()


while(run):
    time.sleep(.5)
    action = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            continue
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # handle up arrow key press
                action = 0
            elif event.key == pygame.K_DOWN:
                # handle down arrow key press
                action = 3
            elif event.key == pygame.K_LEFT:
                # handle left arrow key press
                action = 2
            elif event.key == pygame.K_RIGHT:
                # handle right arrow key press
                action = 1
            elif event.key == pygame.K_RETURN:
                game = Snake()
    if(not game.gameOver):
        game.step(action)
        update()
    
    





