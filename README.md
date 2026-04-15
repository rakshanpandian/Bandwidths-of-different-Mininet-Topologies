# Bandwidths-of-different-Mininet-Topologies

Different network topologies give different throughputs based on the Bandwidths they are provided with. Here I will be testing out three different types of topologies on two types of Bandwidth values to show how they change with time.

# Bus Topology
In a Bus Topology there is a singular linear line by which every host sends it's packets via the shared channel. Each host has a switch and each switch is connected to each other. The switch at the end however is not connected to the switch at the beginning. There is a clearly defined beginning and end present.<br>

## Bandwidth 10MBps

## Bandwidth 50MBps

# Ring Topology
Think about what would happen if you linked the end of the line with it's beginning and you'd arrive at the ring topology. Due to it's more complex structure it can run into more issues.

## Bandwidth 10MBps

## Bandwidth 50MBps

# Tree Topology
With this topology a switch has one or more host nodes tied to it. Every switch at the very bottom level of a 'tree' is connected to a set of switches above. And so on and so on till there is a singular root switch which controls all communication with seperate parts of the network.
