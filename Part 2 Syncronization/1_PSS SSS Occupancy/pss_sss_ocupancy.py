# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import RE Count Table

df_fr1 = pd.read_excel('FR1_Re_Count.xlsx', index_col=0)
df_fr2 = pd.read_excel('FR2_Re_Count.xlsx', index_col=0)

# Only 15, 30, 120, 240 kHz SCS supported for SSB. So filter 60 kHz SCS

df_fr1 = df_fr1.loc[(df_fr1['SCS (kHz)'] == 15) | (df_fr1['SCS (kHz)'] == 30)]
df_fr2 = df_fr2.loc[(df_fr2['SCS (kHz)'] == 120) |
                    (df_fr2['SCS (kHz)'] == 240)]

############################ FR1 PSS + SSS Occupancy ############################

# For FR1, SSB Count in SSB Burst can be up until 4 and 8 (LMax = 4 for < 3GHz, 8 for ~3-6GHz)
# For SSB Periodicity, it can be set to 5, 10, 15, 20, 40, 80, 160 ms based on spec
# Simulation will only consider SSB periodicity 5-20ms
# PSS Size: 127 Suncarriers, 1 Symbol
# SSS Size: 127 Suncarriers, 1 Symbol

# PSS + SSS Occupancy for LMax = 4 (Normal CP)

df_fr1['PSS+SSS Occupancy/Frame % (L = 4, SSB Burst Periodicity = 5ms)'] = ((
    ((127*1)+(127*1))*4*2)/df_fr1['Normal CP RE/Frame'])*100  # ((PSS Size+SSS Size)*L*SSB Burst Count in a Frame)/Total RE per Frame

df_fr1['PSS+SSS Occupancy/Frame % (L = 4, SSB Burst Periodicity = 10ms)'] = ((
    ((127*1)+(127*1))*4*1)/df_fr1['Normal CP RE/Frame'])*100  # ((PSS Size+SSS Size)*L*SSB Burst Count in a Frame)/Total RE per Frame

df_fr1['PSS+SSS Occupancy/Frame % (L = 4, SSB Burst Periodicity = 15ms)'] = ((
    ((127*1)+(127*1))*4*1)/df_fr1['Normal CP RE/Frame'])*100  # ((PSS Size+SSS Size)*L*SSB Burst Count in a Frame)/Total RE per Frame

df_fr1['PSS+SSS Occupancy/Frame % (L = 4, SSB Burst Periodicity = 20ms)'] = ((
    ((127*1)+(127*1))*4*1)/df_fr1['Normal CP RE/Frame'])*100  # ((PSS Size+SSS Size)*L*SSB Burst Count in a Frame)/Total RE per Frame

# PSS + SSS Occupancy for LMax = 8 (Normal CP)

df_fr1['PSS+SSS Occupancy/Frame % (L = 8, SSB Burst Periodicity = 5ms)'] = ((
    ((127*1)+(127*1))*8*2)/df_fr1['Normal CP RE/Frame'])*100  # ((PSS Size+SSS Size)*L*SSB Burst Count in a Frame)/Total RE per Frame

df_fr1['PSS+SSS Occupancy/Frame % (L = 8, SSB Burst Periodicity = 10ms)'] = ((
    ((127*1)+(127*1))*8*1)/df_fr1['Normal CP RE/Frame'])*100  # ((PSS Size+SSS Size)*L*SSB Burst Count in a Frame)/Total RE per Frame

df_fr1['PSS+SSS Occupancy/Frame % (L = 8, SSB Burst Periodicity = 15ms)'] = ((
    ((127*1)+(127*1))*8*1)/df_fr1['Normal CP RE/Frame'])*100  # ((PSS Size+SSS Size)*L*SSB Burst Count in a Frame)/Total RE per Frame

df_fr1['PSS+SSS Occupancy/Frame % (L = 8, SSB Burst Periodicity = 20ms)'] = ((
    ((127*1)+(127*1))*8*1)/df_fr1['Normal CP RE/Frame'])*100  # ((PSS Size+SSS Size)*L*SSB Burst Count in a Frame)/Total RE per Frame


############################ FR2 PSS + SSS Occupancy ############################

# For FR2, SSB Count in SSB Burst can be up until 64 (LMax = 64 for > 6GHz)
# For SSB Periodicity, it can be set to 5, 10, 15, 20, 40, 80, 160 ms based on spec
# Simulation will only consider SSB periodicity 5-20ms
# PSS Size: 127 Suncarriers, 1 Symbol
# SSS Size: 127 Suncarriers, 1 Symbol

# PSS + SSS Occupancy for LMax = 64 (Normal CP)

df_fr2['PSS+SSS Occupancy/Frame % (L = 64, SSB Burst Periodicity = 5ms)'] = ((
    ((127*1)+(127*1))*64*2)/df_fr2['Normal CP RE/Frame'])*100  # ((PSS Size+SSS Size)*L*SSB Burst Count in a Frame)/Total RE per Frame

df_fr2['PSS+SSS Occupancy/Frame % (L = 64, SSB Burst Periodicity = 10ms)'] = ((
    ((127*1)+(127*1))*64*1)/df_fr2['Normal CP RE/Frame'])*100  # ((PSS Size+SSS Size)*L*SSB Burst Count in a Frame)/Total RE per Frame

df_fr2['PSS+SSS Occupancy/Frame % (L = 64, SSB Burst Periodicity = 15ms)'] = ((
    ((127*1)+(127*1))*64*1)/df_fr2['Normal CP RE/Frame'])*100  # ((PSS Size+SSS Size)*L*SSB Burst Count in a Frame)/Total RE per Frame

df_fr2['PSS+SSS Occupancy/Frame % (L = 64, SSB Burst Periodicity = 20ms)'] = ((
    ((127*1)+(127*1))*64*1)/df_fr2['Normal CP RE/Frame'])*100  # ((PSS Size+SSS Size)*L*SSB Burst Count in a Frame)/Total RE per Frame


# Plot FR1 with LMax = 4
df_fr1.plot(x='ID', y=['PSS+SSS Occupancy/Frame % (L = 4, SSB Burst Periodicity = 5ms)', 'PSS+SSS Occupancy/Frame % (L = 4, SSB Burst Periodicity = 10ms)',
                       'PSS+SSS Occupancy/Frame % (L = 4, SSB Burst Periodicity = 15ms)', 'PSS+SSS Occupancy/Frame % (L = 4, SSB Burst Periodicity = 20ms)'], kind="bar", width=1)

plt.xlabel('FR_SCS(kHz)_BW(MHz)')
plt.ylabel('PSS + SSS Occupancy (%)')
plt.legend(['SSB Burst Periodicity = 5ms', 'SSB Burst Periodicity = 10ms',
            'SSB Burst Periodicity = 15ms', 'SSB Burst Periodicity = 20ms'])
plt.title('FR1 PSS + SSS Occupancy per 10ms Frame (%)\nL = 4')

plt.show()

print('\n')

# Plot FR1 with LMax = 8
df_fr1.plot(x='ID', y=['PSS+SSS Occupancy/Frame % (L = 8, SSB Burst Periodicity = 5ms)', 'PSS+SSS Occupancy/Frame % (L = 8, SSB Burst Periodicity = 10ms)',
                       'PSS+SSS Occupancy/Frame % (L = 8, SSB Burst Periodicity = 15ms)', 'PSS+SSS Occupancy/Frame % (L = 8, SSB Burst Periodicity = 20ms)'], kind="bar", width=1)

plt.xlabel('FR_SCS(kHz)_BW(MHz)')
plt.ylabel('PSS + SSS Occupancy (%)')
plt.legend(['SSB Burst Periodicity = 5ms', 'SSB Burst Periodicity = 10ms',
            'SSB Burst Periodicity = 15ms', 'SSB Burst Periodicity = 20ms'])
plt.title('FR1 PSS + SSS Occupancy per 10ms Frame (%)\nL = 8')

plt.show()

print('\n')

# Plot FR2 with LMax = 64
df_fr2.plot(x='ID', y=['PSS+SSS Occupancy/Frame % (L = 64, SSB Burst Periodicity = 5ms)', 'PSS+SSS Occupancy/Frame % (L = 64, SSB Burst Periodicity = 10ms)',
                       'PSS+SSS Occupancy/Frame % (L = 64, SSB Burst Periodicity = 15ms)', 'PSS+SSS Occupancy/Frame % (L = 64, SSB Burst Periodicity = 20ms)'], kind="bar", width=1)

plt.xlabel('FR_SCS(kHz)_BW(MHz)')
plt.ylabel('PSS + SSS Occupancy (%)')
plt.legend(['SSB Burst Periodicity = 5ms', 'SSB Burst Periodicity = 10ms',
            'SSB Burst Periodicity = 15ms', 'SSB Burst Periodicity = 20ms'])
plt.title('FR1 PSS + SSS Occupancy per 10ms Frame (%)\nL = 64')

plt.show()