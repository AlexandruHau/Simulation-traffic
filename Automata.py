import random 
import numpy as np
import matplotlib.pyplot as plt

class Cellular_Automata(object):

    # Initialize the constructor
    # Read from the keyboard the input values: the number of cells for the road, car density and the number of iterations
    # The road will be modified just below, in the constructor. The declaration has been made here for easier code handling
    def __init__(self, no_cells, density, no_iter):
        # The road is initialized as a matrix of two numpy arrays. This is to outline the road initially and after each car has gone a certain step distance
        self.road = np.zeros( (2, no_cells) )
        # Another array has been defined for the state of the cell. In this task, it s taken into account whether the car has previously moved or not. 
        # Initially, all the states of the cells within the state array are 1
        self.state = np.zeros( (1, no_cells) )
        # Some random cells are selected, standing for the cars (the filled cells)
        # Work out the number of cars as function of the given traffic density and the desired number of cells
        no_cars = round( density * no_cells )
        self.car = no_cars
        for i in range (no_cars):
            # If the selected cell is already filled, try another value, until an empty one has been found
            r = random.randint(0, no_cells - 1)
            while ( self.road[0][r] == 1):
                r = random.randint(0, no_cells - 1)
            # Once an empty cell has been found, it is filled
            self.road[0][r] = 1
            # State array with cells 0 involves empty cells, 1 are used for stationary cars
            # and -1 for cars which previously moved. Initially, all cars that are created have state 1
            self.state[0][r] = 1
        print("The number of the cars is: " + str(no_cars))
        

    def modify_step(self, no_cells, p_move, p_stay):
        # Modify the next step for the traffic using the rule specified below
        # It is taken into account whether the car has previously moved or not
        moving_cars = 0
        for i in range (no_cells):
            # If the cell has state 1
            if(self.road[0][i] == 1):
                # Analyse the case where the next cell is empty
                # When the last cell is reached, the next value will be the first cell. Hence, the modulo operation.
                if(self.road[0][ (i+1) % no_cells ] == 0):
                    # Analyse if the car has previously moved. This is why two arrays have been created. self.road array retains only the curent state of the cell.
                    # On the other hand, self.state array also takes into account the previous state of the cell. If the car has previously moved and 
                    # is now located at position i, then self.state[0][i] will have value -1. If the car has not moved and is at position i, then self.state[0][i] 
                    # will have value 0. The two cases are analysed below
                    if(self.state[0][i] == -1):
                        r = random.random()
                        if(r <= p_move):
                            # If the car moves, update the values of the road and state numpy arrays. The car leaves the current cell at position i and moves to position (i+1)
                            # or 0 if the car is located at the last cell
                            self.road[1][i] = 0
                            self.road[1][(i+1) % no_cells] = 1
                            self.state[0][i] = 0
                            self.state[0][ (i+1) % no_cells ] = -1
                            # Update the number of cars which have moved
                            moving_cars += 1
                    if(self.state[0][i] == 1):
                        # In this case, the car has not previously moved
                        r = random.random()
                        if(r <= p_stay):
                            self.road[1][i] = 0
                            self.road[1][(i+1) % no_cells] = 1
                            self.state[0][i] = 0
                            self.state[0][ (i+1) % no_cells ] = -1
                            moving_cars += 1
                else:
                    self.road[1][i] = 1
                    self.state[0][i] = 1
            # If the cell has state 0
            if(self.road[0][i] == 0):
                # The same cases are analysed here, ony from the motion of the cars behind cell located at position i 
                if(self.road[0][ (i-1) % no_cells ] == 1):
                    if(self.state[0][i] == -1):
                        r = random.random()
                        if(r <= p_move):
                            self.road[1][i] = 1
                            self.road[1][(i-1) % no_cells] = 0
                            self.state[0][i] = -1
                            self.state[0][ (i-1) % no_cells ] = 0
                    if(self.state[0][i] == 1):
                        r = random.random()
                        if(r <= p_stay):
                            self.road[1][i] = 1
                            self.road[1][(i-1) % no_cells] = 0
                            self.state[0][i] = -1
                            self.state[0][ (i-1) % no_cells ] = 0
                else:
                    self.road[1][i] = 0
                    self.state[0][i] = 0
        # The first row of the road array represents the initial state of the traffic and the second row represents the final state of the traffic.
        # Update the the initial state to be the same as the final state, in order to repeat the process
        self.road[0] = self.road[1]
        return moving_cars

    def plot_normal_traffic(self, no_cells, no_iter, p_move, p_stay):
    # Modify the traffic for the specified number of iterations and calculate the average speed of cars for each timestep
        avg_speed = []
        timestep = []
        traffic = np.zeros( (no_iter,no_cells) )
        for i in range (no_iter):
            timestep.append(i)
            moving_cars = self.modify_step(no_cells, p_move, p_stay)
            traffic[i] = self.road[0]
            avg = moving_cars / self.car
            avg_speed.append(avg)
        return traffic, timestep, avg_speed


    def output(self):
        # Print out the final grid by using string
        s = ""
        for i in range (len(self.road)):
            for j in range (len(self.road[i])):
                s += str(self.road[i][j]) + " "
            s += "\n"
        print(s)
