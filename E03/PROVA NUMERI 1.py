#PROVA NUMERI 1
import sys
import math
import numpy as np

n1 = int(input('Inserisci un primo numero'))
n2 = int(input('Inserisci un secondo numero'))

#Stampa numero
print( "Primo numero: Binario {:06b}".format(n1), "Decimale {:d}".format(n1), "Esadecimale {:x}".format(n1))
print( "Secondo numero: Binario {:06b}".format(n2), "Decimale {:d}".format(n2), "Esadecimale {:x}".format(n2))

print('bitwise OR / AND Tra i due numeri')
print ("----------------------")
print ("  n1   : {:06b}".format(n1) )
print ("  n2   : {:06b}".format(n2) )
print ("----------------------")
print ("(n1|n2) Binario : {:06b}".format(n1|n2) )
print ("(n1&n2) Binario : {:06b}".format(n1&n2) )
print ("(n1|n2) Esadecimale : {:x}".format(n1|n2) )
print ("(n1&n2) Esadecimale : {:x}".format(n1&n2) )