# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

# Import 3GPP Table
df = pd.read_excel('3GPP_TS_38_101_BwSettings.xlsx', index_col=0)

# Create ID
df['ID'] = df['FR'] + '_' + \
    df['SCS (kHz)'].astype(str)+'_'+df['Bandwidth (MHz)'].astype(str)

########################################################################################

### Calculate Overall RE/Frame ###

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
# df['Extended CP Symbol/Frame'] = df['Slots/Frame'].multiply(12)

# Calculate No of RE/Frame/RB
df['Normal CP RE/Frame/RB'] = df['Normal CP Symbol/Frame'].multiply(12)
# df['Extended CP RE/Frame/RB'] = df['Extended CP Symbol/Frame'].multiply(12)

# Calculate No of RE/Frame (All Bandwidth)
df['Normal CP RE/Frame'] = df['Normal CP RE/Frame/RB']*df['RB']
# df['Extended CP RE/Frame'] = df['Extended CP RE/Frame/RB']*df['RB']

# Split Dataframe based on FR
df_fr1 = df[df['FR'] == 'FR1']
df_fr2 = df[df['FR'] == 'FR2']

########################################################################################

### Calculate Overall DL RE/Frame ###

# Percentage of DL Slots in a 10ms frame
tdd_dl_slot_percent = (70/100)

# Calculate No of DL RE/Frame (All Bandwidth)
df_fr1['Normal CP DL RE/Frame'] = df_fr1['Normal CP RE/Frame']*tdd_dl_slot_percent
df_fr2['Normal CP DL RE/Frame'] = df_fr2['Normal CP RE/Frame']*tdd_dl_slot_percent

########################################################################################

### Calculate SSB RE/Frame ###

# SSB Size (Specs)
ssb_symbols = 4
ssb_subcarriers = 270

# No of Beams (Assume) - No of SSB Beam / SSB Burst (L) can be FR1 = [1, 2, 4, 8], FR2 = [1, 2, 4, 8, 16, 32, 64]

ssb_beam_fr1 = 4
ssb_beam_fr2 = 16

# SSB Periodicity (Assume) - SSB Periodicity (ms) can be [5, 10, 20, 40, 80, 160]

ssb_periodicity_fr1 = 10
ssb_periodicity_fr2 = 10

# SSB RE/Frame

ssb_re_frame_fr1 = ssb_symbols*ssb_subcarriers * \
    ssb_beam_fr1*(10/ssb_periodicity_fr1)
ssb_re_frame_fr2 = ssb_symbols*ssb_subcarriers * \
    ssb_beam_fr2*(10/ssb_periodicity_fr2)

# Include in Dataframe

df_fr1['SSB RE/Frame'] = ssb_re_frame_fr1
df_fr2['SSB RE/Frame'] = ssb_re_frame_fr2

########################################################################################

### Calculate DL DMRS RE/Frame ###

# DMRS RE Rules

# Type1:

# 1. One OFDM Symbols = Up to 4 Ports
# 2. Two OFDM Symbols = Up to 8 Ports

# Type2:

# 1. One OFDM Symbols = Up to 6 Ports
# 2. Two OFDM Symbols = Up to 12 Ports

# DMRS Ports (Assume)

dmrs_ports_fr1 = 4
dmrs_ports_fr2 = 4

# DMRS Symbols (Assume) - Can be One or Two

dmrs_symbols_fr1 = 2
dmrs_symbols_fr2 = 2

# PDSCH Layers (Assume)

pdsch_layer_number_fr1 = 4
pdsch_layer_number_fr2 = 4

# DL DMRS RE/Frame

df_fr1['DL DMRS RE/Frame'] = df_fr1['RB'] * df_fr1['Slots/Frame'] * \
    tdd_dl_slot_percent * \
    (dmrs_ports_fr1 * dmrs_symbols_fr1 * pdsch_layer_number_fr1)
df_fr2['DL DMRS RE/Frame'] = df_fr2['RB'] * df_fr2['Slots/Frame'] * \
    tdd_dl_slot_percent * \
    (dmrs_ports_fr2 * dmrs_symbols_fr2 * pdsch_layer_number_fr2)


########################################################################################

### Calculate CSI-RS RE/Frame ###

# Import 3GPP Table
df_csi_rs = pd.read_excel('3GPP_TS_38_211_CsiRsSettings.xlsx', index_col=0)

# CSI-RS Port (Assume) -  Based on CSI-RS Settings table
csi_rs_port_fr1 = 4
csi_rs_port_fr2 = 4

# CSI-RS Slot Periodicity (Assume) -  can be [4, 5, 8, 10, 16, 20, 40, 80, 160, 320]
csi_rs_slot_periodicity_fr1 = 4
csi_rs_slot_periodicity_fr2 = 20

# DL CSI-RS RE/Frame

df_fr1['DL CSI-RE/Frame'] = df_fr1['RB'] * csi_rs_port_fr1 * \
    (10/(csi_rs_slot_periodicity_fr1 * df_fr1['Slot Duration (ms)']))
df_fr2['DL CSI-RE/Frame'] = df_fr2['RB'] * csi_rs_port_fr2 * \
    (10/(csi_rs_slot_periodicity_fr2 * df_fr2['Slot Duration (ms)']))

########################################################################################

### Calculate PT-RS RE/Frame ###

# PT-RS Info

# 1. Only for High Frequency Phase Tracking (mmWave/FR2)
# 2. Configured by RRC
# 3. Time Density (TD) PTRS increase when MCS increase
# 4. Frequency Density (FD) decrease when BW increase

normal_cp_symbols = 14
extended_cp_symbols = 12

# PTRS Time Density (Assume) - can be [n/a, 1, 2, 4]

ptrs_time_density_fr1 = 0
ptrs_time_density_fr2 = 1

# PTRS Frequency Density (Assume) - can be [n/a, 1, 2, 4, 8. 16]

ptrs_frequency_density_fr1 = 0
ptrs_frequency_density_fr2 = 2

# PDCCH Symbols (Assume) - can be [1, 2, 3]

pdcch_symbols_fr1 = 3
pdcch_symbols_fr2 = 3

# DL PT-RS RE/Frame

try:
    df_fr1['DL PTRS-RE/Frame'] = (df_fr1['RB'] / ptrs_frequency_density_fr1) * df_fr1['Slots/Frame'] * \
        tdd_dl_slot_percent * \
        ((normal_cp_symbols - pdcch_symbols_fr1 -
         dmrs_symbols_fr1) / ptrs_time_density_fr1)

except ZeroDivisionError:
    df_fr1['DL PTRS-RE/Frame'] = 0


try:
    df_fr2['DL PTRS-RE/Frame'] = (df_fr2['RB'] / ptrs_frequency_density_fr2) * df_fr2['Slots/Frame'] * \
        tdd_dl_slot_percent * \
        ((normal_cp_symbols - pdcch_symbols_fr2 -
         dmrs_symbols_fr2) / ptrs_time_density_fr2)

except ZeroDivisionError:
    df_fr2['DL PTRS-RE/Frame'] = 0


########################################################################################

### Calculate T-RS RE/Frame ###

# TRS RE / RB - Only 3 RE/RB

trs_subcarrier_perRB_fr1 = 3
trs_subcarrier_perRB_fr2 = 3

# TRS Symbol / Burst (Assume) - 4 Symbol for FR1, can be [2, 4] Symbol for FR2

trs_symbol_perBurst_fr1 = 4
trs_symbol_perBurst_fr2 = 4

# TRS Burst Periodicity (Assume) - can be [10, 20, 40, 80] ms

trs_burst_periodicity_fr1 = 80
trs_burst_periodicity_fr2 = 80

# DL CSI-RS RE/Frame

df_fr1['DL TRS-RE/Frame'] = df_fr1['RB'] * trs_subcarrier_perRB_fr1 * \
    trs_symbol_perBurst_fr1 * (10/trs_burst_periodicity_fr1)
df_fr2['DL TRS-RE/Frame'] = df_fr2['RB'] * trs_subcarrier_perRB_fr2 * \
    trs_symbol_perBurst_fr2 * (10/trs_burst_periodicity_fr2)

########################################################################################

### Calculate PDCCH RE/Frame ###

# PDCCH RE is really flexible in 5G and can be a lot based on demand. For this simulation - asummption of PDCCH resources is assumed.

pdcch_usage_percentage_fr1 = 1.2/100
pdcch_usage_percentage_fr2 = 0.25/100

# PDCCH RE/Frame

df_fr1['PDCCH-RE/Frame'] = pdcch_usage_percentage_fr1 * \
    df_fr1['Normal CP RE/Frame']
df_fr2['PDCCH-RE/Frame'] = pdcch_usage_percentage_fr2 * \
    df_fr2['Normal CP RE/Frame']

########################################################################################

### Calculate PDSCH RE/Frame ###

df_fr1['PDSCH-RE/Frame'] = df_fr1['Normal CP DL RE/Frame'] - df_fr1['SSB RE/Frame'] - df_fr1['DL DMRS RE/Frame'] - \
    df_fr1['DL CSI-RE/Frame'] - df_fr1['DL PTRS-RE/Frame'] - \
    df_fr1['DL TRS-RE/Frame'] - df_fr1['PDCCH-RE/Frame']

df_fr2['PDSCH-RE/Frame'] = df_fr2['Normal CP DL RE/Frame'] - df_fr2['SSB RE/Frame'] - df_fr2['DL DMRS RE/Frame'] - \
    df_fr2['DL CSI-RE/Frame'] - df_fr2['DL PTRS-RE/Frame'] - \
    df_fr2['DL TRS-RE/Frame'] - df_fr2['PDCCH-RE/Frame']

########################################################################################

# Calculate Distribution of Every Channel


df_fr1['DL PTRS-RE %'] = (df_fr1['DL PTRS-RE/Frame'] /
                          df_fr1['Normal CP DL RE/Frame']) * 100
df_fr2['DL PTRS-RE %'] = (df_fr2['DL PTRS-RE/Frame'] /
                          df_fr2['Normal CP DL RE/Frame']) * 100

df_fr1['DL TRS-RE %'] = (df_fr1['DL TRS-RE/Frame'] /
                         df_fr1['Normal CP DL RE/Frame']) * 100
df_fr2['DL TRS-RE %'] = (df_fr2['DL TRS-RE/Frame'] /
                         df_fr2['Normal CP DL RE/Frame']) * 100

df_fr1['DL CSI-RE %'] = (df_fr1['DL CSI-RE/Frame'] /
                         df_fr1['Normal CP DL RE/Frame']) * 100
df_fr2['DL CSI-RE %'] = (df_fr2['DL CSI-RE/Frame'] /
                         df_fr2['Normal CP DL RE/Frame']) * 100

df_fr1['DL DMRS-RE %'] = (df_fr1['DL DMRS RE/Frame'] /
                          df_fr1['Normal CP DL RE/Frame']) * 100
df_fr2['DL DMRS-RE %'] = (df_fr2['DL DMRS RE/Frame'] /
                          df_fr2['Normal CP DL RE/Frame']) * 100

df_fr1['SSB-RE %'] = (df_fr1['SSB RE/Frame'] /
                      df_fr1['Normal CP DL RE/Frame']) * 100
df_fr2['SSB-RE %'] = (df_fr2['SSB RE/Frame'] /
                      df_fr2['Normal CP DL RE/Frame']) * 100

df_fr1['PDCCH-RE %'] = (df_fr1['PDCCH-RE/Frame'] /
                        df_fr1['Normal CP DL RE/Frame']) * 100
df_fr2['PDCCH-RE %'] = (df_fr2['PDCCH-RE/Frame'] /
                        df_fr2['Normal CP DL RE/Frame']) * 100

df_fr1['PDSCH-RE %'] = (df_fr1['PDSCH-RE/Frame'] /
                        df_fr1['Normal CP DL RE/Frame']) * 100
df_fr2['PDSCH-RE %'] = (df_fr2['PDSCH-RE/Frame'] /
                        df_fr2['Normal CP DL RE/Frame']) * 100

df_fr1['DL Overhead %'] = 100 - df_fr1['PDSCH-RE %']
df_fr2['DL Overhead %'] = 100 - df_fr2['PDSCH-RE %']

########################################################################################

### Manage User Distribution ###

# Import User location
df_ue_loc = pd.read_csv('ue_loc.csv')
df_ue_loc = df_ue_loc[df_ue_loc['UE_Loc'].notna()]  # Filter UE location only

# Calculate count of UE per Sector
df_sec_ue = df_ue_loc.pivot_table(
    index='SecArea_UEAllowed', aggfunc=np.count_nonzero)
df_sec_ue = df_sec_ue['UE_Loc']
df_sec_ue = df_sec_ue.reset_index()
secuemap = dict(zip(df_sec_ue['SecArea_UEAllowed'], df_sec_ue['UE_Loc']))

# Lookup UE Count from Dictionary
df_ue_loc['Sec_UE_Count'] = df_ue_loc['SecArea_UEAllowed'].map(secuemap)

########################################################################################

## Calculate User Throughput ###

# Import SE Curve
df_se = pd.read_csv('5G_3.5G_SE.csv', index_col=0)

# Select a band
band_select = 'FR1_30_100'

band_config = df_fr1.loc[df_fr1['ID'] == f'{band_select}']
pdsch_re = band_config.iloc[0]['PDSCH-RE/Frame']

# Distribute PDSCH RE per UE (Use simple round robin)
df_ue_loc['PDSCH-RE/Frame/Sec'] = pdsch_re
df_ue_loc['PDSCH-RE/Frame/UE'] = df_ue_loc['PDSCH-RE/Frame/Sec'] / \
    df_ue_loc['Sec_UE_Count']

# Import SE in Calculation
semap = dict(zip(df_se.index, df_se['Estimated SE (bps/Hz)']))
df_ue_loc['SS-SINR_Cat'] = df_ue_loc['SS-SINR'].apply(np.floor)
df_ue_loc['Estimated SE (bps/Hz)'] = df_ue_loc['SS-SINR_Cat'].map(semap)

# Calculate Tput (Mbps)

radio_frame_sec = 100
dl_mu_mimo_gain = 0/100
dl_bler = 0/100  # DL BLER is already reflected in SE calculation

df_ue_loc[f'{band_select}'] = ((df_ue_loc.iloc[0]['PDSCH-RE/Frame/UE'] * radio_frame_sec) * (df_ue_loc['Estimated SE (bps/Hz)'] * ((band_config.iloc[0]
                                                                                                                                    ['SCS (kHz)']*1000)/(normal_cp_symbols * band_config.iloc[0]['Slots/Frame']*100))) / 1000000) * (1 + dl_mu_mimo_gain) * (1 - dl_bler)

df_ue_loc['UE_Tput_Mbps'] = df_ue_loc[f'{band_select}']

# Calculate Tput (Mbps) considering VONR as priority

vonr_tput_mbps = 0.128

df_ue_loc['UE_Tput_woVonr_Mbps'] = df_ue_loc['UE_Tput_Mbps'] - vonr_tput_mbps


# Calculate Tput (Mbps) considering scheduling demand

high_demand_ue = 80/100  # % of time need scheduling
low_demand_ue = 20/100  # % of need scheduling

df_ue_loc['UE_Tput_LowDemand_Mbps'] = df_ue_loc['UE_Tput_woVonr_Mbps'] * low_demand_ue
df_ue_loc['UE_Tput_HighDemand_Mbps'] = df_ue_loc['UE_Tput_woVonr_Mbps'] * high_demand_ue

########################################################################################

# Plot

df_ue_loc_plt1 = df_ue_loc.set_index(df_ue_loc['SS-RSRP'])
df_ue_loc_plt1.sort_index(inplace=True)

df_ue_loc_plt1[['UE_Tput_woVonr_Mbps', 'UE_Tput_HighDemand_Mbps', 'UE_Tput_LowDemand_Mbps']].plot(
    style=['v--', 's--', '8--'], markersize=3, markerfacecolor='None', color=['firebrick', 'limegreen', 'steelblue'])
plt.title(
    f'[5G NR]\nDownlink User Throughput (Mbps)\n\nAssumptions:\nTDD DL Slot % = {tdd_dl_slot_percent*100} %\nMU MIMO Gain = {dl_mu_mimo_gain*100} %\nSpectral Efficiency = Same for all bands\nMax MIMO Layers = 4, BLER = 10%\nHigh Demand UE = {high_demand_ue*100} % of Scheduling Demand\nLow Demand UE = {low_demand_ue*100} % of Scheduling Demand\n', fontsize=11)
plt.ylabel('Mbps')
plt.xlabel('SS-RSRP (dBm)')
plt.ylim(0, 50)
plt.xlim(-130, -90)
plt.grid()
# plt.legend(['Default', 'High Demand UE', 'Low Demand UE'])
plt.legend(['Full Buffer', 'High Demand UE', 'Low Demand UE'], title=f'BW Setting {band_select}', loc='upper center',
           bbox_to_anchor=(1.22, 1.02), fancybox=True)

plt.savefig('5G_DL_User_Throughput_RSRP.png', dpi=300, bbox_inches='tight')
plt.show()

# Plot

df_ue_loc_plt1 = df_ue_loc.set_index(df_ue_loc['SS-SINR'])
df_ue_loc_plt1.sort_index(inplace=True)

df_ue_loc_plt1[['UE_Tput_woVonr_Mbps', 'UE_Tput_HighDemand_Mbps', 'UE_Tput_LowDemand_Mbps']].plot(
    style=['v--', 's--', '8--'], markersize=3, markerfacecolor='None', color=['firebrick', 'limegreen', 'steelblue'])
plt.title(
    f'[5G NR]\nDownlink User Throughput (Mbps)\n\nAssumptions:\nTDD DL Slot % = {tdd_dl_slot_percent*100} %\nMU MIMO Gain = {dl_mu_mimo_gain*100} %\nSpectral Efficiency = Same for all bands\nMax MIMO Layers = 4, BLER = 10%\nHigh Demand UE = {high_demand_ue*100} % of Scheduling Demand\nLow Demand UE = {low_demand_ue*100} % of Scheduling Demand\n', fontsize=11)
plt.ylabel('Mbps')
plt.xlabel('SS-SINR (dB)')
plt.ylim(0, 50)
plt.xlim(-10, 17)
plt.grid()
# plt.legend(['Default', 'High Demand UE', 'Low Demand UE'])
plt.legend(['Full Buffer', 'High Demand UE', 'Low Demand UE'], title=f'BW Setting {band_select}', loc='upper center',
           bbox_to_anchor=(1.22, 1.02), fancybox=True)

plt.savefig('5G_DL_User_Throughput_SINR.png', dpi=300, bbox_inches='tight')
plt.show()

# Plot

df_ue_loc_plt2 = df_ue_loc.sort_values(by=['SecArea_UEAllowed'])
df_ue_loc_plt2.reset_index(inplace=True)

df_ue_loc_plt2['UE_Tput_woVonr_Mbps'].plot(kind='bar', width=0.9)

plt.title(
    f'[5G NR]\nDownlink User Throughput (Mbps)\n\nAssumptions:\nTDD DL Slot % = {tdd_dl_slot_percent*100} %\nMU MIMO Gain = {dl_mu_mimo_gain*100} %\nSpectral Efficiency = Same for all bands\nMax MIMO Layers = 4, BLER = 10%\n', fontsize=11)
plt.ylabel('Mbps')
plt.xlabel('UE ID')
plt.ylim(0, 50)
# plt.xlim(0, 17)
# plt.xticks(rotation=45)
plt.grid()
plt.grid(which='minor', alpha=0.2)
plt.grid(which='major', alpha=0.5)
# plt.legend(['UE ID'], title=f'BW Setting {band_select}', loc='upper center',
#            bbox_to_anchor=(1.22, 1.02), fancybox=True)
plt.savefig('5G_DL_User_Throughput_UEID.png', dpi=300, bbox_inches='tight')
plt.show()
