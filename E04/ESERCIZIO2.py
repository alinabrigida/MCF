import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import pandas as pd


solar_system_data = {
    'pl_name': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
    'hostname': ['Sun', 'Sun', 'Sun', 'Sun', 'Sun', 'Sun', 'Sun', 'Sun'],
    'pl_orbper': [87.97, 224.7, 365.25, 686.98, 4332.59, 10759.22, 30685.4, 60189.0],
    'pl_orbsmax': [0.387, 0.723, 1.000, 1.524, 5.204, 9.582, 19.201, 30.047],
    'pl_bmassj': [0.000174, 0.00257, 0.003146, 0.000338, 1.0, 0.299, 0.046, 0.054],
    'st_mass': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], #massa solare per Sole è sempre 1
}

df_solar = pd.DataFrame(solar_system_data)
print(df_solar[['pl_name', 'pl_orbper', 'pl_bmassj', 'pl_orbsmax']])


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

SOLAR_SYSTEM_MASS = df_solar['pl_bmassj']
SOLAR_SYSTEM_PERIOD = df_solar['pl_orbper']

plt.scatter( P1, M1, color='royalblue', s=20, label='Pianeti Extrasolari', alpha=0.5)
plt.scatter( SOLAR_SYSTEM_PERIOD, SOLAR_SYSTEM_MASS, color='red', s=20, label='Sistema Solare', alpha=0.5)
plt.xlabel('Period[days]', fontsize=10)
plt.ylabel('Planet Mass[$m_j$]', fontsize=10)
plt.xscale('log')
plt.yscale('log')
plt.legend(loc="lower right", fontsize=10)
plt.show()







#RICHIESTA 5
R1 = df2['pl_orbsmax']
S1 = df2['st_mass']
SOLAR_SYSTEM_ORBSMAX = df_solar['pl_orbsmax']
SOLAR_SYSTEM_STMASS = df_solar['st_mass']

Rapporto_extra = R1**2/S1
Rapporto_solar = SOLAR_SYSTEM_ORBSMAX**2/SOLAR_SYSTEM_STMASS

plt.scatter( P1, Rapporto_extra, color='royalblue', s=20, label='Pianeti Extrasolari', alpha=0.5)
plt.scatter( SOLAR_SYSTEM_PERIOD, Rapporto_solar, color='red', s=20, label='Sistema Solare', alpha=0.5)
plt.xlabel('Period[days]', fontsize=10)
plt.ylabel('$R_{max}^2/m_* [m^2/days]$', fontsize=10)
plt.xscale('log')
plt.yscale('log')
plt.legend(loc="lower right", fontsize=10)
plt.show()





#RICHIESTA 6
sub_df = df2.loc[( df2['discoverymethod'] == 'Transit')]
sub_df1 = df2.loc[( df2['discoverymethod'] == 'Radial Velocity')]
#per sistema solare non è necessario fare un sub_df in quanto non si ha la colonna sulla tipologia di scoperta

M2 = sub_df['pl_bmassj']
P2  = sub_df['pl_orbper']

M3 = sub_df1['pl_bmassj']
P3  = sub_df1['pl_orbper']

plt.scatter( P2, M2, color='royalblue', s=20, label='Transit', alpha=0.7)
plt.scatter( P3, M3, color='orange', s=20, label='Radial Velocity', alpha = 0.7)
plt.scatter(SOLAR_SYSTEM_PERIOD, SOLAR_SYSTEM_MASS, color='red', s=20, label='Sistema Solare', alpha=0.7)
plt.xlabel('Period[days]', fontsize=10)
plt.ylabel('Planet Mass[$m_j$]', fontsize=10)
plt.xscale('log')
plt.yscale('log')
plt.legend(loc = 'lower left', fontsize=10)
plt.show()


#RICHIESTA 7
plt.hist(M2, bins=50, color='royalblue', label="Transit", alpha=0.6)
plt.hist(M3, bins=50, color='orange', label="Radial Velocity", alpha=0.6)
plt.xlabel("Planet Mass[$m_j$]")
plt.ylabel("Counts")
plt.title("Istogramma sovrapposto delle masse per Metodo di Scoperta")
plt.legend()
plt.show()

#RICHIESTA 8
plt.hist(np.log(M2), bins=50, color='royalblue', label="Transit", alpha=0.6)
plt.hist(np.log(M3), bins=50, color='orange', label="Radial Velocity", alpha=0.6)
plt.xlabel("Planet Mass[$m_j$]")
plt.ylabel("Counts")
plt.title("Istogramma sovrapposto delle masse per Metodo di Scoperta")
plt.legend()
plt.show()


