# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

from typing import Sized
import pandas as pd
import matplotlib.pyplot as plt

# Import 3GPP Table
df_rb_fr1 = pd.read_excel('3GPP_TS_38_101_RB_FR1.xlsx', index_col=0)
df_rb_fr2 = pd.read_excel('3GPP_TS_38_101_RB_FR2.xlsx', index_col=0)

# Process FR1
df_rb_fr1 = df_rb_fr1.transpose()
df_rb_fr1['BW'] = df_rb_fr1.index
df_rb_fr1['BW'] = df_rb_fr1['BW'].map(lambda x: x.lstrip('').rstrip(' MHz'))
df_rb_fr1['BW']=df_rb_fr1['BW'].astype('int64')
df_rb_fr1.set_index('BW', inplace=True)

# Process FR2
df_rb_fr2 = df_rb_fr2.transpose()
df_rb_fr2['BW'] = df_rb_fr2.index
df_rb_fr2['BW'] = df_rb_fr2['BW'].map(lambda x: x.lstrip('').rstrip(' MHz'))
df_rb_fr2['BW']=df_rb_fr2['BW'].astype('int64')
df_rb_fr2.set_index('BW', inplace=True)

# Plot FR1
df_rb_fr1.plot(style=['v-','s-','8-'], markersize=10)
plt.title('RB Count for every BW & SCS - FR1', fontsize=15)
plt.ylabel('RB Count')
plt.xlabel('NR Bandwidth (MHz)')
plt.ylim(0, 300)
plt.xlim(0, 120)
plt.grid()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='(SCS) (kHz)')

plt.show()

# Plot FR2
df_rb_fr2.plot(style=['v-','s-'], markersize=10)
plt.title('RB Count for every BW & SCS - FR2', fontsize=15)
plt.ylabel('RB Count')
plt.xlabel('NR Bandwidth (MHz)')
plt.ylim(0, 300)
plt.xlim(0, 450)
plt.grid()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='(SCS) (kHz)')

plt.show()
