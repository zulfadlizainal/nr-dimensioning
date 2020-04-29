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
# For SSB Periodicity, it can be set to 5, 10, 20, 40, 80, 160 ms based on spec
# PSS Size: 127 Subcarriers, 1 Symbol
# SSS Size: 127 Subcarriers, 1 Symbol
# PSS + SSS Occupancy/Sec = ((PSS Size+SSS Size)*L*SSB Burst Count in 1 Sec)/Total RE per Sec

pss_size = 127*1
sss_size = 127*1
sec = 1000


p = [5, 10, 20, 40, 80, 160]  # SSB Burst Periodicity
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

df_fr1_scs15 = df_fr1[df_fr1['SCS (kHz)'] == 15]
df_fr1_scs15 = df_fr1_scs15.drop(['FR', 'SCS (kHz)', 'RB', 'ID', 'Slots/Subframe', 'Slots/Frame',
                                  'Normal CP Symbol/Frame', 'Normal CP RE/Frame/RB', 'Normal CP RE/Frame', 'Normal CP RE/Sec'], axis=1)
df_fr1_scs15.set_index('Bandwidth (MHz)', inplace=True)
df_fr1_scs15_5ms = df_fr1_scs15.iloc[:,:4]
df_fr1_scs15_10ms = df_fr1_scs15.iloc[:,4:8]
df_fr1_scs15_20ms = df_fr1_scs15.iloc[:,8:12]
df_fr1_scs15_40ms = df_fr1_scs15.iloc[:,12:16]
df_fr1_scs15_80ms = df_fr1_scs15.iloc[:,16:20]
df_fr1_scs15_160ms = df_fr1_scs15.iloc[:,20:24]

df_fr1_scs30 = df_fr1[df_fr1['SCS (kHz)'] == 30]
df_fr1_scs30 = df_fr1_scs30.drop(['FR', 'SCS (kHz)', 'RB', 'ID', 'Slots/Subframe', 'Slots/Frame',
                                  'Normal CP Symbol/Frame', 'Normal CP RE/Frame/RB', 'Normal CP RE/Frame', 'Normal CP RE/Sec'], axis=1)
df_fr1_scs30.set_index('Bandwidth (MHz)', inplace=True)
df_fr1_scs30_5ms = df_fr1_scs30.iloc[:,:4]
df_fr1_scs30_10ms = df_fr1_scs30.iloc[:,4:8]
df_fr1_scs30_20ms = df_fr1_scs30.iloc[:,8:12]
df_fr1_scs30_40ms = df_fr1_scs30.iloc[:,12:16]
df_fr1_scs30_80ms = df_fr1_scs30.iloc[:,16:20]
df_fr1_scs30_160ms = df_fr1_scs30.iloc[:,20:24]

# FR2

# For FR2, SSB Count in SSB Burst can be up until 64 (LMax = 64)
# For SSB Periodicity, it can be set to 5, 10, 20, 40, 80, 160 ms based on spec
# PSS Size: 127 Subcarriers, 1 Symbol
# SSS Size: 127 Subcarriers, 1 Symbol
# PSS + SSS Occupancy/Sec = ((PSS Size+SSS Size)*L*SSB Burst Count in 1 Sec)/Total RE per Sec

pss_size = 127*1
sss_size = 127*1
sec = 1000


p = [5, 10, 20, 40, 80, 160]  # SSB Burst Periodicity
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

df_fr2_scs120 = df_fr2[df_fr2['SCS (kHz)'] == 120]
df_fr2_scs120 = df_fr2_scs120.drop(['FR', 'SCS (kHz)', 'RB', 'ID', 'Slots/Subframe', 'Slots/Frame',
                                    'Normal CP Symbol/Frame', 'Normal CP RE/Frame/RB', 'Normal CP RE/Frame', 'Normal CP RE/Sec'], axis=1)
df_fr2_scs120.set_index('Bandwidth (MHz)', inplace=True)
df_fr2_scs120_5ms = df_fr2_scs120.iloc[:,:7]
df_fr2_scs120_10ms = df_fr2_scs120.iloc[:,7:14]
df_fr2_scs120_20ms = df_fr2_scs120.iloc[:,14:21]
df_fr2_scs120_40ms = df_fr2_scs120.iloc[:,21:28]
df_fr2_scs120_80ms = df_fr2_scs120.iloc[:,28:35]
df_fr2_scs120_160ms = df_fr2_scs120.iloc[:,35:42]

df_fr2_scs240 = df_fr2[df_fr2['SCS (kHz)'] == 240]
df_fr2_scs240 = df_fr2_scs240.drop(['FR', 'SCS (kHz)', 'RB', 'ID', 'Slots/Subframe', 'Slots/Frame',
                                    'Normal CP Symbol/Frame', 'Normal CP RE/Frame/RB', 'Normal CP RE/Frame', 'Normal CP RE/Sec'], axis=1)
df_fr2_scs240.set_index('Bandwidth (MHz)', inplace=True)

# Plot

fig1, axes = plt.subplots(nrows=2, ncols=3)

df_fr1_scs15_5ms.plot(kind='line', style='.--', ax=axes[0,0], ylim=[0,15], xlim=[0,100])
df_fr1_scs15_10ms.plot(kind='line', style='.--', ax=axes[0,1], ylim=[0,15], xlim=[0,100])
df_fr1_scs15_20ms.plot(kind='line', style='.--', ax=axes[0,2], ylim=[0,15], xlim=[0,100])
df_fr1_scs15_40ms.plot(kind='line', style='.--', ax=axes[1,0], ylim=[0,5], xlim=[0,100])
df_fr1_scs15_80ms.plot(kind='line', style='.--', ax=axes[1,1], ylim=[0,5], xlim=[0,100])
df_fr1_scs15_160ms.plot(kind='line', style='.--', ax=axes[1,2], ylim=[0,5], xlim=[0,100])

fig1.suptitle('PSS+SSS Occupancy (%) for FR = 1, SCS = 15 kHz\nL = SSB Count in SSB Burst Set, p = SSB Periodicity')
# fig1.text(0.5, 0.04, 'Bandwidth (MHz)', ha='center')
fig1.text(0.04, 0.5, 'Occupancy (%)', va='center', rotation='vertical')

plt.show()

fig2, axes = plt.subplots(nrows=2, ncols=3)

df_fr1_scs30_5ms.plot(kind='line', style='.--', ax=axes[0,0], ylim=[0,15], xlim=[0,100])
df_fr1_scs30_10ms.plot(kind='line', style='.--', ax=axes[0,1], ylim=[0,15], xlim=[0,100])
df_fr1_scs30_20ms.plot(kind='line', style='.--', ax=axes[0,2], ylim=[0,15], xlim=[0,100])
df_fr1_scs30_40ms.plot(kind='line', style='.--', ax=axes[1,0], ylim=[0,5], xlim=[0,100])
df_fr1_scs30_80ms.plot(kind='line', style='.--', ax=axes[1,1], ylim=[0,5], xlim=[0,100])
df_fr1_scs30_160ms.plot(kind='line', style='.--', ax=axes[1,2], ylim=[0,5], xlim=[0,100])

fig2.suptitle('PSS+SSS Occupancy (%) for FR = 1, SCS = 30 kHz\nL = SSB Count in SSB Burst Set, p = SSB Periodicity')
# fig2.text(0.5, 0.04, 'Bandwidth (MHz)', ha='center')
fig2.text(0.04, 0.5, 'Occupancy (%)', va='center', rotation='vertical')

plt.show()

fig3, axes = plt.subplots(nrows=2, ncols=3)

df_fr2_scs120_5ms.plot(kind='line', style='.--', ax=axes[0,0], ylim=[0,15], xlim=[0,400])
df_fr2_scs120_10ms.plot(kind='line', style='.--', ax=axes[0,1], ylim=[0,15], xlim=[0,400])
df_fr2_scs120_20ms.plot(kind='line', style='.--', ax=axes[0,2], ylim=[0,15], xlim=[0,400])
df_fr2_scs120_40ms.plot(kind='line', style='.--', ax=axes[1,0], ylim=[0,5], xlim=[0,400])
df_fr2_scs120_80ms.plot(kind='line', style='.--', ax=axes[1,1], ylim=[0,5], xlim=[0,400])
df_fr2_scs120_160ms.plot(kind='line', style='.--', ax=axes[1,2], ylim=[0,5], xlim=[0,400])

fig3.suptitle('PSS+SSS Occupancy (%) for FR = 2, SCS = 120 kHz\nL = SSB Count in SSB Burst Set, p = SSB Periodicity')
# fig3.text(0.5, 0.04, 'Bandwidth (MHz)', ha='center')
fig3.text(0.04, 0.5, 'Occupancy (%)', va='center', rotation='vertical')

plt.show()