import time

def measure_execution_time(method, *args):
    """
    Measures the average execution time of a given method over multiple runs.

    Args:
        method: The method to be tested
        *args: The arguments to pass to the method.

    Returns:
        The average execution time of the method in milliseconds.
    """
    times = []  

    for _ in range(300):  # Run the method 300 times
        start_time = time.perf_counter()  # Record the start time
        method(*args)  # Execute the method 
        end_time = time.perf_counter()  # Record the end time
        times.append(end_time - start_time)  

    average_time = sum(times) / len(times)  
    return average_time * 1000  # time in ms
