# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

# MT Users in the Area during busy hour
mt_rrc_hour = 1800

# Paging Core
tac_size = 200                          # Number of cell is TAC area

# Paging RAN
# Number of times UE goes to RRC_INACTIVE in 1 RRC Session
rrc_inactive = 5
ran_noti_area = 180                     # Number of cell is RAN Notification area

# Paging Occasion
# N = min(T, nB). nB can be [4T, 2T,T, 1/2T, 1/4T, 1/8T, 1/16T, 1/32T]
N = [1, 1/2, 1/4, 1/8, 1/16, 1/32]
# Ns = max(1, nB/T). nB can be [4T, 2T,T, 1/2T, 1/4T, 1/8T, 1/16T, 1/32T]
Ns = [4, 2, 1]

# Paging CCE Agg Level
paging_cce_agg_lev = 8

# SSB Beams
# For FR1, SSB Count in SSB Burst Set can be up until 4 and 8 (LMax = 4 for < 3GHz, LMax = 8 for ~3-6GHz)
# For FR2, SSB Count in SSB Burst Set can be up until 64 (LMax = 64)
ssb_beams = [1, 2, 4, 8, 16, 32, 64]


# UE allowed per paging message
max_ue_per_paging_msg_val = 16
max_ue_per_paging_msg = [4, 8, 12, 16, 20, 24, 28, 32]

# UE per paging message - List
ue_per_paging_msg = list(range(1, 101))

# Color List
color = ['navy', 'darkcyan', 'seagreen', 'olivedrab',
         'gold', 'sienna', 'firebrick', 'dimgrey']
