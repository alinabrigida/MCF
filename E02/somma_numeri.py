import numpy as np

nn = input('Immettere un numero intero: ')

nn1 = int(nn)

somma = 0
for i in range(nn1 + 1):
	somma = somma + i

print('Somma dei primi', nn ,'numeri naturali è  ', somma)
