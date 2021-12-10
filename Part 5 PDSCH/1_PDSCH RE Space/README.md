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

XXX

### Calculation

PDSCH RE

    PDCCH CCE RE Needed / (Number of PRB * 12 Subcarriers * PDCCH OFDM Symbols * Number of DL Slots per Frame)

    ** Number of PRB in 5G depends on total bandwidth and SCS
    ** Number of DL Slots per Frame depending on % of TDD DL slots in a 10ms frame

DL Overhead

    PDCCH CCE RE Needed / (Number of PRB * 12 Subcarriers * PDCCH OFDM Symbols * Number of DL Slots per Frame)

    ** Number of PRB in 5G depends on total bandwidth and SCS
    ** Number of DL Slots per Frame depending on % of TDD DL slots in a 10ms frame

### Results

PDSCH RE vs DL Overhead for 5G Sub 6 and mmWave.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/PDSCHvsOverhead.jpg" alt="PDSCH RE vs DL Overhead" title="PDSCH RE vs DL Overhead" width=70% height=70% />
</p>
<br />
<br />

5G DL Channels and Signals distribution for 5G Sub 6 and mmWave.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%205%20PDSCH/img/ChannelAlloc.jpg" alt="Channel Distribution DL" title="Channel Distribution DL" width=70% height=70% />
</p>
<br />
<br />