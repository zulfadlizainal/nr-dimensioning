# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

from pagingparam import *
from paginglib import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

######### Paging Blocking Probability - Set of Assumptions #########

pd_core = pagingvolume.paging_core(mt_rrc_hour, tac_size)
pd_ran = pagingvolume.paging_ran(mo_rrc_hour, mt_rrc_hour, rrc_inactive_hour, ran_noti_area)
pdem = pagingvolume.paging_demand(pd_core, pd_ran)
po = pagingoccasion.paging_occassion(N, Ns)
ue_per_paging_msg = pagingue.ue_per_paging_msg(pdem, po)

block_prob = ue_per_paging_msg.copy()
for i in range(len(block_prob)):
    block_prob.loc[i, ['block_prob_%']] = pagingblock.ErlangB(block_prob.iloc[i]['ue_per_paging_msg'], max_ue_per_paging_msg_val)

# Plot
block_prob = block_prob.sort_values(by=['po'], ascending=False)
precision = 2
block_prob['N'] = np.ceil(block_prob['N'] * 10**precision) / (10**precision)
cols = ['N', 'Ns']
block_prob['N_Ns'] = block_prob[cols].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
block_prob.set_index('N_Ns', inplace=True)

block_prob['block_prob_%'].plot(
    style=['v--'], markersize=3, markerfacecolor='None', color=['steelblue'])
plt.title(f'[5G NR]\nSA Paging Block Probability\n\nAssumptions:\nTDD DL Slot % = {mo_rrc_hour*100} %\n')
plt.ylabel('Block Probability (%)')
plt.xlabel('N_Ns')
plt.ylim(0, 100)
# plt.xlim(-7, 17)
plt.grid()
# # plt.legend(['Default', 'High Demand UE', 'Low Demand UE'])
# plt.legend(['Full Buffer', 'High Demand UE', 'Low Demand UE'], title=f'BW Setting {band_select}', loc='upper center',
#            bbox_to_anchor=(1.22, 1.02), fancybox=True)

# plt.savefig('5G_DL_User_Throughput_SINR.png', dpi=300, bbox_inches='tight')
plt.show()