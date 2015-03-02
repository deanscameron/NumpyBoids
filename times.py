import timeit
from badboids import update_boids, badboids
import random

def wrapper(func, *args):
    def wrapped():
        return func(*args)
    return wrapped
badboids_original = wrapper(update_boids, badboids)

time_badboids = timeit.timeit(badboids_original, number=1000)

print 'Original bad boids time was ' +str(time_badboids)
print 'My class based bad boids time was ' 
print 'My Numpy bad boids time is ' 