import numpy as np 
import matplotlib.pyplot as plt

from Automata import Cellular_Automata


class Test_Automata(object):

    def main(self): 

        no_cells = int( input ("Introduce the number of cells: ") )
        density = float( input ( "Introduce the car density for the traffic simulation: ") )
        no_iter = int( input ("Introduce the number of iterations: ") )
        p_move = float( input ("Chance of a car to move if it previously moved: ") )
        p_stay = float( input ("Chance of a car to move if it previously stayed: ") )
        
        cars = Cellular_Automata(no_cells, density, no_iter)
        road, timestep, avg_speed = cars.plot_normal_traffic(no_cells, no_iter, p_move, p_stay)
        # Plot the movement of cars in time
        plt.imshow(road[:,1:-1], interpolation = 'none', origin = 'lower')
        plt.xlabel("no of cars")
        plt.ylabel("timestep")
        plt.show()
        # Plot the density function depending on time (iteration)
        plt.plot(timestep, avg_speed)
        plt.xlabel("timestep")
        plt.ylabel("average speed")
        plt.show()
        # Print the steady state, which is the average speed after a long time
        print("The steady state of the traffic is: " + str(avg_speed[-1]) )

test = Test_Automata()
test.main()