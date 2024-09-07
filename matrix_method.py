import numpy as np
from scipy.linalg import expm
from parameters import par

def matrix_method(y0, t0, tf, dt):
    """
    Solves a system of ordinary differential equations using the matrix exponential method.

    Args:
        y0: Initial state of the system.
        t0: Initial time.
        tf: Final time.
        dt: Time step for the integration.

    Returns:
        A list of tuples where each tuple contains the current time and the corresponding state of the system.
    """
    # Calculate the number of steps based on the total time and time step
    n = int((tf - t0) / dt)
    # Initialize the time and state variables
    t = t0
    y = y0
    
    results = [(t, y)]
    
    # Define the matrix based on the differential equations and compute the matrix exponential 
    A = np.array([
        [-par.LAMBDA_I, 0],
        [par.LAMBDA_I, -par.LAMBDA_XE]
    ])
    matrix_exp = expm(dt * A)
    
    # Perform the matrix exponential integration
    for _ in range(n):
        y = np.dot(matrix_exp, y)
        t += dt
        
        results.append((t, y))
    
    return results
