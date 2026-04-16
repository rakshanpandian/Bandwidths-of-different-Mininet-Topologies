# Bandwidths-of-different-Mininet-Topologies

Different network topologies give different throughputs based on the Bandwidths they are provided with. Here I will be testing out three different types of topologies on the same bandwidth value of 10MBps.

# Bus Topology
In a Bus Topology there is a singular linear line by which every host sends it's packets via the shared channel. Each host has a switch and each switch is connected to each other. The switch at the end however is not connected to the switch at the beginning. There is a clearly defined beginning and end present.<br>

![](https://github.com/rakshanpandian/Bandwidths-of-different-Mininet-Topologies/blob/main/bus%20topo.png)

## Bandwidth 10MBps

<img width="940" height="556" alt="image" src="https://github.com/user-attachments/assets/55586b33-f106-4a93-9470-cecdf9ca7c49" />
As seen here h1 can't reach h3. This is because a rule has been set within the ryu controller to filter any packets going from h1 to h3 and vice versa. This filter exists or every topology in use

<img width="940" height="556" alt="image" src="https://github.com/user-attachments/assets/ce5fad97-1d6f-42dc-a002-274264bbda89" />

As seen here the logs show how everything is filtered and what pings to what ip.

<img width="940" height="556" alt="image" src="https://github.com/user-attachments/assets/149e450e-643a-4c4a-8ecb-70e7d8238a4c" />

We set the server to run iperf on in host 4. From there we use iperf it to send packets via host 2 to host 4. As per the iperf we see that the real bandwidth available for this topology is 8.06MBps. The throughput can be determined as 0.965346534653 MBps

<img width="940" height="556" alt="image" src="https://github.com/user-attachments/assets/a4281101-bed5-4a7c-98eb-fc5c4e7d2021" />

As we can see here this is the respective flow table for the topology.

# Ring Topology
Think about what would happen if you linked the end of the line with it's beginning and you'd arrive at the ring topology. Due to it's more complex structure it can run into more issues.

![](https://github.com/rakshanpandian/Bandwidths-of-different-Mininet-Topologies/blob/main/Ring%20topo.png)

## Bandwidth 10MBps

<img width="940" height="556" alt="image" src="https://github.com/user-attachments/assets/ace9c3a5-b6be-4b55-90f9-7e9c33d2a65f" />
<img width="940" height="556" alt="image" src="https://github.com/user-attachments/assets/faea2ba2-2e8d-4e0a-976f-58b8d265e60a" />

As can be seen here it is hard to ping the different hosts for a ring topology. This stems from it's cyclical structure which makes it harder for the switches to determine where to forward a packet. However with the final pings we see that they are able to find where they can ping their packets.

<img width="940" height="556" alt="image" src="https://github.com/user-attachments/assets/13589173-1ce0-45f9-97f2-f6a1dde0da8e" />

However as shown, they still can block pings from h1 to h3.

<img width="940" height="556" alt="image" src="https://github.com/user-attachments/assets/5f2912a6-7510-4fc7-836e-3e2f9e069074" />
As per the iperf operation we get a higher bandwidth as compared to the bus topology as they have a shared network. Furthermore, the throughput of the topology gives a considerable 1.108910891089109MBps which is higher than the bus topology.

<img width="940" height="556" alt="image" src="https://github.com/user-attachments/assets/7cc35f3b-b23d-45c3-bf53-b5a70b45ecd1" />
The resulting flow diagram results in this.

# Tree Topology
With this topology a switch has one or more host nodes tied to it. Every switch at the very bottom level of a 'tree' is connected to a set of switches above. And so on and so on till there is a singular root switch which controls all communication with seperate parts of the network.

![](https://github.com/rakshanpandian/Bandwidths-of-different-Mininet-Topologies/blob/main/tree%20topo.png)


## Bandwidth 10MBps

<img width="940" height="556" alt="image" src="https://github.com/user-attachments/assets/1ef094f5-d305-4173-bcbd-2f8b39f7ba00" />

As can be seen every member of the tree can ping each other excluding h1<->h3 as they have blocked each other.

<img width="940" height="556" alt="image" src="https://github.com/user-attachments/assets/f0de431f-7465-4e8a-9eb2-88475a92119d" />
<img width="940" height="556" alt="image" src="https://github.com/user-attachments/assets/e5b9ec17-5288-4d94-89cc-5afbf00f3281" />

Furthermore As we can see here these are how the pings are transmit.



<img width="940" height="556" alt="image" src="https://github.com/user-attachments/assets/1fd7353b-4428-4cc8-93d4-c0a631ba80df" />
Here we can see that the bandwidth is 8.06MBps like that of the linear tree network. It also has a similar throughput of 0.965346534653 MBps which makes sense since they have to pass through a similar amount of switches to reach their location.


![Uploading image.png…]()


This is the flow table
