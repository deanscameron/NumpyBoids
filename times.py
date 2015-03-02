import timeit
from badboids import update_badboids, badboids
from numpyboids import update_boids, boids

def wrapper(func, *args):
    def wrapped():
        return func(*args)
    return wrapped
	
badboids_original = wrapper(update_badboids, badboids)
numpyboids = wrapper(update_boids, boids) 

time_badboids = timeit.timeit(badboids_original, number=500)
time_numpyboids = timeit.timeit(numpyboids, number=500)

print 'Original bad boids time was ' +str(time_badboids)
print 'My class based bad boids time was ' 
print 'My Numpy bad boids time is ' +str(time_numpyboids)