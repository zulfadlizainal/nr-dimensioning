# SI Occupancy

Calculating the resource utilized by System Information (SI) corresponding to number of beams transmitting SI and SI periodicity. Simulation will consider 2 types of SI: 

    1) RMSI (Required Minimum System Information) - SIB1 NR
    2) OSI (Other System Information) - In this example calculating SIB2 NR

### Assumptions

To first understand the resource occupied by SI, we need to understand on how to calculate the total RE in 5G NR resource grid based on bandwidth. For the total RE calculation for NR, refer to this link ([Link](https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/tree/master/Part%201%20Operating%20Band%2C%20Frame%20Structure/3_RE%20Count)) .

The assumptions taken in calculating RMSI resource utilization in this simulation:

    1. RMSI (SIB1) will use between 1008 RE to 2016 RE depending on informations it need to broadcast in SIB1.
    2. Number of beams for SI is assumed to be similar to the number of beams supported for SSB in SUB6 and mmWave.
    3. RMSI periodicity is assumed to be similar as SSB periodicity for initial access (20ms).

The assumptions taken in calculating OSI resource utilization in this simulation (Eg: SIB2):

    1. OSI will use between 504 RE to 2016 RE depending on informations it need to broadcast in the SIB (In this Eg: SIB2).
    2. Number of beams for SI is assumed to be similar to the number of beams supported for SSB in SUB6 and mmWave.
    3. OSI periodicity is based on si-Periodicity parameter defined in RMSI as stated in 3GPP TS 38.331. 

### Calculation

SI Occupancy / Frame (%) Formulae References

    ((No of RE Used for SI / (SI Periodicity (ms) / 10ms Frame)) * No of Beams) / (Total RE/Frame)

### Results

Eg: The resource utilized by RMSI (SIB1 NR) for 20ms RMSI periodicity in different beam settings for SCS 60kHz and BW 50MHz:
<br />
<br />
<img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%203%20System%20Information/img/si_rmsi_result.png" alt="RMSI (SIB1 NR)" title="RMSI (SIB1 NR)" width=100% height=100% />
<br />
<br />
Eg: The resource utilized by OSI (SIB2 NR) for different SI periodicity in different beam settings for SCS 60kHz and BW 50MHz:
<br />
<br />
<img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%203%20System%20Information/img/si_osi_result.png" alt="OSI (SIB2 NR)" title="OSI (SIB2 NR)" width=100% height=100% />
<br />
<br />

