#The concept of generators

def squares(nums):
    for i in nums:
        yield(i*i) #We use yield to create generator

nums = [1, 2, 3, 4, 5]

sq = squares(nums)
print(sq)

#We use 'next' to get the iterations
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq)) #Another such line will give StopIteration exception

#We can still loop as 
for num in sq:
    print(num)

#We can make a generators using a list comprehensions as well
#my_squares = [x*x for x in nums]
my_squares = (x*x for x in nums)
print(my_squares)

#A generator has memeory advantages over a list
#The following snippet exhibits that
from pympler import summary, muppy
import psutil
import resource
import os
import sys
import random 
import time

def memory_usage_psutil():
    # return the memory usage in MB
    process = psutil.Process(os.getpid())
    mem = process.get_memory_info()[0] / float(2 ** 20)
    return mem

def memory_usage_resource():
    rusage_denom = 1024.
    if sys.platform == 'darwin':
        # ... it seems that in OSX the output is different units ...
        rusage_denom = rusage_denom * rusage_denom
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
    return mem

names = ['John','Corey','Adam','Steve','Rick','Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print("Memory (Before): {} Mb".format(memory_usage_psutil()))

def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))
print('Took {} Seconds'.format(t2-t1)) 

#De nada!