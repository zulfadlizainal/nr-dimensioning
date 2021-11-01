# Demand for VoNR Scheduling

The objective of this simulation is to calculate the demand for VoNR scheduling in 5G NR. This simulations will take multiple input as considerations: 

    1) Number of VoNR subscribers
    2) Call duration
    3) Number of call
    4) Activity period factor
    5) Scheduling periodicity

### Assumptions

Below are definitions for taken assumptions:

Number of VoNR subscribers

    Total number of VoNR devices in a cell

Call duration (Erlang)

    Average duration of each call in seconds / 3600 to convert it to Erlang.

Number of call

    Average number of voice call per UE in busy hour. This should consider both triggered by MO and MT UE.

Activity period factor (%)

    Average of time where voice packet actually transferred in each call in %. This should consider both DL and UL activity.

Scheduling periodicity (ms)

    DL and UL data scheduling interval.

### Calculation

Number of Scheduling Needed / 10ms Frame

    Number of VoNR subscribers * Call duration (Erlang) * Number of call * Activity period factor (%) * (10ms/Scheduling periodicity (ms)) * (1+BLER)


### Results

Eg: The number of scheduling demand / frame for a range of subscribers with different user behaviour.
<br />
<br />
<p align="center">
    <img src="https://github.com/zulfadlizainal/5G-NR-Planning-And-Dimensioning/blob/master/Part%204%20DL%20Common%20Channel/img/Scheduled_Voice.png" alt="Voice Scheduling Demand" title="Voice Scheduling Demand" width=50% height=50% />
</p>
<br />
<br />

