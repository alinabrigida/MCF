import matplotlib.pyplot as plt
import numpy as np
import math

c = 3.0e8 #m/s

"""
Considero per adesso il corpo come una sfera
"""

#Collocazione massa-tumorale

Mass = np.array([0.1,0.2,0.3]) #m
v = np.random.uniform(-1, 1, size=3)
P_annichilazione = Mass + (v / np.linalg.norm(v)) * 0.003 

"""
Considero il decadimento beta in positrone che si annichila
con elettrone e poi ci sono due fotoni back to back

Il decadimento inizierà nella posizione della collocazione massa-tumorale
Il positrone si troverà a una distanza tot dalla massa tumorale da cui poi vi saranno
i fotoni btb. Il positrone percorre circa 3 mm prima di annichilirsi
"""
#Decadimento Beta

phi = np.random.uniform(0, 2 * np.pi)
cos_theta = np.random.uniform(-1, 1)
sin_theta = np.sqrt(1 - cos_theta**2)

#considero coordinate sferiche, si una simmetria sferica (isotropia)
dir_fotone1 = np.array([
    sin_theta * np.cos(phi),
    sin_theta * np.sin(phi),
    cos_theta
])
dir_fotone2 = -dir_fotone1

class PET_Machine():
    """
    Classe per rappresentare un l'apparato per l'utilizzo PET

    Parametri:
    ----------
    radius : dimensione macchinario (raggio)
    num_detectors : numero di rivelatori
    ris_spatial : dimensione dei cristalli (risoluzione spaziale)
    ris_temporal : risoluzione temporale macchinario
    pixel : numero di pixel

    """
    def __init__(self, radius, num_detectors, ris_spatial, ris_temporal, pixel):
        self.raggio = radius
        self.num_detectors = num_detectors
        self.ris_spatial = ris_spatial
        self.ris_temporal = ris_temporal
        self.pixel = pixel

    def get_detectors(self, detector):
        #Da completare con la logica dei rivelatori
        return detector

    def detect_event(gamma1, gamma2):
        R1, s1 = self.punto_impatto_sfera_3d(P_annichilazione, gamma1)
        R2, s2 = self.punto_impatto_sfera_3d(P_annichilazione, gamma2)
        return R1, R2

    def __gt__(self, other):
        return self.raggio > other.raggio

    def __lt__(self, other):
        return self.ris < other.ris

    def __str__(self):
        return 'PET: {:} - {:} - {:}'.format(self.raggio, self.ris, self.pixel)

    def __repr__(self):
        return 'PET: {:} - {:} - {:}'.format(self.raggio, self.ris, self.pixel)

    def punto_impatto_sfera_3d(self, P, u):
        """
        P: punto di partenza [x, y, z]
        u: direzione qualsiasi [ux, uy, uz]
        R: raggio della sfera dei rivelatori centrata in (0, 0, 0)
        """
        px, py, pz = float(P[0]), float(P[1]), float(P[2])
        ux, uy, uz = float(u[0]), float(u[1]), float(u[2])

        norma_u = np.sqrt(ux**2 + uy**2 + uz**2)
        ux, uy, uz = ux / norma_u, uy / norma_u, uz / norma_u

        P_dot_u = px * ux + py * uy + pz * uz #prodotto scalare
        P_quadro = px**2 + py**2 + pz**2 #norma

        # Considero la risoluzione di || p + s \scalar r ||^2 = R^2
        s = -P_dot_u + np.sqrt(P_dot_u**2 - P_quadro + R**2)

        # Punto esatto d'impatto in uno solo dei rivelatori
        impatto_x = px + s * ux
        impatto_y = py + s * uy
        impatto_z = pz + s * uz

        #per il fotone btb considero punto_impatto_sfera_3d(P, -u, R)

        return np.array([impatto_x, impatto_y, impatto_z]), s

pet = PET_Machine(
    radius=0.45, num_detectors=1000, ris_spatial=0.004, ris_temporal=3e-10, pixel=128
)
LOR = pet.detect_event(dir_fotone1, dir_fotone2)

