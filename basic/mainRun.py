from snake import Snake
import numpy as np

t = Snake(cols=5)
t.boardComp()
print(np.array(t.finalBoard))

t.step(0)
t.boardComp()
print(np.array(t.finalBoard))

t.step(0)
t.boardComp()
print(np.array(t.finalBoard))

