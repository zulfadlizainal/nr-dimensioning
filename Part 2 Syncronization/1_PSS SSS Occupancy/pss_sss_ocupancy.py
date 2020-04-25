# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import RE Count Table

df_fr1 = pd.read_excel('FR1_Re_Count.xlsx', index_col=0)
df_fr2 = pd.read_excel('FR2_Re_Count.xlsx', index_col=0)

# Only 15, 30, 120, 240 kHz SCS supported for SSB. So filter out 60 kHz SCS

df_fr1 = df_fr1.loc[(df_fr1['SCS (kHz)'] == 15) | (df_fr1['SCS (kHz)'] == 30)]
df_fr2 = df_fr2.loc[(df_fr2['SCS (kHz)'] == 120) |
                    (df_fr2['SCS (kHz)'] == 240)]

# Change RE/Frame (10ms) to RE/Sec (1Sec)

df_fr1['Normal CP RE/Sec'] = df_fr1['Normal CP RE/Frame']*100
df_fr2['Normal CP RE/Sec'] = df_fr2['Normal CP RE/Frame']*100


############################### Simulation Info ################################

# FR1

# For FR1, SSB Count in SSB Burst can be up until 4 and 8 (LMax = 4 for < 3GHz, LMax = 8 for ~3-6GHz)
# For SSB Periodicity, it can be set to 5, 10, 15, 20, 40, 80, 160 ms based on spec
# PSS Size: 127 Subcarriers, 1 Symbol
# SSS Size: 127 Subcarriers, 1 Symbol
# PSS + SSS Occupancy/Sec = ((PSS Size+SSS Size)*L*SSB Burst Count in 1 Sec)/Total RE per Sec

pss_size = 127*1
sss_size = 127*1
sec = 1000


p = [5, 10, 15, 20, 40, 80, 160]  # SSB Burst Periodicity
i = 0                             # Counter
index = 0

for index in range(len(p)):

    l = 1                         # L = No of SSB in 1 SSB Burst (Max = 8)

    for index in range(len(p)):

        for index in range(len(p)):

            if i < len(p):

                if l <= 8:

                    df_fr1[f'L = {l}, p = {p[i]} ms'] = (
                        ((pss_size+sss_size)*l*(np.floor(sec/p[i])))/df_fr1['Normal CP RE/Sec'])*100

                    l = l*2

                else:
                    None

            else:
                None

    i = i+1


# FR2

# For FR2, SSB Count in SSB Burst can be up until 64 (LMax = 64)
# For SSB Periodicity, it can be set to 5, 10, 15, 20, 40, 80, 160 ms based on spec
# PSS Size: 127 Subcarriers, 1 Symbol
# SSS Size: 127 Subcarriers, 1 Symbol
# PSS + SSS Occupancy/Sec = ((PSS Size+SSS Size)*L*SSB Burst Count in 1 Sec)/Total RE per Sec

pss_size = 127*1
sss_size = 127*1
sec = 1000


p = [5, 10, 15, 20, 40, 80, 160]  # SSB Burst Periodicity
i = 0                             # Counter
index = 0

for index in range(len(p)):

    l = 1                         # L = No of SSB in 1 SSB Burst (Max = 64)

    for index in range(len(p)):

        for index in range(len(p)):

            if i < len(p):

                if l <= 64:

                    df_fr2[f'L = {l}, p = {p[i]} ms'] = (
                        ((pss_size+sss_size)*l*(np.floor(sec/p[i])))/df_fr2['Normal CP RE/Sec'])*100

                    l = l*2

                else:
                    None

            else:
                None

    i = i+1


df_fr1.to_excel('FR1.xlsx')
df_fr2.to_excel('FR2.xlsx')

# Plot

df_fr1.plot(x='ID', y=['L = 1, p = 5 ms', 'L = 2, p = 5 ms', 'L = 4, p = 5 ms',	'L = 8, p = 5 ms',
                       'L = 1, p = 10 ms', 'L = 2, p = 10 ms', 'L = 4, p = 10 ms', 'L = 8, p = 10 ms',
                       'L = 1, p = 15 ms', 'L = 2, p = 15 ms', 'L = 4, p = 15 ms', 'L = 8, p = 15 ms',
                       'L = 1, p = 20 ms', 'L = 2, p = 20 ms', 'L = 4, p = 20 ms', 'L = 8, p = 20 ms',
                       'L = 1, p = 40 ms', 'L = 2, p = 40 ms', 'L = 4, p = 40 ms', 'L = 8, p = 40 ms',
                       'L = 1, p = 80 ms', 'L = 2, p = 80 ms', 'L = 4, p = 80 ms', 'L = 8, p = 80 ms',
                       'L = 1, p = 160 ms',	'L = 2, p = 160 ms', 'L = 4, p = 160 ms', 'L = 8, p = 160 ms'
                       ], kind="line")

plt.xlabel('FR_SCS(kHz)_BW(MHz)')
plt.ylabel('PSS+SSS Occupancy %')
plt.title('PSS+SSS Occupancy %')

plt.show()
