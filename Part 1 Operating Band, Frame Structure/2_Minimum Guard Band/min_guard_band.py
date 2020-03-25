# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

import pandas as pd
import matplotlib.pyplot as plt

# Import 3GPP Table
df_gb_fr1 = pd.read_excel('3GPP_TS_38_101_GB_FR1.xlsx', index_col=0)
df_gb_fr2 = pd.read_excel('3GPP_TS_38_101_GB_FR2.xlsx', index_col=0)

# Plot FR1
df_gb_fr1.plot.bar()
plt.title('Minimum Guard Band for every BW & SCS - FR1 (kHz)')
plt.ylabel('Minimum Guard Band (kHz)')
plt.xlabel('Sub Carrier Spacing (SCS) (kHz)')
plt.ylim(0, 10000)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='NR Bandwidth')

# Plot FR2
df_gb_fr2.plot.bar()
plt.title('Minimum Guard Band for every BW & SCS - FR2 (kHz)')
plt.ylabel('Minimum Guard Band (kHz)')
plt.xlabel('Sub Carrier Spacing (SCS) (kHz)')
plt.ylim(0, 10000)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='NR Bandwidth')

plt.show()