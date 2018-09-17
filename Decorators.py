#Decorators

def outer_function(msg):
    message = msg
    print("outer print")

    def inner_function():
        print("Innered " + message)
    return inner_function

hi = outer_function('HEY') #returned the reference to the inner_function
hi()

# A Decorator takes in a function as argument
# Modifies the function that you passed maybe add some functionality 
# Returns some function without altering the original fuction that you passed

def decorator_func(original_function):
    #Some modifier function
    def wrapper():
        print("Wrapper func executed before {}".format(original_function.__name__))
        return original_function()

    return wrapper

def display_func():
    print("Yeh hai display")

display_func = decorator_func(display_func)
display_func()

#Now instead of using the line "display_func = decorator_func(display_func)" 
# We could use "@decorator_func"

def decorator_func(original_function):
    #Some modifier function
    def wrapper():
        print("Wrapper func executed before {}".format(original_function.__name__))
        return original_function()

    return wrapper

@decorator_func
def display_func():
    print("Yeh hai display")

display_func() 

#Now if we want to use the same decorator for multiple functions
#This wouldn't work if the other function takes in arguments
#So we will make it able to take any inputs
 
def decorator_func(original_function):
    #Some modifier function
    def wrapper(*args, **kwargs):
        print("Wrapper func executed before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper

@decorator_func
def display_func():
    print("Yeh hai display")

@decorator_func
def display_info(name, age):
    print("The name is {} and age is {}".format(name, age))


display_func()
display_info('Gaitonde',54)

#We could also use decorator cllasses instead of decorator functions

class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print("Wrapper func executed before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def display_func():
    print("Yeh hai display")

@decorator_class
def display_info(name, age):
    print("The name is {} and age is {}".format(name, age))


display_func()
display_info('Gaitonde',54)

#We can also add the logging functionality in each function using decorators
def my_logger(original_function):
    import logging
    logging.basicConfig(filename = '{}.log'.format(original_function.__name__), level = logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args {} and kwargs {}'.format(args, kwargs))
        return original_function(*args, **kwargs)
    return wrapper

def my_timer(original_function):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in {} secs'.format(original_function.__name__, t2))
    return wrapper

@my_logger
def display_info(name, age):
    print('display_info ran with arguments ({},{})'.format(name, age))

import time
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({},{})'.format(name, age))

display_info('Gaitonde', 54)

#Now what if we want to use two decorators for a single functions
#Stacking the decorators like below won't solve it

def my_logger(original_function):
    import logging
    logging.basicConfig(filename = '{}.log'.format(original_function.__name__), level = logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args {} and kwargs {}'.format(args, kwargs))
        return original_function(*args, **kwargs)
    return wrapper

def my_timer(original_function):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in {} secs'.format(original_function.__name__, t2))
    return wrapper


import time
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({},{})'.format(name, age))

display_info('Sardar', 45)

#The way above works is like this
#display_info = my_logger(my_timer)
#And hence it my_logger executed my_timer's wrapper as the original_function and log it seperately
#We can solve this as 
from functools import wraps

def my_logger(original_function):
    import logging
    logging.basicConfig(filename = '{}.log'.format(original_function.__name__), level = logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args {} and kwargs {}'.format(args, kwargs))
        return original_function(*args, **kwargs)
    return wrapper

def my_timer(original_function):
    import time
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in {} secs'.format(original_function.__name__, t2))
    return wrapper


import time
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({},{})'.format(name, age))

display_info('Sardar', 45)


#We can also have parameterized decorators
def outer_decorator(prefix):
    def decorator_func(original_function):
        #Some modifier function
        def wrapper(*args, **kwargs):
            print(prefix + "Wrapper func executed before {}".format(original_function.__name__))
            return original_function(*args, **kwargs)
        return wrapper
    return decorator_func

@outer_decorator("MERA PREFIX ")
def display_func():
    print("Yeh hai display")

@outer_decorator("MERA PREFIX ")
def display_info(name, age):
    print("The name is {} and age is {}".format(name, age))


display_func()
display_info('Bunty',42)

############
#GRACIAS!
