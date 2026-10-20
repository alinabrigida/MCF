#chieda in input un valore intero e il 
# numero di bit cui applicare delle operazioni di bit shift;

import sys
import math
import numpy as np

n = input('Inserisci un numero intero: ')
n = int(n)

b = input('Inserisci il numero di bit (intero): ')
b = int(b)

print( "Numero intero: Binario {:06b}".format(n), "Decimale {:d}".format(n), "Esadecimale {:x}".format(n))

n_plusb  = ( n << b )
n_minusb = ( n >> b )
print('n   : {:>12}  {:>6}'.format( bin(n),       hex(n)))
print('n << numero di bit forniti: {:>12}  {:>6}'.format( bin(n_plusb),  hex(n_plusb)))
print('n >> numero di bit forniti: {:>12}  {:>6}'.format( bin(n_minusb), hex(n_minusb)))

