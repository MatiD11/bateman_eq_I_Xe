import argparse
from estimate_ex_time import measure_execution_time
from bateman_eq import calc_initial_conditions, bateman_equations
from runge_kutta import runge_kutta
from matrix_method import matrix_method
from plot_results import plot_all_results
from compute_solutions import process

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
