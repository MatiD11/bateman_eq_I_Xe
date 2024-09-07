import argparse
from estimate_ex_time import measure_execution_time
from bateman_eq import calc_initial_conditions, bateman_equations
from runge_kutta import runge_kutta
from matrix_method import matrix_method
from analytical_sol import calculate_errors, Xe_population
from parameters import par
from plot_results import plot_population, plot_rho, plot_err, plot_rho_matrix_3d
from bateman_eq import calculate_rho

def compute_solutions(perc, time_range, dt, compute_matrix_only=False):
    """
    Computes and returns the solutions of the Bateman equations for given flux percentage,
    using both matrix method and Runge-Kutta method, and calculates errors

    Args:
        perc: Flux percentage.
        time_range: Tuple specifying the start and end time.
        dt: Time step for the simulation.
        compute_matrix_only: Boolean flag to indicate whether to compute only the matrix method results.

    Returns:
        Depending on `compute_matrix_only`, either the matrix method results only or all results including errors.
    """
    initial_conditions = calc_initial_conditions(perc)  # Calculate initial conditions
    results_matrix = matrix_method(initial_conditions, time_range[0], time_range[1], dt)  # Matrix method results
    
    if (10 * perc % 2 == 0 and perc < 1.2):
        plot_population(results_matrix, f"matrix_{perc}")
    
    rho_matrix = [(t, calculate_rho(Xe)) for t, (_, Xe) in results_matrix]  # Calculate rho values for matrix method
    
    if not compute_matrix_only:
        results_runge_kutta = runge_kutta(bateman_equations, initial_conditions, time_range[0], time_range[1], dt) # Runge-Kutta method results
        plot_population(results_runge_kutta, f"runge_kutta_{perc}")
        
        rho_runge_kutta = [(t, calculate_rho(Xe)) for t, (_, Xe) in results_runge_kutta] # Calculate rho values for Runge-Kutta method
        rho_rk4 = [rho for _, rho in rho_runge_kutta]

        times = [t for t, _ in rho_runge_kutta]
        Xe_analytic = [Xe_population(t) for t in times]
        rho_analytic = [calculate_rho(Xe) for Xe in Xe_analytic]

        # Calculate errors between numerical and analytical solutions
        error_rk4_rho = calculate_errors(rho_rk4, rho_analytic)
        rho_mtx = [rho for _, rho in rho_matrix]
        error_matrix_rho = calculate_errors(rho_mtx, rho_analytic)

        return rho_runge_kutta, rho_matrix, error_rk4_rho, error_matrix_rho
    else:
        return rho_matrix

def process(time_range, dt):
    """
    Processes results for different flux percentages and collects data for plotting.

    Args:
        time_range: Tuple specifying the start and end time for the simulation.
        dt: Time step for the simulation.

    Returns:
        Results for Runge-Kutta method, matrix method, errors for both methods, and data used for the 3D plot.
    """
    rho_runge_kutta_all = []
    rho_matrix_all = []
    rho_runge_kutta_all_err = []
    rho_matrix_all_err = []
    rho_matrix_3D_all = []

    # Loop through flux percentages from 100% to 20% with 20% intervals
    for perc in par.FLUX_PERCS:
        rho_runge_kutta, rho_matrix, r4k_err, matrix_err = compute_solutions(perc, time_range, dt)
        rho_runge_kutta_all.append(rho_runge_kutta)
        rho_matrix_all.append(rho_matrix)
        rho_runge_kutta_all_err.append(r4k_err)
        rho_matrix_all_err.append(matrix_err)

    # Compute and collect data for 3D plot: flux percentages from 120% to 80% with 4% intervals
    for perc in par.FLUX_PERCS_3D:
        rho_matrix_3D = compute_solutions(perc, time_range, dt, compute_matrix_only=True)
        rho_matrix_3D_all.append(rho_matrix_3D)

    return rho_runge_kutta_all, rho_matrix_all, rho_runge_kutta_all_err, rho_matrix_all_err, rho_matrix_3D_all

def plot_all_results(rho_runge_kutta_all, rho_matrix_all, rho_runge_kutta_all_err, rho_matrix_all_err, rho_matrix_3D_all):
    """
    Plots all results, including populations, rho values, errors, and xenon transient surface.

    Args:
        rho_runge_kutta_all: Results from the Runge-Kutta method.
        rho_matrix_all: Results from the matrix method.
        rho_runge_kutta_all_err: Errors for the Runge-Kutta method.
        rho_matrix_all_err: Errors for the matrix method.
        rho_matrix_3D_all: 3D plot of the xenon transient surface.
    """
    plot_rho(rho_runge_kutta_all, "rho_runge_kutta")
    plot_rho(rho_matrix_all, "rho_matrix")
    plot_err(rho_runge_kutta_all, rho_runge_kutta_all_err, "rho_runge_kutta_err")
    plot_err(rho_matrix_all, rho_matrix_all_err, "rho_matrix_err")
    plot_rho_matrix_3d(rho_matrix_3D_all, "xe_transient_surface")

def main():
    
    parser = argparse.ArgumentParser(description="Bateman equation solver: Runge-Kutta and matrix method")
    
    # Command-line arguments: time range and dt can be selected manually
    parser.add_argument('--performance', action='store_true', help="Estimate execution time")
    parser.add_argument('--time-range', type=int, nargs=2, default=[0, 252000], help="Time range for the simulation (start, end)")
    parser.add_argument('--dt', type=int, default=3600, help="Time step for the simulation")
    args = parser.parse_args()
    time_range = tuple(args.time_range)
    dt = args.dt

    init_conditions = calc_initial_conditions(1)

    if args.performance: #if performance option is selected, the code calculate the execution time of the two methods
        average_rk4_time = measure_execution_time(runge_kutta, bateman_equations, init_conditions, time_range[0], time_range[1], dt)
        average_matrix_time = measure_execution_time(matrix_method, init_conditions, time_range[0], time_range[1], dt)
        print(f"Average execution time RK4: {average_rk4_time:.2f} ms")
        print(f"Average execution time matrix method: {average_matrix_time:.2f} ms")
    else:        
        rho_runge_kutta_all, rho_matrix_all, rho_runge_kutta_all_err, rho_matrix_all_err, rho_matrix_3D_all = process(time_range, dt)
        plot_all_results(rho_runge_kutta_all, rho_matrix_all, rho_runge_kutta_all_err, rho_matrix_all_err, rho_matrix_3D_all)

if __name__ == "__main__":
    main()
