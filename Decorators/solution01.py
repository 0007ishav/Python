# Import the time module
import time

# Define a decorator function named 'timer'
def timer(func):
    # This is a wrapper function that will be used to time the execution of 'func'
    def wrapper(*args, **kwargs):
        # Record the start time
        start = time.time()
        
        # Execute 'func' and store the result
        result = func(*args, **kwargs)
        
        # Record the end time
        end = time.time()
        
        # Print the execution time of 'func'
        print(f"{func.__name__} ran in {end - start}")
        
        # Return the result of 'func'
        return result
    
    # Return the wrapper function
    return wrapper

# Use the 'timer' decorator to measure the execution time of 'example_function'
@timer
def example_function(n):
    # This function simply sleeps for 'n' seconds
    time.sleep(n)

# Call 'example_function' with 'n' set to 2
example_function(2)
