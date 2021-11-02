# PDCCH Utilization

The objective of this simulation is to calculate how many PDCCH Utilization % needed with a certain sets of scheduling demand. This simulations will consider the factor of CCE aggregation level based on PDSCH SINR.

### Simulation Concept Diagram

    ┌─────────────┐                     ┌─────────────┐
    │             │                     │             │
    │  Calculate  │                     │  Calculate  │
    │  5G Data    │                     │  5G VoNR    │
    │  Scheduling │                     │  Scheduling │
    │  Demand     │                     │  Demand     │
    │             │                     │             │
    └──────┬──────┘                     └─────┬───────┘
           │                                  │
           └────────────────┬─────────────────┘
                            │
                            │
                            │
                            │
                     ┌──────▼──────┐                    ┌─────────────────────────────────────┐
                     │  Simulate   │                    │ Input CCE Aggregation Factor        │
                     │  PDCCH CCE  ◄────────────────────┤ OR                                  │
                     │  & PDCCH RE │                    │ RF Condition Impact to CCE Decoding │
                     │  Needed     │                    └─────────────────────────────────────┘
                     └────┬─┬─┬────┘
                          │ │ │
                          │ │ │
                          │ │ │
                          │ │ │
                          │ │ │
                          ▼ ▼ ▼   
                    PDCCH Utilization %
                  (DIMENSIONING REFERENCE)

### Assumptions

Based on NR scheduling demand in ([5G Data Scheduling Demand](https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/tree/master/Part%204%20DL%20Common%20Channel/1_Demand%20Data%20Scheduling)) and ([5G VoNR Scheduling Demand](https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/tree/master/Part%204%20DL%20Common%20Channel/2_Demand%20Voice%20Scheduling)), the ([PDCCH CCE and RE](https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/tree/master/Part%204%20DL%20Common%20Channel/3_PDCCH%20Demand) needed for these scheduling demand is calculated.

The simulations also consider RF condition factor towards CCE aggregation level. Actual PDSCH SINR vs CCE Aggregation level from live network is being used as an assumptions.

<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%204%20DL%20Common%20Channel/img/SINR_CCE_Relation.png" alt="SINR-CCE Relation" title="SINR CCE-Relation" width=50% height=50% />
</p>
<br />
<br />

PDCCH/DCI - CCE - REG - RE Mapping in 5G NR

    RE │
    RE │
    RE │
    RE │
    RE │  12REs
    RE ├────────► REG │
    RE │              │
    RE │          REG │
    RE │              │
    RE │          REG │  6REGs
    RE │              ├────────► CCE │
    RE │          REG │              │
                      │          CCE │
                  REG │              │
                      │          CCE │
                  REG │              │
                                 CCE │
                                     │
                                 CCE │
                                     │
                                 CCE │
                                     │
                                 CCE │
                                     │
                                 CCE │  1,2,4,8,16CCEs Depending on RF Condition
                                     ├────────► DCI/PDCCH
                                 CCE │
                                     │
                                 CCE │
                                     │
                                 CCE │
                                     │
                                 CCE │
                                     │
                                 CCE │
                                     │
                                 CCE │
                                     │
                                 CCE │
                                     │
                                 CCE │

Maximum 3 PDCCH symbols is assummed to be used in this simulation.

    12 │ RE
       │ RE
    S  │ RE
    u  │ RE
    b  │ RE
    c  │ RE
    a  │ RE
    r  │ RE
    r  │ RE
    i  │ RE
    e  │ RE
    r  ▼ RERERE
    s    ─────►
         3 Symbols

### Calculation

PDCCH Utilization %

    PDCCH CCE RE Needed / (Number of PRB * 12 Subcarriers * PDCCH OFDM Symbols * Number of DL Slots per Frame)

    ** Number of PRB in 5G depends on total bandwidth and SCS
    ** Number of DL Slots per Frame depending on % of TDD DL slots in a 10ms frame


### Results

Eg: The number of CCE / frame & CCE-RE / frame needed based on CCE aggregation level.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%204%20DL%20Common%20Channel/img/CCE-RE_AggLev_Combine.png" alt="CCE-RE per Aggr Level" title="CCE-RE per Aggr Level" width=100% height=100% />
</p>
<br />
<br />

Eg: The number of CCE / frame & CCE-RE / frame needed based on PDSCH SINR.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%204%20DL%20Common%20Channel/img/CCE-RE_SINR_Combine.png" alt="CCE-RE per SINR" title="CCE-RE per SINR" width=100% height=100% />
</p>
<br />
<br />
