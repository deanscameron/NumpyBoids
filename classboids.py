"""
Implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import config
import yaml
from boids_functions import update_vel, dist_check
config=yaml.load(open("config.yml"))
from math import hypot

def distance(position_1, position_2):
    return hypot(position_1, position_2)

def update_vel(position_1, position_2, scale_factor):
    velocity_step = (position_2 - position_1)*scale_factor
    return velocity_step

def dist_check(x_position_1, x_position_2, y_position_1, y_position_2, range):
    if distance((x_position_2 - x_position_1), (y_position_2 - y_position_1)) < range:
	    return True

class Boid(object):
    def __init__(self, x_position, y_position, x_velocity, y_velocity):
        self.x_pos = x_position
        self.y_pos = y_position
        self.x_vel = x_velocity
        self.y_vel = y_velocity
        
class Boids(object):
    def __init__(self, num_boids=config['number_boids'], 
	                start_x_pos_range = config['start_x_pos_range'], 
	                start_y_pos_range = config['start_y_pos_range'],
					start_x_vel_range = config['start_x_vel_range'],
					start_y_vel_range = config['start_y_vel_range'],
					velocity_scale_factor = config['velocity_scale_factor'],
					velocity_match_factor = config['velocity_match_factor'],
					nearby_distance = config['nearby_distance'],
					match_speed_distance = config['match_speed_distance']):
	    self.num = num_boids
	    self.x_range = start_x_pos_range
	    self.y_range = start_y_pos_range
	    self.x_vel_range = start_x_vel_range
	    self.y_vel_range = start_y_vel_range
	    self.vel_fact = velocity_scale_factor
	    self.match_fact = velocity_match_factor
	    self.near_dist = nearby_distance
	    self.match_dist = match_speed_distance
	    self.random_boids()

    def random_boids(self):
        self.boids = [Boid(random.uniform(*self.x_range),
                random.uniform(*self.y_range),
                random.uniform(*self.x_vel_range),
                random.uniform(*self.y_vel_range)) for x in range(self.num)]
		
    def fly_towards_middle(self):
        # Update the velocities of boids such that they fly towards the centre
        for boid_1 in self.boids:
            for boid_2 in self.boids:
                boid_1.x_vel += update_vel(boid_1.x_pos, boid_2.x_pos, (self.vel_fact/self.num))
                boid_1.y_vel += update_vel(boid_1.y_pos, boid_2.y_pos, (self.vel_fact/self.num))

    def avoid_nearby_boids(self):   
        # Update the velocities of boids such that they fly away from nearby
		# birds in the flock
        for boid_1 in self.boids:
            for boid_2 in self.boids:
                if dist_check(boid_1.x_pos, boid_2.x_pos, boid_1.y_pos, boid_2.y_pos, self.near_dist):
                    boid_1.x_vel += update_vel(boid_2.x_pos, boid_1.x_pos, 1)
                    boid_1.y_vel += update_vel(boid_2.y_pos, boid_1.y_pos, 1)

    def match_velocities(self):
        # Update the velocities of boids such that they fly at the same 
		#speed as the rest of the flock
        for boid_1 in self.boids:
            for boid_2 in self.boids:
                if dist_check(boid_1.x_pos, boid_2.x_pos, boid_1.y_pos, boid_2.y_pos, self.match_dist):
                    boid_1.x_vel += update_vel(boid_1.x_vel, boid_2.x_vel, (self.match_fact/self.num))
                    boid_1.y_vel += update_vel(boid_1.y_vel, boid_2.y_vel, (self.match_fact/self.num))  

    def move_boids(self):
        # Boids fly according to their velocities
        for boid_1 in self.boids:
            boid_1.x_pos += boid_1.x_vel
            boid_1.y_pos += boid_1.y_vel

    def update_boids(self):
        self.fly_towards_middle()
        self.avoid_nearby_boids()
        self.match_velocities()
        self.move_boids()
    
    def boids_x_vector(self):
        v = []
        for boid_1 in self.boids:
            v.append(boid_1.x_pos)
        return v
            
    def boids_y_vector(self):
        v = []
        for boid_1 in self.boids:
            v.append(boid_1.y_pos)
        return v
    
    
boids = Boids()

figure = plt.figure()
axes = plt.axes(xlim = config['x_limits'], ylim = config['y_limits'])
scatter = axes.scatter(boids.boids_x_vector(), boids.boids_y_vector())

def animate(frame):
   boids.update_boids()
   scatter.set_offsets(zip(boids.boids_x_vector(), boids.boids_y_vector()))


anim = animation.FuncAnimation(figure, animate,
                               frames = config['animation_frame_number'], 
                               interval = config['animation_time_interval'])

if __name__ == "__main__":
    plt.show()