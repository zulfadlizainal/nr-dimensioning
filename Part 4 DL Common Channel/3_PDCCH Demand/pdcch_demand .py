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

### Plotting (Base: CCE Agg Level) ###

df_agg_level.set_index('CCE Agg Level', inplace=True)

df_agg_level[['CCE/Frame_Data', 'CCE/Frame_VoNR']
             ].plot(kind='bar', stacked=True, width=1)
plt.title(
    f'[5G NR DATA + VONR]\nNumber of CCE Needed / 10ms Frame\n\nAssumptions:\nUtilization: Data = {(dl_act_factor+ul_act_factor)*100} %, Voice = {(voice_act_factor)*100} %\nNumber of Attempt: Data = {mo_avgrrcuser_nbh+mt_avgrrcuser_nbh}, Voice = {mo_call_nbh+mt_call_nbh}\nScheduling Periodicity: Data = {sch_periodicity} ms, Voice = {voice_packet_periodicity} ms\nBLER = {bler*100}%\nUsage Duration = {user_duration*3600} Secs \nTotal UE/Cell = {data_subscribers}\n', fontsize=10)
plt.ylabel('CCE Needed')
plt.xlabel('Average CCE in One DCI/PDCCH')
# plt.ylim(0, 20)
plt.xlim(0, 15)
plt.grid()
plt.legend(title='User Type')

plt.show()

df_agg_level[['CCE-RE/Frame_Data', 'CCE-RE/Frame_VoNR']
             ].plot(kind='bar', stacked=True, width=1)
plt.title(
    f'[5G NR DATA + VONR]\nNumber of CCE RE Needed / 10ms Frame\n\nAssumptions:\nUtilization: Data = {(dl_act_factor+ul_act_factor)*100} %, Voice = {(voice_act_factor)*100} %\nNumber of Attempt: Data = {mo_avgrrcuser_nbh+mt_avgrrcuser_nbh}, Voice = {mo_call_nbh+mt_call_nbh}\nScheduling Periodicity: Data = {sch_periodicity} ms, Voice = {voice_packet_periodicity} ms\nBLER = {bler*100}%\nUsage Duration = {user_duration*3600} Secs \nTotal UE/Cell = {data_subscribers}\n', fontsize=10)
plt.ylabel('CCE RE Needed')
plt.xlabel('Average CCE in One DCI/PDCCH')
# plt.ylim(0, 20)
plt.xlim(0, 15)
plt.grid()
plt.legend(title='User Type')

plt.show()


### Plotting (Base: PDSCH SINR) ###

df_pdsch_sinr[['CCE/Frame_Data', 'CCE/Frame_VoNR']
              ].plot(style=['v--', '8--'], markersize=3, markerfacecolor='None', color=['r', 'k'])
plt.title(
    f'[5G NR DATA + VONR]\nNumber of CCE Needed / 10ms Frame\n\nAssumptions:\nUtilization: Data = {(dl_act_factor+ul_act_factor)*100} %, Voice = {(voice_act_factor)*100} %\nNumber of Attempt: Data = {mo_avgrrcuser_nbh+mt_avgrrcuser_nbh}, Voice = {mo_call_nbh+mt_call_nbh}\nScheduling Periodicity: Data = {sch_periodicity} ms, Voice = {voice_packet_periodicity} ms\nBLER = {bler*100}%\nUsage Duration = {user_duration*3600} Secs \nTotal UE/Cell = {data_subscribers}\n', fontsize=10)
plt.ylabel('CCE Needed')
plt.xlabel('PDSCH SINR (dB)')
# plt.ylim(0, 20)
plt.xlim(-8, 30)
plt.grid()
plt.legend(title='User Type')

plt.show()

df_pdsch_sinr[['CCE-RE/Frame_Data', 'CCE-RE/Frame_VoNR']
              ].plot(style=['v--', '8--'], markersize=3, markerfacecolor='None', color=['r', 'k'])
plt.title(
    f'[5G NR DATA + VONR]\nNumber of CCE RE Needed / 10ms Frame\n\nAssumptions:\nUtilization: Data = {(dl_act_factor+ul_act_factor)*100} %, Voice = {(voice_act_factor)*100} %\nNumber of Attempt: Data = {mo_avgrrcuser_nbh+mt_avgrrcuser_nbh}, Voice = {mo_call_nbh+mt_call_nbh}\nScheduling Periodicity: Data = {sch_periodicity} ms, Voice = {voice_packet_periodicity} ms\nBLER = {bler*100}%\nUsage Duration = {user_duration*3600} Secs \nTotal UE/Cell = {data_subscribers}\n', fontsize=10)
plt.ylabel('CCE RE Needed')
plt.xlabel('PDSCH SINR (dB)')
# plt.ylim(0, 20)
plt.xlim(-8, 30)
plt.grid()
plt.legend(title='User Type')

plt.show()
