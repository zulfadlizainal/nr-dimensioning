# PDCCH CCE and PDCCH RE Demand

The objective of this simulation is to calculate how many PDCCH CCE and PDCCH RE needed with a certain sets of scheduling demand. This simulations will consider the factor of CCE aggregation level based on PDSCH SINR.

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
    
                       FINAL GOAL
                   PDCCH DIMENSIONING

### Assumptions

Based on NR scheduling demand in ([5G Data Scheduling Demand](https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/tree/master/Part%204%20DL%20Common%20Channel/1_Demand%20Data%20Scheduling)) and ([5G VoNR Scheduling Demand](https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/tree/master/Part%204%20DL%20Common%20Channel/2_Demand%20Voice%20Scheduling)), the PDCCH CCE and PDCCH RE will be calcualted.

Additional assumptions for this simulations includes a consideration of RF condition factor towards CCE aggregation level. Actual PDSCH SINR vs CCE Aggregation level from live network is being used as an asuumptions.

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

### Calculation

Number of PDCCH CCE Needed / 10ms Frame

    (Demand for Data Scheduling + Demand for VoNR Scheduling) * CCE Aggregation Level

Number of PDCCH RE Needed / 10ms Frame

    (Demand for Data Scheduling + Demand for VoNR Scheduling) * CCE Aggregation Level * 6 * 12

    ** 6 refers to 6 REGs in 1 CCE
    ** 12 refers to 12 REs in 1 REG


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
