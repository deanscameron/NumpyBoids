import timeit
from badboids import update_boids, boids
import random

def wrapper(func, *args):
    def wrapped():
        return func(*args)
    return wrapped
wrapped = wrapper(update_boids, boids)

time_badboids = timeit.timeit(wrapped, number=100)

print 'Original bad boids time was ' +str(time_badboids)
print 'My class bad boids time was ' 
print 'My Numpy bad boids time is ' 