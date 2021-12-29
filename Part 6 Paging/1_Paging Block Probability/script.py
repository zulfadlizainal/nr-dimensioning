# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

from pagingparam import *
from paginglib import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# UE per paging message derived from paging demand
def paging_block_demand():

    # Calculate paging demand from ran and core
    pd_core = pagingvolume.paging_core(mt_rrc_hour, tac_size)
    pd_ran = pagingvolume.paging_ran(
        mt_rrc_hour, rrc_inactive_hour, ran_noti_area)
    pdem = pagingvolume.paging_demand(pd_core, pd_ran)

    # Calculate paging occasion from parameter settings
    po = pagingoccasion.paging_occasion(N, Ns)

    # Calculate average UE needed in every paging msg
    ue_per_paging_msg = pagingue.ue_per_paging_msg(pdem, po)

    # Calculate block probability based on Max allowed UE per paging message
    block_prob = ue_per_paging_msg.copy()
    for i in range(len(block_prob)):
        block_prob.loc[i, ['block_prob_%']] = pagingblock.ErlangB(
            block_prob.iloc[i]['ue_per_paging_msg'], max_ue_per_paging_msg_val)

    # Clean data for plotting
    block_prob_plt = block_prob.copy()
    precision = 2
    block_prob_plt['N'] = np.ceil(block_prob_plt['N'] * 10 **
                                  precision) / (10**precision)
    block_prob_plt['N_Ns Settings'] = block_prob_plt['N'].astype(
        str) + '_' + block_prob_plt['Ns'].astype(str)
    block_prob_plt = block_prob_plt.sort_values(
        by=['N_Ns Settings'], ascending=False)

    # Plot (Settings vs Block Prob - by PO/Sec)
    sns.catplot(x="N_Ns Settings", y="block_prob_%",
                hue="po", kind="swarm", s=10, legend=False, data=block_prob_plt)
    plt.title(
        f'[5G NR]\nSA Paging Block Probability (%) vs Paging Occasion\n\nAssumptions (within TAC/RNA Area):\nMT RRC User in Busy Hour = {mt_rrc_hour}\nCells in TAC Area = {tac_size}\nCells in RAN Notification Area = {ran_noti_area}\nRRC Inactive Time per One RRC Session = {rrc_inactive_hour}\nMaximum UE ID in One Paging Msg = {max_ue_per_paging_msg_val}\n')
    plt.ylabel('Block Probability (%)')
    plt.xlabel('N_Ns Settings')
    plt.ylim(0, 100)
    # plt.xlim(0, 400)
    plt.xticks(rotation=90)
    plt.grid()
    plt.legend(title='Paging Occasions \n/ Second', loc='upper center',
               bbox_to_anchor=(1.22, 1.02), fancybox=True)

    # plt.savefig('5G_SA_PagBlock_byPagoccasion.png',
    #             dpi=300, bbox_inches='tight')
    plt.show()

    # Clean data for plotting
    block_prob_plt = block_prob_plt.drop_duplicates(
        subset='ue_per_paging_msg', keep="last")
    block_prob_plt = block_prob_plt.sort_values(
        by=['ue_per_paging_msg'], ascending=False)
    block_prob_plt.set_index('ue_per_paging_msg', inplace=True)

    # Plot (Settings vs Block Prob - Avg UE/Paging Msg)
    block_prob_plt['block_prob_%'].plot(
        style=['v--'], markersize=3, markerfacecolor='None', color=['steelblue'])
    plt.title(
        f'[5G NR]\nSA Paging Block Probability (%) vs UE Demand\n\nAssumptions (within TAC/RNA Area):\nMT RRC User in Busy Hour = {mt_rrc_hour}\nCells in TAC Area = {tac_size}\nCells in RAN Notification Area = {ran_noti_area}\nRRC Inactive Time per One RRC Session = {rrc_inactive_hour}\nMaximum UE ID in One Paging Msg = {max_ue_per_paging_msg_val}\n')
    plt.ylabel('Block Probability (%)')
    plt.xlabel('Avg UE / Paging Msg')
    plt.ylim(0, 100)
    plt.xlim(0)
    # plt.xticks(rotation=90)
    plt.grid()

    # plt.savefig('5G_SA_PagBlock_byAvgUE.png', dpi=300, bbox_inches='tight')
    plt.show()

    return block_prob
