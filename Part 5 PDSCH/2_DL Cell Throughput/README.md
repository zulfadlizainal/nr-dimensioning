# Cell DL Throughput

The objective of this calculation is to estimate DL cell throughput for 5G NR based on remaining PDSCH RE available after considering DL physical channel overhead. The calculation will incorporated available PDSCH RE with spectral efficiency collected in the field using Qualcomm chipset UE.

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
                              Network ◄─────── ┤ Spatial Layer
                              Testing          │
                                │              │ MU-MIMO Gain
                                │              │
                                ▼              │ DL BLER
          Available          Spectral
           PDSCH             Efficiency
            RE                Curve
            │                   │
            │                   │
            │                   │
            └───► Calculate ◄───┘
                     │
                     │
                     ▼
              DL Cell Throughput

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

### Calculation

DL Cell Throughput formula is constructed as below:

    dl_cell_throughput_mbps = (PDSCH-RE/Frame * radio_frame_sec) * (Estimated SE (bps/Hz) * (SCS (kHz)*1000) /((normal_cp_symbols * (Slots/Frame) * 100) / 1000000 ) * (1 + dl_mu_mimo_gain) * (1 - dl_bler)

    where:

    radio_frame_sec = 100
    normal_cp_symbols = 14
    dl_mu_mimo_gain = 0/100 (SE Calculation already considers MU-MIMO gain)
    dl_bler = 0/100 (SE Calculation already considers BLER)

### Results

Eg: 5G NR DL cell throughput based on bandwidth
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/DL_Cell_Throughput_Result_Title.png" alt="5G DL Cell Throughput" title="5G DL Cell Throughput" width=100% height=100% />
</p>
<br />
<br />
