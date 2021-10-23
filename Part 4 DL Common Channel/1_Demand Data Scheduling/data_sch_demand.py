# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

import pandas as pd
import matplotlib.pyplot as plt

# Assumptions

dl_act_factor = 30/100         # Unit: %
ul_act_factor = 10/100         # Unit: %

mo_avgrrcuser_nbh = 5          # Unit: Avg RRC User / Hour
mt_avgrrcuser_nbh = 2          # Unit: Avg RRC User / Hour

sch_periodicity = 4            # Unit: ms
sch_periodicity_frame = 10/4   # Unit: ms

bler = 10/100                  # Unit %

short_user_duration = 20/3600   # Unit: s/3600 (Erlang)
mid_user_duration = 60/3600     # Unit: s/3600 (Erlang)
long_user_duration = 300/3600   # Unit: s/3600 (Erlang)

# Calculations

subscribers = list(range(0, 251, 10))

df_subs = pd.DataFrame(subscribers, columns=['Subscribers'])

df_subs['Short User (20 Sec)'] = df_subs['Subscribers']*[short_user_duration]*[dl_act_factor +
                                                                               ul_act_factor]*[mo_avgrrcuser_nbh+mt_avgrrcuser_nbh]*[sch_periodicity_frame]*[1+bler]
df_subs['Mid User (60 Sec)'] = df_subs['Subscribers']*[mid_user_duration]*[dl_act_factor +
                                                                           ul_act_factor]*[mo_avgrrcuser_nbh+mt_avgrrcuser_nbh]*[sch_periodicity_frame]*[1+bler]
df_subs['Long User (300 Sec)'] = df_subs['Subscribers']*[long_user_duration]*[dl_act_factor +
                                                                              ul_act_factor]*[mo_avgrrcuser_nbh+mt_avgrrcuser_nbh]*[sch_periodicity_frame]*[1+bler]


df_subs.plot(style=['v--', 's--', '8--'], markersize=5, markerfacecolor='None', color = ['r', 'b', 'k'],
             x='Subscribers', y=['Short User (20 Sec)', 'Mid User (60 Sec)', 'Long User (300 Sec)'])

plt.title(
    f'[NR DATA]\nNumber of Scheduling Needed / 10ms Frame\n\nAssumptions:\nUtilized Period / RRC Session (DL+UL) = {(dl_act_factor+ul_act_factor)*100} %\nNumber of RRC / UE / Hour (MO+MT) = {mo_avgrrcuser_nbh+mt_avgrrcuser_nbh}\nScheduling Periodicity = {sch_periodicity} ms\nBLER = {bler*100}%\n', fontsize=10)
plt.ylabel('Scheduling Needed')
plt.xlabel('Number of UE / Cell')
plt.ylim(0, 180)
plt.xlim(0, 250)
plt.grid()
plt.legend(title='User Behaviour')

plt.show()
