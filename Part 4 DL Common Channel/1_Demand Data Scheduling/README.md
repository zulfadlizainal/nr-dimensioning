# Demand for Data Scheduling

The objective of this simulation is to calculate the demand for data scheduling in 5G NR. This simulations will take multiple input as considerations: 

    1) Number of subscribers
    2) Connection duration
    3) Number of RRC connections
    4) Activity period factor
    5) Scheduling periodicity

### Assumptions

Below are definitions for taken assumptions:

Number of subscribers 

    Total number of data devices in a cell

Connection duration (Erlang)

    Average duration of each RRC connections in seconds / 3600 to convert it to Erlang.

Number of RRC connections

    Average RCC connections number per UE in busy hour. This should consider both RRC triggered by MO and MT UE.

Activity period factor (%)

    Average of time where data actually transferred in each RRC connections in %. This should consider both DL and UL activity.

Scheduling periodicity (ms)

    DL and UL data scheduling interval.

### Calculation

Number of Scheduling Needed / 10ms Frame

    Number of subscribers * Connection duration (Erlang) * Number of RRC connections * Activity period factor (%) * (10ms/Scheduling periodicity (ms)) * (1+BLER)


### Results

Eg: The number of scheduling demand / frame for a range of subscribers with different user behaviour.
<br />
<br />
<img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%204%20DL%20Common%20Channel/img/Scheduled_Data.png" alt="Data Scheduling Demand" title="Data Scheduling Demand" width=100% height=100% />
<br />
<br />

