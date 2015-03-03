import timeit
from badboids import update_badboids, badboids
from numpyboids import update_boids, boids
import numpy as np

def wrapper(func, *args):
    def wrapped():
        return func(*args)
    return wrapped
	
badboids_original = wrapper(update_badboids, badboids)
numpyboids = wrapper(update_boids, boids) 

time_badboids = timeit.repeat(badboids_original, repeat=20, number=100)
time_numpyboids = timeit.repeat(numpyboids, repeat=20, number=100)

print 'Original bad boids time was ' +str(np.mean(time_badboids))
print 'My Numpy bad boids time is ' +str(np.mean(time_numpyboids))

# Original bad boids time was 1.43 seconds for 100 iterations 
# My Numpy bad boids time is 0.95 seconds for 100 iterations 
