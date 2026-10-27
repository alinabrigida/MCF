import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('kplr010666592-2011240104155_slc.csv')

#RICHIESTA 2
print(df.columns)

#RICHIESTA 3
F1 = df['SAP_FLUX']
T1 = df['TIME']

fig, axs = plt.subplots(2, 2, figsize=(10, 8)) #sono 2 righe e 2 colonne

axs[0, 0].plot(T1, F1)
axs[0, 0].set_ylabel('Flux (e-/s)')
axs[0, 0].set_xlabel('Time (BJD - 2454833)')


#RICHIESTA 4
F2 = F1.copy()
T2 = T1.copy()

axs[0, 1].plot(T1, F1, 'o', color='pink', ms = 2, label='Flux vs Time' )
axs[0, 1].set_ylabel('Flux (e-/s)')
axs[0, 1].set_xlabel('Time (BJD - 2454833)')
axs[0, 1].legend(fontsize=12)



#RICHIESTA 5
F3 = F1.copy()
T3 = T1.copy()

axs[1, 0].errorbar(T3, F3, yerr=df['PDCSAP_FLUX_ERR'], fmt='o', color = 'darkblue', ms = 2, label='Flux vs Time' )
axs[1, 0].set_ylabel('Flux (e-/s)')
axs[1, 0].set_xlabel('Time (BJD - 2454833)')
axs[1, 0].legend(fontsize = 12)

#plt.savefig('grafico_richiesta1.png')

#RICHIESTA 6
indice_minimo = df["SAP_FLUX"].idxmin()
intervallo_inizio = indice_minimo - 200
intervallo_fine = indice_minimo + 200
df_selezionato = df.loc[intervallo_inizio:intervallo_fine]
T6 = df_selezionato["TIME"]
F6 = df_selezionato["SAP_FLUX"]
err6 = df_selezionato["SAP_FLUX_ERR"]

axs[1, 1].errorbar(T6, F6, yerr= err6, fmt='o', color = 'darkgreen', ms = 2, label='Flux vs Time' )
axs[1, 1].set_ylabel('Flux (e-/s)')
axs[1, 1].set_xlabel('Time (BJD - 2454833)')
axs[1, 1].legend(fontsize = 12)

plt.show()

#RICHIESTA 7
fig, ax = plt.subplots(figsize=(12,6))

ax.errorbar(T3, F3, yerr=df['PDCSAP_FLUX_ERR'], fmt='o', color = 'darkblue', ms = 2, label='Flux vs Time' )
ax.set_ylabel('Flux (e-/s)')
ax.set_xlabel('Time (BJD - 2454833)')
ax.legend(fontsize = 12)

ins_ax = ax.inset_axes([0.55, 0.55, 0.35, 0.35]) # w.r.t. ax
ins_ax.errorbar(T6, F6, yerr= err6, fmt='o', color = 'darkgreen', ms = 2, label='Flux vs Time')
ins_ax.set_ylabel('Flux (e-/s)')
ins_ax.set_xlabel('Time (BJD - 2454833)')
ins_ax.legend(fontsize = 12)

plt.show()




