# PSS and SSS Occupancy

Calculating the resource utilized by PSS and SSS depending on L (Count of SSB in 1 SSB Burst Set) and p (SSB Periodicity). Simulation will limit the SCS that can be used to implement SSB.

### Explanation

To first understand the resource occupied by PSS and SSS, we need to understand on how to calculate the total RE in 5G NR resource grid based on bandwidth. The total RE calculation can refer to this link ([Link](https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/tree/master/Part%201%20Operating%20Band%2C%20Frame%20Structure/3_RE%20Count)) .

Next, the structure and size of PSS and SSS inside the SSB need to be considered based on below diagram:
<br />
<br />
<img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%202%20Syncronization/img/ssb_structure.png" alt="SSB Structure" title="SSB Structure" width=100% height=100% />
<br />
<br />

The concept of SSB Burst Set (Multiple SSB in 1 SSB Burst) and SSB Burst Set periodicity:
<br />
<br />
<img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%202%20Syncronization/img/ssb_burst_periodicity.png" alt="SSB Periodicity" title="SSB Periodicity" width=100% height=100% />
<br />
<br />

Parameter L & p that being considered in this simulation:
<br />
<br />
<img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%202%20Syncronization/img/ssb_parameter.png" alt="L&p" title="L&p" width=100% height=100% />
<br />
<br />

### Calculation

The number of slot for every 1ms subframe based on SCS

    SCS 15kHz = 1 Slot/Subframe
    SCS 30kHz = 2 Slot/Subframe
    SCS 60kHz = 4 Slot/Subframe
    SCS 120kHz = 8 Slot/Subframe

Definition of Slot Based on CP Type

    1 Slot = 14 OFDM Symbols (Normal CP)
    1 Slot = 12 OFDM Symbols (Extended CP)

Definition of Frame

    1 Frame = 10 Subframe
    1 Subframe = 1 ms
    1 Frame = 10ms

Definition of RB

    1 RB = 12 Subcarriers

### Results

The resource utilized by PSS and SSS depending on L (Count of SSB in 1 SSB Burst Set) and p (SSB Periodicity).
<br />
<br />
<img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%202%20Syncronization/img/pss_sss_scs15_result.png" alt="SCS15" title="SCS15" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%202%20Syncronization/img/pss_sss_scs30_result.png" alt="SCS30" title="SCS30" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%202%20Syncronization/img/pss_sss_scs120_result.png" alt="SCS120" title="SCS120" width=100% height=100% />
<br />
<br />
