# ann_assignments
Neural networks implemented as part of CS15-1705E2 Artificial Neural Networks at Cochin University

## Neural Networks implemented
Dependencies:
	1. Python 3
	2. Matplotlib
### 1. Maxnet ###
MAXNET [Lippmann, 1987] is a specific example of a neural net based
on competition. It can be used as a subnet to pick the node whose input is
the largest. The m nodes in this subnet are completely interconnected,
with symmetric weights.
There is no training algorithm for the MAXNET; the weights are fixed.

### 2. Mexican Hat ###
The Mexican Hat network [Kohonen, 1989a] is a more general contrast-
enhancing subnet than the MAXNET. Three types of links can be found
in such network:

	1- Each neuron is connected with excitatory (positively weighted)
	links to a number of "cooperative neighbors," neurons that are in
	close proximity.
	
	2- Each neuron is also connected with inhibitory links (with negative
	weights) to a number of "competitive neighbors," neurons that are
	somewhat further away.
	
	3- There may also be a number of neurons, further away still, to
	which the neuron is not connected.
	
All of these connections are within a particular layer of a neural net, so,
as in the case of MAXNET, the neurons receive an external signal in
addition to these interconnection signals.

Note: Add corrections file with mexican hat
