import numpy as np


giorni1 = ['lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato', 'domenica']
giorni2 = ['giovedì', 'venerdì', 'sabato', 'domenica'] + lgiorni1 + ['lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato']

ottobre_dict = { i + 1 : lgiorni2[i] for i in range(len(giorni2)) }

print(ottobre_dict)
