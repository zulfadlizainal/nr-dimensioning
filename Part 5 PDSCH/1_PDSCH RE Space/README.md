# PDSCH RE Space vs DL Overhead

The objective of this calculation is to estimate how much PDSCH RE is available considering other DL signal overhead. This calculation is a prerequisite for DL throughput calculation.

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
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/DL_Tput_Calc_Concept.jpg" alt="DL Tput Calculation Concept" title="DL Tput Calculation Concept" width=70% height=70% />
</p>
<br />
<br />

### Assumptions

Total DL RE ([Link](https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/tree/master/Part%201%20Operating%20Band%2C%20Frame%20Structure/3_RE%20Count))

    DL Slot Percentage is assumed based on TDD DL Ratio 
    
    Eg: tdd_dl_slot_percent = 70%

    total_dl_re_frame = total_re_frame * tdd_dl_slot_percent

SSB RE ([Link](https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/tree/master/Part%202%20Syncronization))

    SSB Size (Specs)

    ssb_symbols = 4
    ssb_subcarriers = 270

    No of Beams (Assume) - No of SSB Beam / SSB Burst (L) can be FR1 = [1, 2, 4, 8], FR2 = [1, 2, 4, 8, 16, 32, 64]

    ssb_beam_fr1 = 4
    ssb_beam_fr2 = 16

    SSB Periodicity (Assume) - SSB Periodicity (ms) can be [5, 10, 20, 40, 80, 160]

    ssb_periodicity_fr1 = 10
    ssb_periodicity_fr2 = 10

    SSB RE/Frame

    ssb_re_frame = ssb_symbols * ssb_subcarriers * ssb_beam * (10/ssb_periodicity)

DL DMRS RE

    DMRS Rules (Specs)

    Type1:

    1. One OFDM Symbols = Up to 4 Ports
    2. Two OFDM Symbols = Up to 8 Ports

    Type2:

    1. One OFDM Symbols = Up to 6 Ports
    2. Two OFDM Symbols = Up to 12 Ports

    DMRS Ports (Assume)

    dmrs_ports_fr1 = 4
    dmrs_ports_fr2 = 4

    DMRS Symbols (Assume) - Can be One or Two

    dmrs_symbols_fr1 = 2
    dmrs_symbols_fr2 = 2

    PDSCH Layers (Assume)

    pdsch_layer_number_fr1 = 4
    pdsch_layer_number_fr2 = 4

    DL DMRS RE/Frame

    dl_dmrs_re_frame = RB Count * (Slots/Frame') * tdd_dl_slot_percent * (dmrs_ports * dmrs_symbols * pdsch_layer_number)

DL CSI RE

    CSI-RS Port (Assume) -  Based on CSI-RS Settings table

    csi_rs_port_fr1 = 4
    csi_rs_port_fr2 = 4

    CSI-RS Slot Periodicity (Assume) -  can be [4, 5, 8, 10, 16, 20, 40, 80, 160, 320]

    csi_rs_slot_periodicity_fr1 = 4
    csi_rs_slot_periodicity_fr2 = 20

    DL CSI-RS RE/Frame

    dl_csi_re_frame = RB Count * csi_rs_port * (10/(csi_rs_slot_periodicity * Slot Duration (ms)']))

Reference for CSI-RS settings from 3GPP TS 38.211

<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/3GPP_TS_38_211_CsiRsSettings.jpg" alt="CSI RS Table 3GPP" title="CSI RS Table 3GPP" width=100% height=100% />
</p>
<br />

DL PTRS RE

    PTRS Rules (Specs)

    1. Only for High Frequency Phase Tracking (mmWave/FR2)
    2. Configured by RRC
    3. Time Density (TD) PTRS increase when MCS increase
    4. Frequency Density (FD) decrease when BW increase

    CP Config (Specs)

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

    DL PT-RS RE/Frame

    dl_ptrs_re_frame = (RB Count / ptrs_frequency_density) * (Slots/Frame) * tdd_dl_slot_percent * ((normal_cp_symbols - pdcch_symbols - dmrs_symbols) / ptrs_time_density)

DL TRS RE

    TRS RE / RB - Only 3 RE/RB (Specs)

    trs_subcarrier_perRB_fr1 = 3
    trs_subcarrier_perRB_fr2 = 3

    TRS Symbol / Burst (Assume) - 4 Symbol for FR1, can be [2, 4] Symbol for FR2

    trs_symbol_perBurst_fr1 = 4
    trs_symbol_perBurst_fr2 = 4

    TRS Burst Periodicity (Assume) - can be [10, 20, 40, 80] ms

    trs_burst_periodicity_fr1 = 80
    trs_burst_periodicity_fr2 = 80

    DL CSI-RS RE/Frame

    dl_trs_re_frame = RB Count * trs_subcarrier_perRB * trs_symbol_perBurst * (10/trs_burst_periodicity)
    
PDCCH RE ([Link](https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/tree/master/Part%204%20DL%20Common%20Channel))

    PDCCH RE is really flexible in 5G and can be a lot based on demand. For this simulation - asummption of PDCCH resources is assumed.

    pdcch_usage_percentage_fr1 = 1.2/100
    pdcch_usage_percentage_fr2 = 0.25/100

    PDCCH RE/Frame

    dl_pdcch_re_frame = pdcch_usage_percentage * (Normal CP RE/Frame)
    
### Calculation

DL Overhead

    dl_overhead_frame = ssb_re_frame + dl_dmrs_re_frame + dl_csi_re_frame + dl_ptrs_re_frame + dl_trs_re_frame + dl_pdcch_re_frame

PDSCH RE

    pdsch_re_frame = total_dl_re_frame - dl_overhead_frame

### Results

PDSCH RE vs DL Overhead for 5G Sub6 and mmWave.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/PDSCHvsOverhead.jpg" alt="PDSCH RE vs DL Overhead" title="PDSCH RE vs DL Overhead" width=100% height=100% />
</p>
<br />
<br />

DL channels/signals distribution for 5G Sub6 and mmWave.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/ChannelAlloc.jpg" alt="Channel Distribution DL" title="Channel Distribution DL" width=100% height=100% />
</p>
<br />
<br />