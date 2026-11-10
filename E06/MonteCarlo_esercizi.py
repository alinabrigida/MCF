#MonteCarlo 1

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import transforms

#Metodo Hit or Miss

def parabola(x):
    yy = np.zeros(len(x))
    mask = (x >= 0) & (x <= 10)

    yy[mask] = 3*x**2/1000
    return yy

valori_x = np.arange(0,10, 0.1)
y_parabola = (valori_x)

plt.plot(valori_x, y_parabola)
plt.show()

nsample= 100000

#generazione numeri random
x_random = np.random.uniform(low=0, high=10, size=nsample)
y_random = np.random.random(nsample)

plt.scatter(x_random, y_random, marker='.', color='darkblue')
plt.xlabel('Hit or Miss X')
plt.ylabel('Hit or Miss Y')
plt.show()

mask_selezione = y_random <= parabola(x_random)
x_selezionati = x_random[mask_selezione]

plt.scatter(x_random[mask_selezione], y_random[mask_selezione], marker='.', color='yellow')
plt.xlabel('Hit or Miss Selected X')
plt.ylabel('Hit or Miss Selected Y')
plt.show()

#istrogramma
plt.hist(x_random, bins = 200, range = (0,10), color='darkblue', label = 'Valori Generati')
plt.hist(x_selezionati, bins = 200, range = (0,10), color='yellow', label = 'Valori Selezionati')
plt.xlabel('Hit or Miss X')
plt.ylabel('Hit or Miss Y')
plt.legend()
plt.show()