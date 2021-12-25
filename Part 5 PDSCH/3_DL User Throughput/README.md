# User DL Throughput

The objective of this calculation is to estimate DL user throughput for 5G NR based on user location within the cell. The estimaation will incorporated the factor of UE number in a cell, its radio conditon, and its activity behaviour.

### RE Type for DL and UL

                       5G NR RE
                          │
            ┌─────────────┴────────────┐
            ▼                          ▼
          DL RE                      UL RE
            │                          │
            ▼                          ▼
        PDSCH RE                   PUSCH RE
        PDCCH RE                   PUCCH RE
        SSB RE                     PRACH RE
        DL DMRS RE                 UL DMRS RE
        DL CSI RE                  UL PTRS RE
        DL TRS RE                  SRS RE
        DL PTRS RE

### DL Throughput Calculation Flow

To calculate throughput for DL, total PDSCH RE first need to be estimated. Calculation for PDSCH RE is based on this link. ([Link](https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/tree/master/Part%205%20PDSCH/1_PDSCH%20RE%20Space))
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/DL_Tput_Calc_Concept.jpg" alt="DL Tput Calculation Concept" title="DL Tput Calculation Concept" width=70% height=70% />
</p>
<br />
<br />

Once available PDSCH RE is calculated, it is then converted to throughput based spectral efficiency collected in the field using Qualcomm chipset UE.

                                                     │ MCS
                                                     │
                                     Network ◄───────┤ Spatial Layer
                                     Testing         │
                                        │            │ MU-MIMO Gain
                                        │            │
                                        ▼            │ DL BLER
                Available            Spectral
                  PDSCH             Efficiency
                   RE                 Curve
                    │                   │
                    │                   │
                    ▼                   │
             Allocate PDSCH             │
              RE to Every               │
              UE in a Cell              │
                    │                   │
                    │                   │
                    │                   │
                    │     Calculate     │
                    └───► Throughput◄───┘
                         for Every UE
                              │
                              │
                              ▼
                         Deduct VONR
                          Throughput
                         Reservation
                              │
                              │
                              ▼
                         Estimate User
                          Throughput
                         Based on User
                           Activity

### Assumptions

Available PDSCH RE ([Link](https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/tree/master/Part%205%20PDSCH/1_PDSCH%20RE%20Space))

    DL Slot Percentage is assumed based on TDD DL Ratio 
    
    Eg: tdd_dl_slot_percent = 70%

    total_dl_re_frame = total_re_frame * tdd_dl_slot_percent

Spectral efficiency is derived from actual network testing using Qualcomm chipset UE. Similar spectral efficiency is assumed for all bands in this simulation.
    
    Network settings:

    1. NSA ENDC
    2. Band 3.5GHz Sub6
    3. Max MIMO Layer = 4
    4. BLER = 10%
    5. MU-MIMO = Not supported

    UE type:

    1. Qualcomm chipset UE
    2. Support all 5 features mentioned in the network settings

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
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/DL_User_Throughput_UserLoc.png" alt="User Location" title="User Location" width=100% height=100% />
</p>
<br />
<br />

Available PDSCH RE is distributed to every UE based on simplified round robin resource allocation technique.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/DL_User_Throughput_RoundRobin.png" alt="RR" title="RR" width=70% height=70% />
</p>
<br />
<br />

Below relation between SS-RSRP and SS-SINR/RSRQ is used for mapping purpose.
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

VoNR required throughput is deducted from DL User Throughput:

    where: 
    
    vonr_tput_mbps = 0.128

DL User Throughput considers user activity factor:

    where:

    full_buffer_ue = 100/100
    high_demand_ue = 80/100 
    low_demand_ue = 20/100

### Results

Eg: 5G NR DL user throughput for FR1 30kHz SCS 100MHz Bandwidth
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/DL_User_Throughput_3DResult.png" alt="User Tput 3D" title="User Tput 3Dt" width=70% height=70% />
</p>
<br />
<br />

<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/DL_User_Throughput_UEID.png" alt="User Tput" title="User Tput" width=70% height=70% />
</p>
<br />
<br />

<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/DL_User_Throughput_RSRP.png" alt="User Tput_RP" title="User Tput_RP" width=70% height=70% />
</p>
<br />
<br />

<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/DL_User_Throughput_SINR.png" alt="User Tput_SINR" title="User Tput_SINR" width=70% height=70% />
</p>
<br />
<br />

