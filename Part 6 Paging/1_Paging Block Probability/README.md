# Paging Blocking Probability

The objective of this calculation is to estimate the paging blocking probability of required paging by UE based on paging demand and maximum supported UE per paging message. Few important components of paging design in 5G NR SA system will be considered such as TAC size and RNA (RAN Notification Area) size.

### Paging Frame Structure

Paging frame structure for 5G NR have similar concept as 4G LTE with additional concept of multi beam operation.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%206%20Paging/img/5G_SA_PagingFrame.png" alt="Paging Frame" title="Paging Frame" width=100% height=100% />
</p>
<br />
<br />

### Paging Demand & Blockage Calculation Flow

Paging demand is derived from both paging needed in Core and RAN. Based on this demand and paging frame structure settings, average UE per paging message required can be derived. Paging blocking probability can then be estimated based on maximum UE supported per paging message.


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
                                                                   │
                                                                   │
                                     Maximum                       ▼
                                   Supported UE  ─────────► Paging Blocking
                                  per Paging Msg              Probability

### Assumptions

Asummptions taken for number of MT users in the area:

    # MT Users in the Area during busy hour (Assume)
    mt_rrc_hour = 1800

Asummptions taken for core network initiated paging:

    # Number of cell is TAC area (Assume)
    tac_size = 200

Asummptions taken for radio network initiated paging:

    # Number of cell is RAN Notification area (Assume)
    ran_noti_area = 180

    # Number of times UE goes to RRC_INACTIVE in 1 RRC Session (Assume)
    rrc_inactive = 5

Asummptions taken for maximum UE supported in one paging message: 

    (Assume)
    max_ue_per_paging_msg_val = 16 
   
Network settings for paging frame structure based on 3GPP:

    # Paging Occasion
    N = [1, 1/2, 1/4, 1/8, 1/16, 1/32]      # N = min(T, nB). nB can be [4T, 2T,T, 1/2T, 1/4T, 1/8T, 1/16T, 1/32T]
    Ns = [4, 2, 1]                          # Ns = max(1, nB/T). nB can be [4T, 2T,T, 1/2T, 1/4T, 1/8T, 1/16T, 1/32T]
    
    
    max_ue_per_paging_msg = [4, 8, 12, 16, 20, 24, 28, 32]      # Max supported UE in 1 paging message

### Calculation

Total paging demand is derived as follows:

    # Number of paging per second
    paging_demand = paging_demand_core + paging_demand_ran

    # Number of core paging per second
    paging_demand_core = mt_rrc_hour / 3600 * tac_size                              # 3600 seconds per hour

    # Number of ran paging per second
    paging_demand_ran = mt_rrc_hour / 3600 * rrc_inactive * ran_noti_area           # 3600 seconds per hour

Total paging occasion is derived as follows:

    # Number of paging occasion per second
    paging_occasion = N * Ns * 100                                                   # 100 radio frame per second

Average UE require paging per paging message:

    # Number of UE need paging per paging message
    ue_per_paging_msg = paging_demand/paging_occasion

Paging blocking probability is derived based on Erlang B calculation. (To be studied for better calculation method)
<br />
<br />
<p align="left">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%206%20Paging/img/5G_SA_ErlangB.png" alt="ErlangB" title="ErlangB" width=50% height=50% />
</p>
<br />
<br />

    where: (Assume)
    E = ue_per_paging_msg
    m = max_ue_per_paging_msg_val

### Results

Eg: 5G NR SA paging block probability based on network settings and users demand for paging
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%206%20Paging/img/5G_SA_PagBlock_DemandBased.png" alt="Pagblock_demand" title="Pagblock_demand" width=100% height=100% />
</p>
<br />
<br />

Eg: 5G NR SA paging block probability matrix based on average UE needed paging per paging message and maximum supported UE per paging message

<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%206%20Paging/img/5G_SA_PagBlock_All.png" alt="Pagblock_all" title="Pagblock_all" width=100% height=100% />
</p>
<br />
<br />

<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%206%20Paging/img/5G_SA_PagBlock_Zoom.png" alt="Pagblock_zoom" title="Pagblock_zoom" width=100% height=100% />
</p>
<br />
<br />