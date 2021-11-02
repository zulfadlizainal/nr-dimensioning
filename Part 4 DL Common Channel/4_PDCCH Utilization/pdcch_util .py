# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

import pandas as pd
import matplotlib.pyplot as plt

### Data Scheduling Number ###

dl_act_factor = 30/100         # Unit: %
ul_act_factor = 10/100         # Unit: %

mo_avgrrcuser_nbh = 5          # Unit: Avg RRC User / UE / Hour
mt_avgrrcuser_nbh = 2          # Unit: Avg RRC User / UE / Hour

sch_periodicity = 4                          # Unit: ms
sch_periodicity_frame = 10/sch_periodicity   # Unit: ms

bler = 10/100                   # Unit %

user_duration = 40/3600         # Unit: s/3600 (Erlang)

data_subscribers = 250

data_scheduled_number = data_subscribers*user_duration * \
    (dl_act_factor+ul_act_factor)*(mo_avgrrcuser_nbh +
                                   mt_avgrrcuser_nbh)*sch_periodicity_frame*(1+bler)


### Voice Scheduling Number ###

voice_act_factor = 60/100           # Unit: %

mo_call_nbh = 1                     # Unit: Call / UE / Hour
mt_call_nbh = 1                     # Unit: Call / UE / Hour

voice_packet_periodicity = 20                                # Unit: ms
voice_periodicity_frame = 10/voice_packet_periodicity        # Unit: ms

voice_subscribers = data_subscribers

voice_scheduled_number = voice_subscribers*user_duration*voice_act_factor * \
    (mo_call_nbh+mt_call_nbh)*(voice_periodicity_frame)*(1+bler)

########################################################################################

### Calculate CCE/CCE RE per Agg Level ###

cce_agg_level = list(range(1, 17, 1))

df_agg_level = pd.DataFrame(cce_agg_level, columns=['CCE Agg Level'])

# CCE / Frame

df_agg_level['CCE/Frame_Data'] = df_agg_level['CCE Agg Level'] * \
    data_scheduled_number
df_agg_level['CCE/Frame_VoNR'] = df_agg_level['CCE Agg Level'] * \
    voice_scheduled_number
df_agg_level['CCE/Frame_Total'] = df_agg_level['CCE/Frame_Data'] + \
    df_agg_level['CCE/Frame_VoNR']

# RE / Frame

df_agg_level['CCE-RE/Frame_Data'] = df_agg_level['CCE Agg Level'] * \
    data_scheduled_number*6*12
df_agg_level['CCE-RE/Frame_VoNR'] = df_agg_level['CCE Agg Level'] * \
    voice_scheduled_number*6*12
df_agg_level['CCE-RE/Frame_Total'] = df_agg_level['CCE-RE/Frame_Data'] + \
    df_agg_level['CCE-RE/Frame_VoNR']


### Calculate CCE/CCE RE per PDSCH SINR ###

df_pdsch_sinr = pd.read_csv('5G_SINR_CCE_Relation.csv', index_col=0)

# CCE / Frame

df_pdsch_sinr['CCE/Frame_Data'] = df_pdsch_sinr['CCE_Estimate'] * \
    data_scheduled_number
df_pdsch_sinr['CCE/Frame_VoNR'] = df_pdsch_sinr['CCE_Estimate'] * \
    voice_scheduled_number
df_pdsch_sinr['CCE/Frame_Total'] = df_pdsch_sinr['CCE/Frame_Data'] + \
    df_pdsch_sinr['CCE/Frame_VoNR']

# RE / Frame

df_pdsch_sinr['CCE-RE/Frame_Data'] = df_pdsch_sinr['CCE_Estimate'] * \
    data_scheduled_number*6*12
df_pdsch_sinr['CCE-RE/Frame_VoNR'] = df_pdsch_sinr['CCE_Estimate'] * \
    voice_scheduled_number*6*12
df_pdsch_sinr['CCE-RE/Frame_Total'] = df_pdsch_sinr['CCE-RE/Frame_Data'] + \
    df_pdsch_sinr['CCE-RE/Frame_VoNR']

########################################################################################

df_rb = pd.read_excel('3GPP_TS_38_101_RB.xlsx')

# Compared settings

tdd_dl_slot = (50/100)*10           # Percentage of DL Slots in a 10ms frame

scs_one = 15
bw_one = 20
rb_one = df_rb.loc[(df_rb['SCS (kHz)'] == scs_one) &
                   (df_rb['Bandwidth (MHz)'] == bw_one)]
rb_one = rb_one['RB'].values[0]
dl_slot_per_frame_one = tdd_dl_slot * (scs_one/15)

scs_two = 30
bw_two = 50
rb_two = df_rb.loc[(df_rb['SCS (kHz)'] == scs_two) &
                   (df_rb['Bandwidth (MHz)'] == bw_two)]
rb_two = rb_two['RB'].values[0]
dl_slot_per_frame_two = tdd_dl_slot * (scs_two/15)

scs_three = 30
bw_three = 100
rb_three = df_rb.loc[(df_rb['SCS (kHz)'] == scs_three) &
                     (df_rb['Bandwidth (MHz)'] == bw_three)]
rb_three = rb_three['RB'].values[0]
dl_slot_per_frame_three = tdd_dl_slot * (scs_three/15)

########################################################################################

# Calculate PDCCH Utilization

pdcch_symbols = 3
subcarriers = 12

df_pdsch_sinr[f'SCS_{scs_one}kHz_BW{bw_one}MHz'] = df_pdsch_sinr['CCE-RE/Frame_Total'] / \
    (rb_one*subcarriers*pdcch_symbols*dl_slot_per_frame_one)*100
df_pdsch_sinr[f'SCS_{scs_two}kHz_BW{bw_two}MHz'] = df_pdsch_sinr['CCE-RE/Frame_Total'] / \
    (rb_two*subcarriers*pdcch_symbols*dl_slot_per_frame_two)*100
df_pdsch_sinr[f'SCS_{scs_three}kHz_BW{bw_three}MHz'] = df_pdsch_sinr['CCE-RE/Frame_Total'] / \
    (rb_three*subcarriers*pdcch_symbols*dl_slot_per_frame_three)*100

### Plotting PDCCH Utilization % ###

df_pdsch_sinr[[f'SCS_{scs_one}kHz_BW{bw_one}MHz', f'SCS_{scs_two}kHz_BW{bw_two}MHz', f'SCS_{scs_three}kHz_BW{bw_three}MHz']
              ].plot(style=['v--', 's--', '8--'], markersize=3, markerfacecolor='None', color=['r', 'b', 'k'])
plt.title(
    f'[5G NR DATA + VONR]\nNumber of CCE Needed / 10ms Frame\n\nAssumptions:\nUtilization: Data = {(dl_act_factor+ul_act_factor)*100} %, Voice = {(voice_act_factor)*100} %\nNumber of Attempt: Data = {mo_avgrrcuser_nbh+mt_avgrrcuser_nbh}, Voice = {mo_call_nbh+mt_call_nbh}\nScheduling Periodicity: Data = {sch_periodicity} ms, Voice = {voice_packet_periodicity} ms\nBLER = {bler*100}%\nUsage Duration = {user_duration*3600} Secs \nTotal UE/Cell = {data_subscribers}\n\nPDCCH Symbol Used = {pdcch_symbols}\nTDD DL Slot Config = {tdd_dl_slot*100/10}%\n', fontsize=10)
plt.ylabel('PDCCH Utilization %')
plt.xlabel('PDSCH SINR (dB)')
plt.ylim(0, 100)
plt.xlim(-8, 30)
plt.grid()
plt.legend(title='Bandwidth Settings')
