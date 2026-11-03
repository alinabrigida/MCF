import classi_progetto
import numpy as np

P1 = classi_progetto.PET_Machine(10, 5, 100)
#print(P1)
P2 = classi_progetto.PET_Machine(5, 7, 100)

prova = np.array([P1, P2])
prova_sorted = np.sort(prova)

print(prova_sorted)