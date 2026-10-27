import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('kplr010666592-2011240104155_slc.csv')

#RICHIESTA 2
print(df.columns)

#RICHIESTA 3
F1 = df['SAP_FLUX']
T1 = df['TIME']

plt.plot(T1, F1)
plt.ylabel('Flux (e-/s)')
plt.xlabel('Time (BJD - 2454833)')

plt.show()

#RICHIESTA 4
F2 = F1.copy()
T2 = T1.copy()

plt.plot(T1, F1, 'o', color='pink', label='Flux vs Time' )
plt.ylabel('Flux (e-/s)')
plt.xlabel('Time (BJD - 2454833)')
plt.legend(fontsize=12)

plt.show()


#RICHIESTA 5
F3 = F1.copy()
T3 = T1.copy()

plt.errorbar(T3, F3, yerr=df['PDCSAP_FLUX_ERR'], fmt='o', color = 'darkblue', label='Flux vs Time' )
plt.ylabel('Flux (e-/s)')
plt.xlabel('Time (BJD - 2454833)')
plt.legend(fontsize = 12)

#plt.savefig('grafico_richiesta1.png')
plt.show()

#RICHIESTA 6
indice_minimo = df["SAP_FLUX"].idxmin()
intervallo_inizio = indice_minimo - 200
intervallo_fine = indice_minimo + 200
df_selezionato = df.loc[intervallo_inizio:intervallo_fine]
T6 = df_selezionato["TIME"]
F6 = df_selezionato["SAP_FLUX"]
err6 = df_selezionato["SAP_FLUX_ERR"]

plt.errorbar(T6, F6, yerr= err6, fmt='o', color = 'darkgreen', label='Flux vs Time' )
plt.ylabel('Flux (e-/s)')
plt.xlabel('Time (BJD - 2454833)')
plt.legend(fontsize = 12)

plt.show()

#RICHIESTA 7
fig, ax = plt.subplots(figsize=(12,6))

ax.errorbar(T3, F3, yerr=df['PDCSAP_FLUX_ERR'], fmt='o', color = 'darkblue', label='Flux vs Time' )
ax.set_ylabel('Flux (e-/s)')
ax.set_xlabel('Time (BJD - 2454833)')
ax.legend(fontsize = 12)

ins_ax = ax.inset_axes([0.55, 0.55, 0.35, 0.35]) # w.r.t. ax
ins_ax.errorbar(T6, F6, yerr= err6, fmt='o', color = 'darkgreen', label='Flux vs Time')
ins_ax.set_ylabel('Flux (e-/s)')
ins_ax.set_xlabel('Time (BJD - 2454833)')
ins_ax.legend(fontsize = 12)

plt.show()




