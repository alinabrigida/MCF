import numpy as np

def somma_naturali(n):

    """
    Funzione che restituisca la somma dei primi n numeri naturali, con n da passare tramite un argomento

    """
    sum = n*(n + 1) / 2
    return int(sum)

def somma_radici(n):
    """
    Funzione che restituisca la somma delle radici dei primi n numeri naturali, con n da passare tramite un argomento
    """
    sum = 0
    for i in range(n):
        sum = sum + np.sqrt(i)
    return sum

def somma_prodotti(n):
    """
    Funzione che restituisca la somma e il prodotto dei primi n numeri naturali, con n da passare tramite un argomento
    """
    sum = n*(n + 1) / 2
    prod = 1
    for i in range(n):
        prod = prod * i
    return int(sum), int(prod)

def sommatoria(n, alpha = 1):
    """
    Funzione che restituisca sommatoria con n da passare tramite un argomento e 
    da passare come argomento opzionale con valore di default pari a 1
    """

    sum = 0
    for i in range(n):
        sum = sum + (i**alpha)
    return int(sum)