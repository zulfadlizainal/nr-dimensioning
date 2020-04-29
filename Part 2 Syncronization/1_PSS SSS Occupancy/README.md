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

The concept of SSB count/Burst set (Multiple SSB in 1 SSB Burst Set) and SSB Burst Set periodicity:
<br />
<br />
<img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%202%20Syncronization/img/ssb_burst_periodicity.png" alt="SSB Periodicity" title="SSB Periodicity" width=100% height=100% />
<br />
<br />

Parameter L & p that being considered in this simulation:

L = Total number of SSB count inside 1 SSB Burst Set (Important during beam sweeping, more L means more beam)
p = SSB Burst Set periodicity (How often SSB Burst is being repeated in time domain)

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

Definition of Frame

    1 Frame = 10 Subframe
    1 Subframe = 1 ms
    1 Frame = 10ms

Definition of RB

    1 RB = 12 Subcarriers

PSS and SSS Size

    PSS Size = 127 Subcarriers x 1 Symbol
    SSS Size = 127 Subcarriers x 1 Symbol

For FR1, SSB Count in SSB Burst Set can be up until 4 and 8 (LMax = 4 for < 3GHz, LMax = 8 for ~3-6GHz)

    L = 1, 2, 4, 8

For FR2, SSB Count in SSB Burst Set can be up until 64 (LMax = 64)

    L = 1, 2, 4, 8, 16, 32, 64

For SSB Periodicity, it can be set based on spec

    p = 5, 10, 20, 40, 80, 160 ms

PSS + SSS Occupancy (%) - Use 1 Seconds as benchmark

    PSS + SSS Occupancy (%) = ((PSS Size+SSS Size)*L*SSB Burst Count in 1 Sec)/Total RE per Sec

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
