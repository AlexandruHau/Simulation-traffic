import random 
import numpy as np
import matplotlib.pyplot as plt

class Cellular_Automata(object):

    def __init__(self, no_cells, density, no_iter):
        # Initialize the constructor
        # Read from the keyboard the input values
        self.road = np.zeros( (2, no_cells) )
        # Array for the state of each car (has/has not moved)
        self.state = np.zeros( (1, no_cells) )
        # For the simulation of the traffic, the cells with car have state 1
        # The cells are randomly chosen
        no_cars = round( density * no_cells )
        self.car = no_cars
        for i in range (no_cars):
            r = random.randint(0, no_cells - 1)
            while ( self.road[0][r] == 1):
                r = random.randint(0, no_cells - 1)
            self.road[0][r] = 1
            # State array with cells 0 involves empty cells, 1 are used for stationary cars
            # and -1 for cars which previously moved
            self.state[0][r] = 1
        print("The number of the cars is: " + str(no_cars))
        

    def modify_step(self, no_cells, p_move, p_stay):
        # Modify the next step for the traffic using the rule specified below
        moving_cars = 0
        for i in range (no_cells):
            # If the cell has state 1
            if(self.road[0][i] == 1):

                if(self.road[0][ (i+1) % no_cells ] == 0):
                    if(self.state[0][i] == -1):
                        r = random.random()
                        if(r <= p_move):
                            self.road[1][i] = 0
                            self.road[1][(i+1) % no_cells] = 1
                            self.state[0][i] = 0
                            self.state[0][ (i+1) % no_cells ] = -1
                            moving_cars += 1
                    if(self.state[0][i] == 1):
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
        # The first row takes the value of the second row to repeat the process
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
