# RE Count Based on SCS and Bandwidth

Calculating the Resource Element (RE) count for every FR, SCS, and Bandwidth. Simulation is segregating the count based on normal CP and extended CP.

### Explanation

Based on 3GPP TS 38.101, number of RB for ever SCS and Bandwidth are defined. Based on these values, Resource Element (RE) can be calculated based on the symbol numbers and subcarriers. This simulation will try to calculate number of RE for every 10ms frame.
<br />
<br />
<img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%201%20Operating%20Band%2C%20Frame%20Structure/img/rbcount_table.png" alt="RB Count" title="RB Count" width=100% height=100% />
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

Total RE for every 10ms Frame:
<br />
<br />
<img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%201%20Operating%20Band%2C%20Frame%20Structure/img/recount.png" alt="recount" title="recount" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%201%20Operating%20Band%2C%20Frame%20Structure/img/recount_table.png" alt="recount" title="recount" width=100% height=100% />
<br />
<br />