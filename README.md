# Simulation-traffic

This program analyses the motion of the cars in a traffic. All we need to know beforehand is the initial state of the traffic, given by the 
traffic density (no of cars / no of available cells). Initially, a random state is set up with the given parameters. Afterwards, the traffic is updated
at each timestep. During each iteration, the mean traffic speed is re-calculated and appended to list, so all of the mean speed values can then be plotted.
Moreover, the state of the traffic itself, at each time step, is plotted by using the imshow function from matplotlib library. The traffic flow has similar 
behaviour to the cellular automata. 

As a final task, for each car density, the mean final speed is then plotted also on matplotlib. As a note, the results are highly sensitive to the initial parameters,
particularly p_move and p_stay. p_move stands for the probability of a car to move if it has moved before. Likewise, p_stay signifies the probability of a car to stay 
if it has stayed before. 
