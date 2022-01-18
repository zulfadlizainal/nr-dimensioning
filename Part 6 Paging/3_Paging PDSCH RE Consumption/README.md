# PDSCH RE Consumption for Paging

The objective of this calculation is to estimate the paging PDSCH RE consumption by UE based on paging demand and maximum supported UE per paging message. Few important components of paging design in 5G NR SA system will be considered such as TAC size, RNA (RAN Notification Area) size, implemented SSB beams, and paging bits size.

### Paging Frame Structure

Paging frame structure for 5G NR have similar concept as 4G LTE with additional concept of multi beam operation.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%206%20Paging/img/5G_SA_PagingFrame.png" alt="Paging Frame" title="Paging Frame" width=100% height=100% />
</p>
<br />
<br />

### Paging Volume and Paging PDSCH RE Calculation Flow

Paging demand is derived from both paging needed in Core and RAN. Based on this demand and paging frame structure settings, average UE per paging message required can be derived. Paging volume is linearly incremented based on number of SSB beams transmitted. Paging PDSCH RE is then calculated considering paging message header bits and bits per UE identity in the paging message. Paging bits can later be converted to number of RE depending on spectral efficiency using MCS to modulation and code rate table.


    Number of MT Users ───┐                    ┌─── Number of MT Users
                          │                    │
    Cell Count in TAC  ───┤                    ├─── Cell Count in RNA
                          │                    │
                          │                    ├─── Number of RRC_INACTIVE / RRC Session
                          │                    │
                          │                    │
                          │                    │
                          ▼                    ▼
                    Paging Demand        Paging Demand
                      from Core            from RAN
                          │                    │
                          │                    │
                          │                    │                 Paging        Paging Occasion
                          │                    │                 Frames        per Paging Frame
                          └─►  Total Paging  ◄─┘               N Settings        Ns Settings
                                  Demand                            │                  │
                                    │                               │                  │
                                    │                               │                  │
                                    │                               └─► Total Paging ◄─┘
                                    │                                     Occasion
                                    │                                        │
                                    │                                        │
                                    │                                        │
                                    │                                        │
                                    │             Average UE                 │
                                    └─────────► per Paging Msg ◄─────────────┘
                                                    Needed
                                                       │
                           ┌───────────────────────────┤
                           │                           │
                           │                           │
                           │                           │
                           │                           ▼
                           │          Min (1,UE Identity per Paging Msg)                    Number of
                           │                           |                                    SSB Beams
                           │                           │                                        │
                           │                           │                                        │
                           │                           │                                        │
                           │                           │                                        │
                           │                           └────────────────► Paging ◄──────────────┘
                           │                                              Volume
                           │                                                │
                           │                                                │
                           │                   Paging Header Bits ─────────►│
                           │                                                │
                           └─────────────────► UE Identity Bits   ─────────►│
                                                                            │
                                                                            ▼
                                                                           Total               Bits
                                                                           Paging ───────────► to
                                                                           Bits                RE


### Assumptions

Assumptions taken for number of MT users in the area:

    # MT Users in the Area during busy hour (Assume)
    mt_rrc_hour = 1800

Assumptions taken for core network initiated paging:

    # Number of cell is TAC area (Assume)
    tac_size = 200

Assumptions taken for radio network initiated paging:

    # Number of cell is RAN Notification area (Assume)
    ran_noti_area = 180

    # Number of times UE goes to RRC_INACTIVE in 1 RRC Session (Assume)
    rrc_inactive = 5

Assumptions taken for maximum UE supported in one paging message: 

    max_ue_per_paging_msg_val = 16  (Assume)
   
Network settings for paging frame structure based on 3GPP:

    # Paging Occasion (Specs)
    N = [1, 1/2, 1/4, 1/8, 1/16, 1/32]      # N = min(T, nB). nB can be [4T, 2T,T, 1/2T, 1/4T, 1/8T, 1/16T, 1/32T]
    Ns = [4, 2, 1]                          # Ns = max(1, nB/T). nB can be [4T, 2T,T, 1/2T, 1/4T, 1/8T, 1/16T, 1/32T]
    
    # Maximum UE per paging message (Specs)
    max_ue_per_paging_msg = [4, 8, 12, 16, 20, 24, 28, 32]      # Max supported UE in 1 paging message

SSB beams settings is considered as below: 

    # SSB Beams Implementation (Specs)
    ssb_beams = [1, 2, 4, 8, 16, 32, 64]

    # For FR1, SSB Count in SSB Burst Set can be up until 4 and 8 (LMax = 4 for < 3GHz, LMax = 8 for ~3-6GHz)
    # For FR2, SSB Count in SSB Burst Set can be up until 64 (LMax = 64)

Conversion of Paging volume (paging message count) to bits: 
    
    # UE identity bits in paging message (Assume)
    ue_identity_bits = 40

    # Paging header bits (Assume)
    paging_header_bits = 96

Conversion of bits to RE count: 
    
    # Based on MCS, modulation, and code rate used by paging message (Assume) 
    code_rate_constant = 1024
    code_rate_value = 120
    modulation_bitspersym = 2


References for bits conversion to PDSCH RE assumptions taken from configurations based on MCS Index Table for PDSCH (3GPP TS 38.214 - Table 5.1.3.1-1).
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%206%20Paging/img/5G_SA_MCS-Mod-Code.png" alt="MCS-SE_Table" title="MCS-SE_Table" width=50% height=50% />
</p>
<br />
<br /> 

### Calculation

Total paging demand is derived as follows:

    # Number of paging per radio frame
    paging_demand = paging_demand_core + paging_demand_ran

    # Number of core paging per radio frame
    paging_demand_core = mt_rrc_hour / 3600 / 100 * tac_size                              # 3600 seconds per hour       # 100 radio frame per second

    # Number of ran paging per radio frame
    paging_demand_ran = mt_rrc_hour / 3600 / 100 * rrc_inactive * ran_noti_area           # 3600 seconds per hour       # 100 radio frame per second

Total paging occasion is derived as follows:

    # Number of paging occasion per radio frame
    paging_occasion = N * Ns                                                              # 100 radio frame per second

Average UE require paging per paging message:

    # Number of UE need paging per paging message
    ue_per_paging_msg = paging_demand/paging_occasion

Paging Volume is derived as follows:

    # Number of paging message / radio frame
    paging_count = paging_occasion * min(1, ue_per_paging_msg) * ssb_beams

    # If paging ue per paging message < 1 ue, paging occasion might not be used

Paging PDSCH RE is derived as follows:

    # Number of paging bits / radio frame
    paging_bits = paging_count * ((ue_identity_bits * ue_per_paging_msg) + paging_header_bits)

    # Number of paging PDSCH RE / radio frame (Convert bits to RE based on SE)
    paging_re = paging_bits * (code_rate_value / code_rate_constant / modulation_bitspersym)

### Results

Eg: 5G NR SA paging volume (message count) per radio frame based on implemented SSB beams.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%206%20Paging/img/5G_SA_PagingMsgperFrame.png" alt="Paging_Volume" title="Paging_Volume" width=70% height=70% />
</p>
<br />
<br />

Eg: 5G NR SA paging PDSCH RE per radio frame based on implemented SSB beams.

<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%206%20Paging/img/5G_SA_PagingREperFrame.png" alt="Paging_RE" title="Paging_RE" width=70% height=70% />
</p>
<br />
<br />