import matplotlib.pyplot as plt
import numpy as np
import math


class PET_Machine():
    """
    Classe per rappresentare un l'apparato per l'utilizzo PET

    Parametri:
    ----------
    raggio : dimensione macchinario (raggio)
    ris : risoluzione temporale macchinario
    pixel : numero di pixel

    inclinazione : inclinazione macchinario

    """
    def __init__(self, raggio, ris, pixel):
        self.raggio = raggio
        self.ris = ris
        self.pixel = pixel


    def __gt__(self, other):
        return self.raggio > other.raggio

    def __lt__(self, other):
        return self.ris < other.ris

    def __str__(self):
        return 'PET: {:} - {:} - {:}'.format(self.raggio, self.ris, self.pixel)

    def __repr__(self):
        return 'PET: {:} - {:} - {:}'.format(self.raggio, self.ris, self.pixel)
