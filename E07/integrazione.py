import numpy as np
import scipy
from  scipy import integrate
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import argparse


m = int(input("Inserisci la massa in kg: "))
k = int(input("Inserisci la costante elastica in N/m: "))
x_0 = int(input("Inserisci la posizione iniziale (in asse delle x) in m: "))

def V_1(x):
    return k*x**6

def T_1(x):
    return np.sqrt(8*m)/np.sqrt(V_1(x_0) - V_1(x))

x_integral = np.arange(0, 100, 0.5)
scipy_simpson_1  = integrate.simpson(  T_1(x_integral), dx=0.5) 

#print ( "Calcolo integrale con Simpson: ", scipy_simpson_1)


def V_2(x):
    return k*x**2

def T_2(x):
    return np.sqrt(8*m)/np.sqrt(V_2(x_0) - V_2(x))

scipy_simpson_2  = integrate.simpson(  T_2(x_integral), dx=0.5)



def V_3(x):
    return k*x**4

def T_3(x):
    return np.sqrt(8*m)/np.sqrt(V_3(x_0) - V_3(x))

scipy_simpson_3  = integrate.simpson(  T_3(x_integral), dx=0.5)


def V_4(x):
    return k*abs(x)**(3/2)

def T_4(x):
    return np.sqrt(8*m)/np.sqrt(V_4(x_0) - V_4(x))

scipy_simpson_4  = integrate.simpson(  T_4(x_integral), dx=0.5)

plt.plot(x_integral,T_1(x_integral), color = "royalblue", label = "Potenziale con x^6")
plt.plot(x_integral,T_2(x_integral), color = "green", label = "Potenziale con x^2")
plt.plot(x_integral,T_3(x_integral), color = "red", label = "Potenziale con x^4")
plt.plot(x_integral,T_4(x_integral), color = "orange", label = "Potenziale con |x|^(3/2)")
plt.legend()
plt.show()

print("Risultato integrale")
print('Integrale con V(x) = kx^6:             {:}'.format(scipy_simpson_1))
print('Integrale con V(x) = kx^2:             {:}'.format(scipy_simpson_2))
print('Integrale con V(x) = kx^4:             {:}'.format(scipy_simpson_3))
print('Integrale con V(x) = k|x|^(3/2):      {:}'.format(scipy_simpson_4))



def parse_arguments():
    parser = argparse.ArgumentParser(description='Seleziona il potenziale da usare',
                                     usage      ='python3 integrazione.py  --opzione')
    parser.add_argument('-V1', '--opzione1',    action='store_true',  help='Esempio di opzione booleana')
    parser.add_argument('-V2', '--opzione2',    action='store_true',  help='Esempio di opzione booleana')
    parser.add_argument('-V3', '--opzione3',    action='store_true',  help='Esempio di opzione booleana')
    parser.add_argument('-V4', '--opzione4',    action='store_true',  help='Esempio di opzione booleana')
    return  parser.parse_args()

args = parse_arguments()


if args.opzione1 == True:
    print('---------------------------------------------')
    print('Valore opzione1:', scipy_simpson_1)
    print('---------------------------------------------')

if args.opzione2 == True:
    print('---------------------------------------------')
    print('Valore opzione2:', scipy_simpson_2)
    print('---------------------------------------------')


if args.opzione3 == True:
    print('---------------------------------------------')
    print('Valore opzione3:', scipy_simpson_3)
    print('---------------------------------------------')

if args.opzione4 == True:
        print('---------------------------------------------')
        print('Valore opzione4:', scipy_simpson_4)
        print('---------------------------------------------')
