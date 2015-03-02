import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np

# Numpy implementation of badboids

boids_x_positions = np.array([random.uniform(-450,50.0) for x in range(50)])
boids_y_positions = np.array([random.uniform(300.0,600.0) for x in range(50)])
boid_x_velocities = np.array([random.uniform(0,10.0) for x in range(50)])
boid_y_velocities = np.array([random.uniform(-20.0,20.0) for x in range(50)])
boids=(boids_x_positions,boids_y_positions,boid_x_velocities,boid_y_velocities)
print boids_x_positions

def update_boids(boids):
	xs,ys,xvs,yvs=boids
	
	boid_count = len(xs)
	match_vel_scale = 0.125
	nearby_vel_scale = 0.01
	
	x_pos_differences = np.add.outer(xs, -xs)
	y_pos_differences = np.add.outer(ys, -ys)
	
	boid_distance = np.hypot(x_pos_differences, y_pos_differences)
	
	# Fly towards the middle
	xvs += nearby_vel_scale*(np.sum(xs)/boid_count - xs)
	yvs += nearby_vel_scale*(np.sum(ys)/boid_count - ys)
	
	
	# Fly away from nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
				xvs[i] += (xs[i]-xs[j])
				yvs[i] += (ys[i]-ys[j])
	# Try to match speed with nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
				xvs[i] += (xvs[j]-xvs[i])*0.125/len(xs)
				yvs[i] += (yvs[j]-yvs[i])*0.125/len(xs)
	# Move according to velocities
	for i in range(len(xs)):
		xs[i] += xvs[i]
		ys[i] += yvs[i]

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()