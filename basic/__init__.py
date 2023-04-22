import gym
from snakeGym import SnakeEnv

gym.register(
    id='SnakeEnv-v0',
    entry_point='snakeGym:SnakeEnv',
)