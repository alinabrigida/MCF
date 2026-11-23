import numpy as np
import scipy
from  scipy import integrate
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import argparse
import pandas as pd

def my_derivative_vh(xx, yy, nh):
    xx = np.array(xx)
    yy = np.array(yy)
    dd = yy[nh:] - yy[:-nh]
    hh = xx[nh:] - xx[:-nh]
    for ih in range(int(nh/2)):
        dd = np.append(yy[nh-ih-1]-yy[0], dd)
        dd = np.append(dd, yy[-1]-yy[-(nh-ih)])
    
        hh = np.append(xx[nh-ih-1]-xx[0], hh)
        hh = np.append(hh, xx[-1]-xx[-(nh-ih)])
    
    return dd/hh

df = pd.read_csv('oscilloscope.csv')

t = df['time']
s1 = df['signal1']
s2 = df['signal2']

plt.plot(t, s1, color = "royalblue", label = "Signal 1")
plt.plot(t, s2, color = "green", label = "Signal 2")
plt.legend()
plt.show()

plt.plot(t, my_derivative_vh(t, s1, 49916), color = "tomato", label = "Derivative Signal 1")
plt.show()