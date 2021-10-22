# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

import pandas as pd
import matplotlib.pyplot as plt

# Import 3GPP Table
df_gb_fr1 = pd.read_excel('3GPP_TS_38_101_GB_FR1.xlsx', index_col=0)
df_gb_fr2 = pd.read_excel('3GPP_TS_38_101_GB_FR2.xlsx', index_col=0)

# Process FR1
df_gb_fr1 = df_gb_fr1.transpose()
df_gb_fr1['BW'] = df_gb_fr1.index
df_gb_fr1['BW'] = df_gb_fr1['BW'].map(lambda x: x.lstrip('').rstrip(' MHz'))
df_gb_fr1['BW']=df_gb_fr1['BW'].astype('int64')
df_gb_fr1.set_index('BW', inplace=True)

df_gb_fr1_ratio = df_gb_fr1/1000
df_gb_fr1_ratio = df_gb_fr1_ratio.divide(df_gb_fr1_ratio.index, axis=0 )
df_gb_fr1_ratio = df_gb_fr1_ratio*100

# Process FR2
df_gb_fr2 = df_gb_fr2.transpose()
df_gb_fr2['BW'] = df_gb_fr2.index
df_gb_fr2['BW'] = df_gb_fr2['BW'].map(lambda x: x.lstrip('').rstrip(' MHz'))
df_gb_fr2['BW']=df_gb_fr2['BW'].astype('int64')
df_gb_fr2.set_index('BW', inplace=True)

df_gb_fr2_ratio = df_gb_fr2/1000
df_gb_fr2_ratio = df_gb_fr2_ratio.divide(df_gb_fr2_ratio.index, axis=0 )
df_gb_fr2_ratio = df_gb_fr2_ratio*100

# Plot FR1 - Guardband kHz
df_gb_fr1.plot(style=['v-','s-','8-'], markersize=10)
plt.title('Guardband for every BW & SCS - FR1', fontsize=15)
plt.ylabel('Guardband (kHz)')
plt.xlabel('NR Bandwidth (MHz)')
plt.ylim(0, 5000)
plt.xlim(0, 100)
plt.grid()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='(SCS) (kHz)')

plt.show()

# Plot FR1 - Guardband %
df_gb_fr1_ratio.plot(style=['v-','s-','8-'], markersize=10)
plt.title('Guardband Occupation (%) - FR1', fontsize=15)
plt.ylabel('Guardband %')
plt.xlabel('NR Bandwidth (MHz)')
plt.ylim(0, 20)
plt.xlim(0, 100)
plt.grid()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='(SCS) (kHz)')

plt.show()

# Plot FR2 - Guardband kHz
df_gb_fr2.plot(style=['v-','s-'], markersize=10)
plt.title('Guardband for every BW & SCS - FR2', fontsize=15)
plt.ylabel('Guardband (kHz)')
plt.xlabel('NR Bandwidth (MHz)')
plt.ylim(0, 10000)
plt.xlim(0, 450)
plt.grid()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='(SCS) (kHz)')

plt.show()

# Plot FR2 - Guardband %
df_gb_fr2_ratio.plot(style=['v-','s-'], markersize=10)
plt.title('Guardband Occupation (%) - FR2', fontsize=15)
plt.ylabel('Guardband %')
plt.xlabel('NR Bandwidth (MHz)')
plt.ylim(0, 20)
plt.xlim(0, 450)
plt.grid()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='(SCS) (kHz)')

plt.show()