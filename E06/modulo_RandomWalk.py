import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import transforms

def rw_2d(s, N):
    phi = np.random.random(N)*2*np.pi
    deltax = s * np.cos(phi)
    deltay = s * np.sin(phi)
    return deltax, deltay



