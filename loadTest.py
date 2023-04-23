import numpy as np
import pygame


d = np.load("ss.npy", allow_pickle=True)
shape = d.shape

surface = pygame.surfarray.make_surface(d)

screen = pygame.display.set_mode((shape[0], shape[1]))

screen.blit(surface, (0, 0))
pygame.display.update()

# print(d.shape)

# wait for the user to close the window
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

# quit pygame
pygame.quit()