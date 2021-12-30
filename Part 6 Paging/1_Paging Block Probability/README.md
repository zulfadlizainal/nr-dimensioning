# Paging Blocking Probability

The objective of this calculation is to estimate the paging blocking probability of required paging by UE based on paging strategy and maximum supported UE per paging message. Few important components of paging design in 5G NR SA system will be considered sucsh as TAC size and RNA size.

### Paging Frame Structure

To calculate throughput for DL, total PDSCH RE first need to be estimated. Calculation for PDSCH RE is based on this link.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%206%20Paging/img/5G_SA_PagingFrame.png" alt="Paging Frame" title="Paging Frame" width=100% height=100% />
</p>
<br />
<br />

### Paging Demand Calculation Flow

XXX


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

Available PDSCH RE ([Link](https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/tree/master/Part%205%20PDSCH/1_PDSCH%20RE%20Space))

    XXX

Spectral efficiency is derived from actual network testing using Qualcomm chipset UE. Similar spectral efficiency is assumed for all bands in this simulation.
    
    XXX

Spectral efficiency curve derived from network testing is smoothen using polynomial regression (to derive estimated value). It is then compared with Shannon Theorem estimation for accuracy confirmation. Estimated spectral efficiency is choosen to be used this simulation. 
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/SE_NSA_3.5G.png" alt="SE" title="SE" width=70% height=70% />
</p>
<br />
<br />

Users are randomly distributed in each cell from good RF range to poor RF range. 
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/DL_User_Throughput_UserLoc.png" alt="User Location" title="User Location" width=70% height=70% />
</p>
<br />
<br />

Available PDSCH RE is distributed to every UE based on simplified round robin resource allocation technique. With this scheduler, every UE is assumed to get resource in time domain manner without any prioritization.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/DL_User_Throughput_RoundRobin.png" alt="RR" title="RR" width=100% height=100% />
</p>
<br />
<br />

Below relation between SS-RSRP and SS-RSRQ & SS-SINR is used for RF relation derivation.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/DL_User_Throughput_RFRelation.png" alt="RF Relation" title="RF Relation" width=70% height=70% />
</p>
<br />
<br />

### Calculation

DL User Throughput formula is constructed as below:

    dl_user_throughput_mbps = (PDSCH-RE/Frame/User * radio_frame_sec) * (Estimated SE (bps/Hz) * (SCS (kHz)*1000) /((normal_cp_symbols * (Slots/Frame) * 100) / 1000000 ) * (1 + dl_mu_mimo_gain) * (1 - dl_bler)

    where:

    radio_frame_sec = 100
    normal_cp_symbols = 14
    dl_mu_mimo_gain = 0/100 (SE Calculation already considers MU-MIMO gain)
    dl_bler = 0/100 (SE Calculation already considers BLER)

VoNR required throughput is deducted from DL User Throughput to ensure guaranteed VoNR call at any session:

    where: 
    
    vonr_tput_mbps = 0.128

DL User Throughput considers user activity factor based on % of time where scheduling is needed:

    where:

    full_buffer_ue = 100/100
    high_demand_ue = 80/100 
    low_demand_ue = 20/100

### Results

Eg: 5G NR DL user throughput for FR1 30kHz SCS 100MHz Bandwidth
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/DL_User_Throughput_UserLocResult.png" alt="User Tput / Loc" title="User Tput / Loc" width=100% height=100% />
</p>
<br />
<br />

<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/DL_User_Throughput_RP_SNR_Result.png" alt="User Tput RF" title="User Tput RF" width=100% height=100% />
</p>
<br />
<br />