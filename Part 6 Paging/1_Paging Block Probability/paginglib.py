# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

from math import factorial
import pandas as pd


class pagingvolume:

    # Number of paging per second
    def paging_demand(paging_demand_core, paging_demand_ran):
        pdem = paging_demand_core + paging_demand_ran
        return pdem

    # Number of core paging per second
    def paging_core(mt_rrc_hour, tac_size):
        paging_demand_core = mt_rrc_hour / 3600 * tac_size          # 3600 seconds per hour
        return paging_demand_core

    # Number of ran paging per second
    def paging_ran(mt_rrc_hour, rrc_inactive_hour, ran_noti_area):
        paging_demand_ran = mt_rrc_hour / 3600 * rrc_inactive_hour * ran_noti_area
        return paging_demand_ran


class pagingoccasion:

    # Number of paging occasion per second
    def paging_occasion(N, Ns):

        df_po = pd.DataFrame(columns=['N', 'Ns', 'po'])

        index = 0
        for i in range(len(N)):
            for j in range(len(Ns)):
                df_po.loc[index, ['N']] = N[i]
                df_po.loc[index, ['Ns']] = Ns[j]
                df_po.loc[index, ['po']] = N[i] * Ns[j] * \
                    100             # 100 radio frame per second
                index = index + 1
        return df_po


class pagingue:

    # Number of UE need paging per message
    def ue_per_paging_msg(pdem, df_po):
        df_po['ue_per_paging_msg'] = pdem/df_po['po']
        return df_po


class paginguelist:

    # Number of UE need paging per message in list
    def ue_per_paging_msg(ue_per_paging_msg, max_ue_per_paging_msg):

        df_paging_ue = pd.DataFrame(columns=['ue_per_paging_msg', 'max_ue_per_paging_msg'])

        index = 0
        for i in range(len(ue_per_paging_msg)):
            for j in range(len(max_ue_per_paging_msg)):
                df_paging_ue.loc[index, ['ue_per_paging_msg']] = ue_per_paging_msg[i]
                df_paging_ue.loc[index, ['max_ue_per_paging_msg']] = max_ue_per_paging_msg[j]

                index = index + 1
        return df_paging_ue


class pagingblock:

    # Blockage probability - Customer denied service
    def ErlangB(E, m):
        InvB = 1.0
        for j in range(1, m+1):
            InvB = 1.0 + InvB * (j/E)
        return (1.0 / InvB) * 100           # In percent %

    # Blockage probability - Customer put in queue

    def ErlangC(A, N):
        L = (A**N / factorial(N)) * (N / (N - A))
        sum_ = 0
        for i in range(N):
            sum_ += (A**i) / factorial(i)
        return (L / (sum_ + L)) * 100       # In percent %
