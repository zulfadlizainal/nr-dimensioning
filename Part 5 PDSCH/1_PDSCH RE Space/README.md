# PDSCH RE Space vs DL Overhead

The objective of this calculation is to estimate how much PDSCH RE is available considering other DL signal overhead. This calculation is important because PDSCH RE directly correlated to DL throughput that its going to generate.

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

To calculate throughput for DL, total PDSCH RE first need to be estimated.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/DL_Tput_Calc_Concept.jpg" alt="DL Tput Calculation Concept" title="PDSCH RE vs DL Overhead" width=70% height=70% />
</p>
<br />
<br />

### Assumptions

Overall DL RE/Frame ([Link](https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/tree/master/Part%201%20Operating%20Band%2C%20Frame%20Structure/3_RE%20Count)

    DL Slot Percentage is assumed based on TDD DL Ratio 
    
    Eg: tdd_dl_slot_percent = 70%

DL DMRS RE

    XXX

DL PTRS RE

    1. Only for High Frequency Phase Tracking (mmWave/FR2)
    2. Configured by RRC
    3. Time Density (TD) PTRS increase when MCS increase
    4. Frequency Density (FD) decrease when BW increase

    normal_cp_symbols = 14
    extended_cp_symbols = 12

    PTRS Time Density (Assume) - can be [n/a, 1, 2, 4]

    ptrs_time_density_fr1 = 0
    ptrs_time_density_fr2 = 1

    PTRS Frequency Density (Assume) - can be [n/a, 1, 2, 4, 8. 16]

    ptrs_frequency_density_fr1 = 0
    ptrs_frequency_density_fr2 = 2

    PDCCH Symbols (Assume) - can be [1, 2, 3]

    pdcch_symbols_fr1 = 3
    pdcch_symbols_fr2 = 3

    DL PTRS RE = (RB / ptrs_frequency_density) * Slots/Frame * tdd_dl_slot_percent * ((normal_cp_symbols - pdcch_symbols -
         dmrs_symbols) / ptrs_time_density)

DL TRS RE

    XXX

DL CSI RE

    XXX

SSB RE

    XXX

PDCCH RE

    XXX

### Calculation

PDSCH RE

    XXX

DL Overhead

    XXX

### Results

PDSCH RE vs DL Overhead for 5G Sub 6 and mmWave.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/PDSCHvsOverhead.jpg" alt="PDSCH RE vs DL Overhead" title="PDSCH RE vs DL Overhead" width=100% height=100% />
</p>
<br />
<br />

5G DL Channels and Signals distribution for 5G Sub 6 and mmWave.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/ChannelAlloc.jpg" alt="Channel Distribution DL" title="Channel Distribution DL" width=100% height=100% />
</p>
<br />
<br />