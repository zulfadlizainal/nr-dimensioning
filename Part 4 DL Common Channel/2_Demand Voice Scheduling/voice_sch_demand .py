# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

import pandas as pd
import matplotlib.pyplot as plt

# Assumptions
voice_act_factor = 60/100           # Unit: %

mo_call_nbh = 1                     # Unit: Call / UE / Hour
mt_call_nbh = 1                     # Unit: Call / UE / Hour

voice_packet_periodicity = 20                                # Unit: ms
voice_periodicity_frame = 10/voice_packet_periodicity        # Unit: ms

bler = 5/100                        # Unit %

short_user_duration = 20/3600       # Unit: s/3600 (Erlang)
mid_user_duration = 60/3600         # Unit: s/3600 (Erlang)
long_user_duration = 300/3600       # Unit: s/3600 (Erlang)

# Calculations

subscribers = list(range(0, 251, 10))

df_subs = pd.DataFrame(subscribers, columns=['Subscribers'])

df_subs['Short User (20 Sec)'] = df_subs['Subscribers']*[short_user_duration] * \
    [voice_act_factor]*[mo_call_nbh+mt_call_nbh] * \
    [voice_periodicity_frame]*[1+bler]
df_subs['Mid User (60 Sec)'] = df_subs['Subscribers']*[mid_user_duration] * \
    [voice_act_factor]*[mo_call_nbh+mt_call_nbh] * \
    [voice_periodicity_frame]*[1+bler]
df_subs['Long User (300 Sec)'] = df_subs['Subscribers']*[long_user_duration] * \
    [voice_act_factor]*[mo_call_nbh+mt_call_nbh] * \
    [voice_periodicity_frame]*[1+bler]


df_subs.plot(style=['v--', 's--', '8--'], markersize=5, markerfacecolor='None', color=['r', 'b', 'k'],
             x='Subscribers', y=['Short User (20 Sec)', 'Mid User (60 Sec)', 'Long User (300 Sec)'])

plt.title(
    f'[5G VONR]\nNumber of Scheduling Needed / 10ms Frame\n\nAssumptions:\nUtilized Period [Voice Packet Transfer (DL+UL)] = {(voice_act_factor)*100} %\nNumber of Calls / UE / Hour (MO+MT) = {mo_call_nbh+mt_call_nbh}\nScheduling Periodicity = {voice_packet_periodicity} ms\nBLER = {bler*100}%\n', fontsize=10)
plt.ylabel('Scheduling Needed')
plt.xlabel('Number of VoNR Devices / Cell')
plt.ylim(0, 20)
plt.xlim(0, 250)
plt.grid()
plt.legend(title='User Behaviour')

plt.show()
