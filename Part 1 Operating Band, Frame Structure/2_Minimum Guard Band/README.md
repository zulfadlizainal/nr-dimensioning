# Minimum Guard Band

Reference: 3GPP TS 38.101

### Explanation

Table from 3GPP for FR1 and FR2:
<br />
<br />
<img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%201%20Operating%20Band%2C%20Frame%20Structure/img/minguardband_table.png" alt="Minimum Guard Band" title="Minimum Guard Band" width=100% height=100% />
<br />
<br />

### Calculation

The minimum guard bands have been calculated using the following equation: 

    (Channel Bandwidth x 1000 (kHz) - RB value x SCS x 12) / 2 - SCS/2

Taking example for 5MHz channel BW with 25 NRB & 15kHz Subcarrier Spacing

    (5 x 1000 – 25 x 15 x 12) / 2 – 15 / 2
    = (5000kHz – 4500kHz) / 2 – 15kHz / 2
    = 500kHz / 2 – 7.5kHz
    = 242.5 kHz

### Results

Plotting for the mentioned table. Lower bandwidth need smaller kHz for guarband however the occupancy % is much higher.

<br />
<br />
<img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%201%20Operating%20Band%2C%20Frame%20Structure/img/minguardband.png" alt="Minimum Guard Band" title="Minimum Guard Band" width=100% height=100% />
<br />
<br />