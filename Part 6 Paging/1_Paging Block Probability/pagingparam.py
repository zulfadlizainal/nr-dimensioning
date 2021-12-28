# Author: Zulfadli Zainal
# Github: https://github.com/zulfadlizainal
# Linkedin: https://linkedin.com/in/zulfadlizainal

# MT Users in the Area
mt_rrc_hour = 900

# Paging Core
tac_size = 200

# Paging RAN
rrc_inactive_hour = 5
ran_noti_area = 180

# Paging Occasion
N = [1, 1/2, 1/4, 1/8, 1/16, 1/32]      # N = min(T, nB). nB can be [4T, 2T,T, 1/2T, 1/4T, 1/8T, 1/16T, 1/32T]
Ns = [4, 2, 1]                          # Ns = max(1, nB/T). nB can be [4T, 2T,T, 1/2T, 1/4T, 1/8T, 1/16T, 1/32T]

# UE allowed per paging message
max_ue_per_paging_msg_val = 16
max_ue_per_paging_msg = [4, 8, 12, 16, 20, 24, 28, 32]