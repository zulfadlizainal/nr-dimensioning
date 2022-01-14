# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

from pagingparam import *
from paginglib import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Count of Paging Messages per Radio Frame
def paging_count():

    # Calculate paging occasion per radio frame from parameter settings
    po = pagingoccasion.paging_occasion_rf(N, Ns)

    # Paging demand per radio frame based on dimensioning parameter
    pd = pagingvolume.paging_demand_rf(pagingvolume.paging_core_rf(
        mt_rrc_hour, tac_size), pagingvolume.paging_ran_rf(mt_rrc_hour, rrc_inactive, ran_noti_area))

    # Number of UE need paging per paging message
    po = pagingue.ue_per_paging_msg(pd, po)

    # If paging ue per paging message < 1 ue, paging occasion might not be used
    po['ue_per_paging_msg_normalized'] = np.minimum(po['ue_per_paging_msg'], 1)

    # Calculate repeated paging occasion through ssb beams (Total Paging Msg / RF)
    for i in range(len(ssb_beams)):
        po[f'{ssb_beams[i]}'] = po['po_rf'] * \
            po['ue_per_paging_msg_normalized'] * ssb_beams[i]

    # Clean data for plotting
    po_plt = po.copy()
    precision = 2
    po_plt['N'] = np.ceil(po_plt['N'] * 10 ** precision) / (10**precision)
    po_plt['N_Ns Settings'] = po_plt['N'].astype(
        str) + '_' + po_plt['Ns'].astype(str)
    po_plt = po_plt.sort_values(by=['N_Ns Settings'], ascending=False)

    # Plot (Paging Settings vs Paging Msg Count / RF)
    ax = po_plt[['N_Ns Settings', '1', '2', '4', '8', '16', '32', '64']].plot(
        style=['v--', '8--', 'o--', '^--', 's--', 'p--', 'h--'], markersize=7, markerfacecolor='None', color=color)
    ax.set_xticks(np.arange(len(po_plt['N_Ns Settings'])))
    ax.set_xticklabels(po_plt['N_Ns Settings'], rotation=90)

    plt.title(
        f'[5G NR]\nSA Paging Message Count / Radio Frame\n\nAssumptions (within TAC/RNA Area):\nMT RRC User in Busy Hour = {mt_rrc_hour}\nCells in TAC Area = {tac_size}\nCells in RAN Notification Area = {ran_noti_area}\nRRC Inactive Time per One RRC Session = {rrc_inactive}\n')
    plt.ylabel('Paging Message / Radio Frame')
    plt.xlabel('N_Ns Settings')
    plt.ylim(0)
    plt.xlim(0, 17)
    plt.grid()
    plt.legend(title='SSB Beams', loc='upper center',
               bbox_to_anchor=(1.15, 1.02), fancybox=True)

    # plt.savefig('5G_SA_PagingMsgperFrame.png', dpi=300, bbox_inches='tight')
    plt.show()

    return po

# Count of CCE per Radio Frame for all paging messages


def paging_cce(paging_count):

    pc = paging_count

    # Calculate needed CCE for avery paging messgage (Total Paging CCE / RF)
    for i in range(len(ssb_beams)):
        pc[f'{ssb_beams[i]}'] = pc[f'{ssb_beams[i]}'] * paging_cce_agg_lev

    # Clean data for plotting
    pc_plt = pc.copy()
    precision = 2
    pc_plt['N'] = np.ceil(pc_plt['N'] * 10 ** precision) / (10**precision)
    pc_plt['N_Ns Settings'] = pc_plt['N'].astype(
        str) + '_' + pc_plt['Ns'].astype(str)
    pc_plt = pc_plt.sort_values(by=['N_Ns Settings'], ascending=False)

    # Plot (Paging Settings vs Paging CCE Count / RF)
    ax = pc_plt[['N_Ns Settings', '1', '2', '4', '8', '16', '32', '64']].plot(
        style=['v--', '8--', 'o--', '^--', 's--', 'p--', 'h--'], markersize=7, markerfacecolor='None', color=color)
    ax.set_xticks(np.arange(len(pc_plt['N_Ns Settings'])))
    ax.set_xticklabels(pc_plt['N_Ns Settings'], rotation=90)

    plt.title(
        f'[5G NR]\nSA Paging CCE / Radio Frame\n\nAssumptions (within TAC/RNA Area):\nMT RRC User in Busy Hour = {mt_rrc_hour}\nCells in TAC Area = {tac_size}\nCells in RAN Notification Area = {ran_noti_area}\nRRC Inactive Time per One RRC Session = {rrc_inactive}\nAverage CCE Agg Level for P-RNTI = {paging_cce_agg_lev}\n')
    plt.ylabel('Paging CCE / Radio Frame')
    plt.xlabel('N_Ns Settings')
    plt.ylim(0)
    plt.xlim(0, 17)
    plt.grid()
    plt.legend(title='SSB Beams', loc='upper center',
               bbox_to_anchor=(1.15, 1.02), fancybox=True)

    # plt.savefig('5G_SA_PagingCCEperFrame.png', dpi=300, bbox_inches='tight')
    plt.show()

    return pc
