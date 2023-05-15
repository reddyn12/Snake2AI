from snake import Snake
import numpy as np
import time


import time
t = Snake(rows=10,cols=10)
t.draw()

t.boardComp()
print(np.array(t.finalBoard))
t.draw()
# t.step(0)
# t.boardComp()
# print(np.array(t.finalBoard))
# time.sleep(20)
t.draw()
p = t.getPixels()

# t.step(0)
# t.boardComp()
# print(np.array(t.finalBoard))
# t.step()
t.draw()
print(p.shape)
print(p[80:120])
print(p.mean())
np.save("ss.npy", p)
time.sleep(5)
# time.sleep(100)