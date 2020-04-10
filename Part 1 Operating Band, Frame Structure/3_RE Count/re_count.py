# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import 3GPP Table
df = pd.read_excel('3GPP_TS_38_101.xlsx', index_col=0)

# Create ID
df['ID'] = df['FR'] + '_' + \
    df['SCS (kHz)'].astype(str)+'_'+df['Bandwidth (MHz)'].astype(str)

# Calculate Slots/Subframe
scs = [
    (df['SCS (kHz)'] == 15),
    (df['SCS (kHz)'] == 30),
    (df['SCS (kHz)'] == 60),
    (df['SCS (kHz)'] == 120)]
slotspersubframe = [1, 2, 4, 8]

df['Slots/Subframe'] = np.select(scs, slotspersubframe, default='null')
df['Slots/Subframe'] = df['Slots/Subframe'].astype(int)

# Calculate Slots/Frame
df['Slots/Frame'] = df['Slots/Subframe'].multiply(10)

# Calculate No of Symbol/Frame
df['Normal CP Symbol/Frame'] = df['Slots/Frame'].multiply(14)
df['Extended CP Symbol/Frame'] = df['Slots/Frame'].multiply(12)

# Calculate No of RE/Frame/RB
df['Normal CP RE/Frame/RB'] = df['Normal CP Symbol/Frame'].multiply(12)
df['Extended CP RE/Frame/RB'] = df['Extended CP Symbol/Frame'].multiply(12)

# Calculate No of RE/Frame (All Bandwidth)
df['Normal CP RE/Frame'] = df['Normal CP RE/Frame/RB']*df['RB']
df['Extended CP RE/Frame'] = df['Extended CP RE/Frame/RB']*df['RB']

# Plot
df.plot(x='ID', y=['Normal CP RE/Frame', 'Extended CP RE/Frame'], kind="bar", width=1)

plt.xlabel('FR_SCS(kHz)_BW(MHz)')
plt.ylabel('RE / 10ms Frame')
plt.title('Total RE in 10ms Frame')

plt.show()

print('\n')
print(df)
