import gym
from gym import spaces
from snake import Snake
import pygame
import random

class SnakeEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    
    def __init__(self, rows=10, cols=10):
        super(SnakeEnv, self).__init__()
        self.rows = rows
        self.cols = cols
        self.action_space = spaces.Discrete(5)
        self.observation_space = spaces.Box(low=0, high=2, shape=(self.rows, self.cols), dtype=int)
        self.snake = Snake(rows=self.rows, cols=self.cols)
        
    def reset(self):
        self.snake = Snake(rows=self.rows, cols=self.cols)
        self.snake.boardComp()
        return self.snake.finalBoard
        
    def step(self, action):
        done = self.snake.step(action)
        reward = self.snake.score
        # done = self.snake.gameOver
        info = {}
        self.snake.boardComp()
        return self.snake.finalBoard, reward, done, info
        
    def render(self, mode='human'):
        self.snake.draw()
        
    def close(self):
        pygame.quit()