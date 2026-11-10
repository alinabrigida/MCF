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
y_parabola = parabola(valori_x)

#Metodo Funzione Cumulativa

def para_cumulativa(x):
    yy_cum = np.zeros(len(x))
    mask = (x >= 0) & (x <= 10)
    
    yy_cum[mask] = x/1000
    return yy_cum

plt.plot(valori_x, parabola(valori_x), color='cornflowerblue',label='onda quadra')
plt.plot(valori_x, para_cumulativa(valori_x),      color='darkgreen',       label='funzione cumulativa')
plt.grid()
plt.xlabel('x')
plt.ylabel('Valore Funzione')
plt.legend()
plt.show()

def inv_cumulativa(y):
    mask = (y >= 0) & (y <= 1)
    xx = np.zeros(len(y))
    xx[mask] = (1000*y[mask])**(1/3)
    return xx

y_invcumulativa = np.arange(0,1,0.1)
x_invcumulativa = inv_cumulativa(y_invcumulativa)

plt.plot(y_invcumulativa, x_invcumulativa, color = 'red', label = 'Funzione cumulativa inversa')
plt.plot(y_parabola, valori_x, color = 'cornflowerblue', label = 'Funzione cumulativa ruotata')
plt.grid()
plt.xlabel('y')
plt.ylabel(r'$c^{-1}(y)$')
plt.legend()
plt.show()

#considero valori di y random tra 0 e 1 e tramite la cumulativa inv ricavo la x

nsamples = 250000
y_random = np.random.random(nsamples)
x_random = inv_cumulativa(y_random)

fig, ax = plt.subplots(1,2, figsize=(11,5))
ax[0].hist(y_random, bins=200, range=(0,1), color='pink',   ec='violet')
ax[0].set_title('Distribuzione y Cumulativa')
ax[0].set_xlabel('y cumulativa')

ax[1].hist(x_random, bins=200, range=(0,5), color='orange', ec='darkorange')
ax[1].set_title('Distribuzione secondo la funzione parabola')
ax[1].set_xlabel('x')
plt.show()
