def runge_kutta(f, y0, t0, tf, dt):
    """
    Solves a system of ordinary differential equations using the Runge-Kutta method.

    Args:
        f:  Equations to solve.
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
    y = y0[:]
  
    
    results = [(t, y)]
    
    # Perform the Runge-Kutta integration
    for _ in range(n):
       
        delta_y1 = [dt * dy for dy in f(y)]
        
        y2_app = [y[j] + delta_y1[j] / 2 for j in range(len(y))]
        delta_y2 = [dt * dy for dy in f(y2_app)]
        
        y3_app = [y[j] + delta_y2[j] / 2 for j in range(len(y))]
        delta_y3 = [dt * dy for dy in f(y3_app)]
       
        y4_app = [y[j] + delta_y3[j] for j in range(len(y))]
        delta_y4 = [dt * dy for dy in f(y4_app)]
  
        # Update the state 
        y = [y[j] + (delta_y1[j] + 2 * delta_y2[j] + 2 * delta_y3[j] + delta_y4[j]) / 6 for j in range(len(y))]
        t += dt
        
        results.append((t, y))
    
    return results
