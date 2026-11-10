import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import transforms
import modulo_RandomWalk as rw

rwN = 10
rws = 2.5

for i in range(5):
    #plt.plot(rw.rw_2d(rws, rwN))
    wx,wy = rw.rw_2d(rws, rwN)
    plt.plot(wx, wy, '.')

plt.xlabel('Posizione X')
plt.ylabel('Posizione Y')
plt.show()



for i in range(5):
    #plt.plot(rw.rw_2d(rws, rwN))
    posx = np.array([0])
    posy = np.array([0])

    posx = np.append(posx, np.cumsum(wx))
    posy = np.append(posy, np.cumsum(wy))
    wx,wy = rw.rw_2d(rws, rwN)
    plt.plot(posx, posy, '-')

plt.xlabel('Posizione X')
plt.ylabel('Posizione Y')
plt.show()


