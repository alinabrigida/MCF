import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#RICHIESTA 1
df2 = pd.read_csv('ExoplanetsPars_2025.csv', comment='#')

#RICHIESTA 2
print(df2.columns)

#RICHIESTA 3
df_estratto = df2.iloc[4:9]
print(df_estratto)

#RICHIESTA 4
M1 = df2['pl_bmassj']
P1 = df2['pl_orbper']

plt.scatter( P1, M1, color='royalblue', s=32, label='Massa vs Periodo')
plt.xlabel('Periodo', fontsize=10)
plt.ylabel('Massa', fontsize=10)
plt.xscale('log')
plt.yscale('log')
plt.show()

#RICHIESTA 5
R1 = df2['pl_orbsmax']
S1 = df2['st_mass']

Rapporto = R1**2/S1

plt.scatter( P1, Rapporto, color='pink', s=32, label='Rapporto vs Periodo')
plt.xlabel('Periodo', fontsize=10)
plt.ylabel('Rapporto', fontsize=10)
plt.xscale('log')
plt.yscale('log')
plt.show()

#RICHIESTA 6
sub_df = df2.loc[( df2['discoverymethod'] == 'Transit')]
sub_df1 = df2.loc[( df2['discoverymethod'] == 'Radial Velocity')]

M2 = sub_df['pl_bmassj']
P2  = sub_df['pl_orbper']

M3 = sub_df1['pl_bmassj']
P3  = sub_df1['pl_orbper']

plt.scatter( P2, M2, color='royalblue', s=32, label='Transit', alpha=0.5)
plt.scatter( P3, M3, color='orange', s=32, label='Radial Velocity', alpha = 0.5)
plt.xlabel('Perido', fontsize=10)
plt.ylabel('Massa', fontsize=10)
plt.xscale('log')
plt.yscale('log')
plt.show()


